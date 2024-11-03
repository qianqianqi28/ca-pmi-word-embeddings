This is for pre train BERT. The results about BERT-PRETRAIN-LAST-LAYER and BERT-PRETRAIN-FIRST-LAYER in Table 5 can be found in the "evaluatebertpretrainbase.npy" and "evaluatebertpretrainbasefirstlayer.npy", respectively.


### For the last layer
The code "bertpretrainbase" is to create "pre_train_bert_embeddings.txt"
The code "evaluatebertfinetunebase" is to create "pre_train_bert_vectors.npy" and "thr10000_ws_score_bert.npy"



### For the first layer
The code "bertpretrainbasefirstlayer" is to create "pre_train_bert_embeddings_first_layer.txt"
The code "evaluatebertpretrainbasefirstlayer" is to create "pre_train_bert_vectors_first_layer.npy" and "thr10000_ws_score_bert_first_layer.npy"

In addition, the foobar.py includes functions which are used in other codes. The foobar.py is the same as the foobar.py for Text8 and BNC.

In this repository, we delete pre_train_bert_embeddings.txt, pre_train_bert_embeddings_first_layer.txt, pre_train_bert_vectors.npy, and pre_train_bert_vectors_first_layer.npy.
