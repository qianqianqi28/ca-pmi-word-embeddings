## Describe how to obtain the cleaned corpus. The "enwiki-20240501-pages-articles-multistream.xml.bz2", the folder "wikiextractor240901", "he_wiki", and "he_wiki_cleaned" are stored in "carme\wiki052024"
The enwiki-20240501-pages-articles-multistream.xml.bz2 is from https://dumps.wikimedia.org/enwiki/20240501/.

The folder "wikiextractor240901" is obtained by "wikiextractor". The command in Ubuntu is python3 -m wikiextractor.WikiExtractor --json /mnt/d/240901paper3/enwiki-20240501-pages-articles-multistream.xml.bz2 -o /mnt/d. Please refer to https://github.com/attardi/wikiextractor and https://yulianudelman.medium.com/build-a-corpus-for-nlp-models-from-wikipedia-dump-file-475b21145885

The code "cleanwiki" is to tranform the folder "wikiextractor240901" created by the "wikiextractor" into corpus "he_wiki". And "cleanwiki" transforms "he_wiki" into "he_wiki_cleaned". The "he_wiki_cleaned" is used for analysis.

The code "createvacabulary" is to create a vocabulary for model. This is used in the description about how many word pairs included in Rare dataset, and the created "vocabthr1000_dic" is used in the "creatematrix".

The code "numbersentenceswords" is used to calculate how many sentences and words in the Wiki052024, and the average length of sentences.


## SVD-based methods
The code "initialmatrixwiki052024" is to create a vocabulary and a cooccurence matrix for wiki052024 with thr10000. The code "initialmatrixwiki052024" is also used to describe how many word pairs included in Rare dataset.

The code "wiki052024creatematrixinneed.ipynb" is to create the needed matrix and the spearman's correlation coefficient for wiki052024 corpus with SVD-based methods.


## GloVe. Results for Glove can be found in loadglovewiki.ipynb.
loadglovewiki.ipynb is to obtain the spearman's correlation coefficient for GloVe.

## SGNS. Results for SGNS can be found in loadword2vecwiki.ipynb.
loadword2vecwiki.ipynb is to obtain the spearman's correlation coefficient for SGNS.

## Results for SVD-based methods are obtained by wiki052024evaluation.ipynb
wiki052024evaluation.ipynb is to create the results in the paper for wiki052024 corpus with SVD-based methods.

In addition, foobar.py includes functions which are used in other codes.
The word file "cmd command to obtain the vectors from GloVe and SGNS" is the cmd command to obtain the GloVe and SGNS vectors.


The code to pre-train BERT model is in the folder "carme\wiki052024\Bertpretrain".
The code to fine-tune BERT model is in the folder "carme\wiki052024\Bertfinetune".