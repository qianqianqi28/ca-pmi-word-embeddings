The enwiki-20240501-pages-articles-multistream.xml.bz2 is from https://dumps.wikimedia.org/enwiki/20240501/.

The folder "wikiextractor240901" is obtained by "wikiextractor". The command in Ubuntu is python3 -m wikiextractor.WikiExtractor --json /mnt/d/240901paper3/enwiki-20240501-pages-articles-multistream.xml.bz2 -o /mnt/d. Please refer to https://github.com/attardi/wikiextractor and https://yulianudelman.medium.com/build-a-corpus-for-nlp-models-from-wikipedia-dump-file-475b21145885

he_wiki.txt file and "he_wiki_cleaned" are created by the cleanwiki.ipynb. The "he_wiki_cleaned" is used for analysis.

The above files are not shown in this repository.

## SVD-based method

The folder "decomposed matrix" is matrices and SVD of matrices, which are created by code/createvacabulary.ipynb, code/initialmatrixwiki052024.ipynb, and code/wiki052024creatematrixinneed.ipynb except for thre10000_raw_ttest.npy. thre10000_raw_ttest.npy is copied from decomposed matrix/thre10000_ttest.npy.

The folder "Table 2" is the word similarity results for Table 3 in the paper, which are created by code/wiki052024creatematrixinneed.ipynb and are used in wiki052024evaluation.ipynb.

## GloVe

The GloVe-master.zip is from https://github.com/stanfordnlp/GloVe/tree/master. GloVe-master.zip is not shown in this repository.
The folder "GloVe-master" is uncompressed GloVe-master.zip.

## SGNS

The source-archive.zip is from https://code.google.com/archive/p/word2vec/source/default/source. source-archive.zip is not shown in this repository.
The folder "source-archive" is uncompressed source-archive.zip.

## .NPY files
In the "carme/wiki052024", "wiki052024_ws_score_glove.npy" file is created by code/loadglovewiki.ipynb, "wiki052024_ws_score_sgns.npy" file is created by code/loadword2vecwiki.ipynb. The other seven .npy files, which are used in wiki052024evaluation.ipynb, are created by code/wiki052024creatematrixinneed.ipynb.

## Bertpretrain folder and Bertfinetune folder
Bertpretrain forder is to obtain the pre-train BERT results.
Bertfinetune forder is to obtain the fine-tune BERT results.