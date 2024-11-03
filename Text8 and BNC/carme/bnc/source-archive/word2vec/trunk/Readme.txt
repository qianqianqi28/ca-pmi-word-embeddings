In the "source-archive\word2vec\trunk", the "demo-word.sh" file is changed to create vectors that we need. We add the "bnccorpus" file to "source-archive\word2vec\trunk". We add the "vocabglo" file to "source-archive\word2vec\trunk" and the "vocabglo" is copied from "vocab" of "GloVe-master/GloVe-master" which is created by GloVe.

Then we run the demo-word.sh by the command on the "code/cmd command to obtain the vectors from GloVe and SGNS". 
After we run, the "word-analogy", "word2vec", "word2phrase", "distance", "compute-accuracy", "vectorsvocglo200", "vectorsvocglo300", "vectorsvocglo400", "vectorsvocglo500", "vectorsvocglo600" are created.

After we run, 
in "source-archive\word2vec\trunk"：
we delete the original files from the source-archive.zip: "compute-accuracy.c", "demo-analogy", "demo-classes", "demo-phrase-accuracy", "demo-phrases", "demo-train-big-model-v1", "demo-word-accuracy", "distance.c", "LICENSE", "makefile", "questions-phrases", "questions-words", "README", "word2phrase.c", "word2vec.c", "word-analogy.c", ".svn" folder; 
we also delete the files "word-analogy", "word2vec", "word2phrase", "distance", "compute-accuracy" which are created by the demo-word.sh; 
we also delete the "bnccorpus" file;
we also delete the "vocabglo", "vectorsvocglo200", "vectorsvocglo300", "vectorsvocglo400", "vectorsvocglo500", "vectorsvocglo600" which are used in the code/loadword2vec.npy. 
In source-archive\word2vec, we delete ".svn" folder. 

In conclusion, we use the "demo-word.sh" file to create "vectorsvocglo200", "vectorsvocglo300", "vectorsvocglo400", "vectorsvocglo500", "vectorsvocglo600" which are used in the code/loadword2vec.npy.
