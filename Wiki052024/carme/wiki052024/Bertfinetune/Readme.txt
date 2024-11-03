This is for fine tune BERT. The results about BERT-FINETUNE-LAST-LAYER and BERT-FINETUNE-FIRST-LAYER in Table 5 can be found in the "evaluatebertfinetunebase.npy" and "evaluatebertfinetunebasefirstlayer.npy", respectively.

The code "create_he_wiki_cleaned_sample" is to create he_wiki_cleaned_sample.txt file. This .txt is used to fine tune BERT.

The code "finetunebert" is to fine tune the BERT model on the 28916 sentences in "he_wiki_cleaned_sample.txt". The "finetunebert" creates "special_tokens_map", "tokenizer_config", "vocab" by tokenizer.save_pretrained, and "model.safetensors", "config", and "generation_config" by model.save_pretrained.

### For the last layer
The code "finetunebertbase" is to create "fine_tune_bert_embeddings.txt"
The code "evaluatebertfinetunebase" is to create "fine_tune_bert_vectors.npy" and "thr10000_ws_score_bert.npy"

### For the first layer
The code "finetunebertbasefirstlayer" is to create "fine_tune_bert_embeddings_first_layer.txt"
The code "evaluatebertfinetunebasefirstlayer" is to create "fine_tune_bert_vectors_first_layer.npy" and "thr10000_ws_score_bert_first_layer.npy"

In addition, the foobar.py includes functions which are used in other codes. The foobar.py is the same as the foobar.py for Text8 and BNC.

In this repository, we delete he_wiki_cleaned_sample.txt, fine_tune_bert_embeddings.txt, fine_tune_bert_embeddings_first_layer.txt, fine_tune_bert_vectors.npy, and fine_tune_bert_vectors_first_layer.npy, 
In this repository, we also delete "special_tokens_map", "tokenizer_config", "vocab", "model.safetensors", "config", and "generation_config".
