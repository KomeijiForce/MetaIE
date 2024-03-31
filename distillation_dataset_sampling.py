import json, re

from nltk import word_tokenize

import sys

import openai

from tqdm import tqdm

openai.api_key = sys.argv[1]
model_engine = "gpt-3.5-turbo" 

def MetaIE(sentence):

    response = ""
    
    for _ in range(5):
        try:
            response = openai.ChatCompletion.create(
            model=model_engine,
            temperature=1.0,
            messages=[
                {"role": "user", "content": f"Extract some short important information from the following sentence:\n{sentence}"},
                {"role": "system", "content": f"Important information (Format: - <label>: <span>):\n"},
            ],
            ).choices[0]['message']["content"]

            return response
        except:
            pass

def parse(sentence, qa):
    
    dataset = []
    
    words = word_tokenize(sentence)
    
    query_answers = re.findall("- (.*)?: (.*)?", qa.strip("."))
    if len(query_answers) > 0:
        for query_answer in query_answers:
            labels = ["O" for _ in words]
            query, answers = query_answer
            answers = answers.replace(" and", "").split(", ")
            for answer in answers:
                answer_words = word_tokenize(answer)
                if len(answer_words) > 0:
                    for idx in range(len(words)+1-len(answer_words)):
                        if " ".join(words[idx:idx+len(answer_words)]).lower() == " ".join(answer_words).lower():
                            labels[idx] = "B"
                            labels[idx+1:idx+len(answer_words)] = ["I" for _ in range(len(answer_words)-1)]
                    if not all([label == "O" for label in labels]):
                        query_words = word_tokenize(query)
                        data = {
                            "words": query_words + [":"] + words,
                            "ner": ["O" for word in query_words] + ["O"] + labels,
                        }
                        dataset.append(data)
    
    return dataset


sentences = open(sys.argv[2]).read().split("\n")

dataset = []

bar = tqdm(sentences)

for sentence in bar:

    iie = MetaIE(sentence)

    dataset.extend(parse(sentence, iie))

    json.dump(dataset, open(sys.argv[3], "w"))
    
    bar.set_description(f"Sampling MetaIE Data: {len(dataset)} Samples")