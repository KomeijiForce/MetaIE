import json, jsonlines
from tqdm import tqdm
from transformers import AutoModelForTokenClassification, AutoTokenizer
import torch
import numpy as np

device = torch.device("cuda:0")

path = f"models/roberta-large-metaie-5-shot-conll2003"
tokenizer = AutoTokenizer.from_pretrained(path)
tagger = AutoModelForTokenClassification.from_pretrained(path).to(device)

ent_names = ['Organization', 'Other entity', 'Person', 'Location']

def find_sequences(lst):
    sequences = []
    i = 0
    while i < len(lst):
        if lst[i] == 0:
            start = i
            end = i
            i += 1
            while i < len(lst) and lst[i] == 1:
                end = i
                i += 1
            sequences.append((start, end+1))
        else:
            i += 1
    return sequences

def is_sublst(lst1, lst2):
    for idx in range(len(lst1)-len(lst2)+1):
        if lst1[idx:idx+len(lst2)] == lst2:
            return True
    return False

def filter_tuples(data):
    filtered_data = []

    for current in data:
        conflicts = [other for other in data if other[0] == current[0] and other[2] != current[2]]
        
        if not conflicts:
            filtered_data.append(current)
        else:
            should_add = True
            for conflict in conflicts:
                if conflict[1] > current[1]:
                    should_add = False
                    break
            
            if should_add:
                filtered_data.append(current)
    
    unique_filtered_data = list(set(filtered_data))

    return unique_filtered_data

T, P, TP = 0, 0, 0

bar = tqdm([data for data in jsonlines.open(f"dataset/test.conll2003.json")])

PRED, REF = [], []

cnt = 0

for item in bar:
    sentence = " ".join(item["words"])
    label = " ".join(item["words"][:item["words"].index(':')])

    inputs = tokenizer(sentence, return_tensors="pt").to(device)
    logits = tagger(**inputs).logits[0, 1:-1]
    confidences = logits.amax(-1)
    tag_predictions = logits.argmax(-1)
    tag_references = [["B", "I", "O"].index(tag) for tag in item["ner"]]
    
    predictions = [(tokenizer.decode(inputs.input_ids[0, 1:-1][seq[0]:seq[1]]).strip(), confidences[seq[0]:seq[1]].mean().item(), label) for seq in find_sequences(tag_predictions)]
    predictions = [prediction for prediction in predictions if is_sublst(item["words"], prediction[0].split())]
    references = [(" ".join(item["words"][seq[0]:seq[1]]), label) for seq in find_sequences(tag_references)]
    
    PRED.extend(predictions)
    REF.extend(references)
    
    cnt += 1
    
    if cnt % len(ent_names) == 0:
        PRED = filter_tuples(PRED)
        PRED = [(tup[0], tup[2]) for tup in PRED]
    
        P += len(PRED)
        T += len(REF)

        TP += len([prediction for prediction in PRED if prediction in REF])

        Prec = TP/(P+1e-8)
        Rec = TP/(T+1e-8)
        F1 = TP*2/(T+P+1e-8)

        bar.set_description(f"#Prec. = {Prec*100:.4} #Rec. = {Rec*100:.4} #F1 = {F1*100:.4}")
        
        PRED, REF = [], []