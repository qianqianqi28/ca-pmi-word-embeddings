The 2554.zip is from https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2554.

The folder "2554" is the uncompressed 2554.zip.
bnccorpus.txt file is created by the initialmatrixbnc.ipynb.
bnccorpus.txt is used in "GloVe-master" and "source-archive".
The above files are not shown in this repository.


## SVD-based method

The folder "decomposed matrix" is matrices and SVD of matrices, which are created by code/initialmatrixbnc.ipynb and code/bnccreatematrixinneed.ipynb except for bnc_raw.npy. bnc_raw.npy is copied from decomposed matrix/bnc_cooccur_dense.npy.

The folder "Table 2" is the word similarity results for Table 2 in the paper, which are created by code/bnccreatematrixinneed.ipynb and are used in text8bncevaluation.ipynb.

## GloVe

The GloVe-master.zip is from https://github.com/stanfordnlp/GloVe/tree/master. GloVe-master.zip is not shown in this repository.
The folder "GloVe-master" is uncompressed GloVe-master.zip.

## SGNS

The source-archive.zip is from https://code.google.com/archive/p/word2vec/source/default/source. source-archive.zip is not shown in this repository.
The folder "source-archive" is uncompressed source-archive.zip.

## .NPY files
In the "carme/bnc", "bnc_ws_score_glove.npy" file is created by code/loadglove.ipynb, "bnc_ws_score_sgns.npy" file is created by code/loadword2vec.ipynb. The other seven .npy files are created by code/bnccreatematrixinneed.ipynb. These .npy files are used in text8bncevaluation.ipynb.