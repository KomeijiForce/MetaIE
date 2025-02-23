# MetaIE 🌐 [[Paper]](https://arxiv.org/abs/2404.00457)
This is a meta-model distilled from ChatGPT-3.5-turbo for information extraction. This is an intermediate checkpoint that can be well-transferred to all kinds of downstream information extraction tasks.

![MetaIE](https://github.com/KomeijiForce/MetaIE/blob/main/metaie_overview.png)

Update: We release a new model by merging the ability of MetaIE and massive other resources into it: [Cuckoo](https://github.com/KomeijiForce/Cuckoo).

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

If you don't want to spend money, you can replace the ```train_file``` argument in the meta-learning script by ```KomeijiForce/MetaIE-Pretrain```, which is used for our experiment.

## Meta-learning 🤖
```
bash pretrain.sh
```

## Pre-trained checkpoints 🔑
You can directly use our pre-trained MetaIE models for [English](https://huggingface.co/KomeijiForce/roberta-large-metaie) and [Multi-language](https://huggingface.co/KomeijiForce/xlm-roberta-large-metaie) from Huggingface. The readme in the Huggingface repo can help you to further understand the mechanism of MetaIE.

Update: A GPT-4-distilled [Checkpoint](https://huggingface.co/KomeijiForce/roberta-large-metaie-gpt4) is available now!

Update: A GPT-4o-distilled [Checkpoint](https://huggingface.co/KomeijiForce/roberta-large-metaie-super-academia-gpt4o) for Academia Domain is available now!

## Dataset 📚
Our [dataset for distillation](https://huggingface.co/datasets/KomeijiForce/MetaIE-Pretrain) is at Huggingface.

## Downstream Scenario (CoNLL2003 as an instance) 🛠️

### Fine-tuning 🔧
```
bash tune_ner.sh
```

### Inference 🧠
```
python inference.py
```

## Citation 📝

```bibtex
@article{MetaIE,
  author       = {Letian Peng and
                  Zilong Wang and
                  Feng Yao and
                  Zihan Wang and
                  Jingbo Shang},
  title        = {MetaIE: Distilling a Meta Model from {LLM} for All Kinds of Information
                  Extraction Tasks},
  journal      = {CoRR},
  volume       = {abs/2404.00457},
  year         = {2024},
  url          = {https://doi.org/10.48550/arXiv.2404.00457},
  doi          = {10.48550/ARXIV.2404.00457},
  eprinttype    = {arXiv},
  eprint       = {2404.00457},
  timestamp    = {Wed, 08 May 2024 17:22:41 +0200},
  biburl       = {https://dblp.org/rec/journals/corr/abs-2404-00457.bib},
  bibsource    = {dblp computer science bibliography, https://dblp.org}
}
```
