python run_ner.py \
  --model_name_or_path KomeijiForce/roberta-large-metaie \
  --train_file dataset/train.5-shot.conll2003.json \
  --output_dir models/roberta-large-metaie-5-shot-conll2003 \
  --per_device_train_batch_size 8\
  --gradient_accumulation_steps 8\
  --num_train_epochs 100\
  --save_steps 10000\
  --learning_rate 0.00001\
  --do_train \
  --overwrite_output_dir
