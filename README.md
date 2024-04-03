# MetaIE 🌐
This is a meta-model distilled from ChatGPT-3.5-turbo for information extraction. This is an intermediate checkpoint that can be well-transferred to all kinds of downstream information extraction tasks.

## To begin 🚀
You need first to install the dependent packages.
```
pip install -r requirements.txt
```

## Distillation Dataset Sampling 📖
You can create your own distillation dataset based on your own corpus:
```
python distillation_dataset_sampling.py <your OpenAI API key> <path to your corpus (e.g. example.txt)> <path to distillation dataset (e.g. distill/metaie.json)>
```

## Meta-learning 🤖
```
bash pretrain.sh
```

## Pre-trained checkpoints 🔑
You can directly use our pre-trained MetaIE models for [English](https://huggingface.co/KomeijiForce/roberta-large-metaie) and [Multi-language](https://huggingface.co/KomeijiForce/xlm-roberta-large-metaie) from Huggingface. The readme in the Huggingface repo can help you to further understand the mechanism of MetaIE.

## Dataset 📚
Our [dataset for distillation](https://huggingface.co/datasets/KomeijiForce/MetaIE-Pretrain) is at Huggingface.

## Fine-tuning 🔧
```
bash tune_ner.sh
```

## Inference 🧠
```
python inference.py
```
