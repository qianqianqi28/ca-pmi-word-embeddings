make
#QQ
#if [ ! -e text8 ]; then
#  wget http://mattmahoney.net/dc/text8.zip -O text8.gz
#  gzip -d text8.gz -f
#fi
#time ./word2vec -train text8 -output vectors.bin -cbow 1 -size 200 -window 8 -negative 25 -hs 0 -sample 1e-4 -threads 20 -binary 1 -iter 15

time ./word2vec -train bnccorpus.txt -read-vocab vocabglo.txt -output vectorsvocglo200.txt -cbow 0 -size 200 -window 2 -negative 5 -hs 0 -sample 0 -threads 20 -binary 0 -iter 15 -min-count 500
time ./word2vec -train bnccorpus.txt -read-vocab vocabglo.txt -output vectorsvocglo300.txt -cbow 0 -size 300 -window 2 -negative 5 -hs 0 -sample 0 -threads 20 -binary 0 -iter 15 -min-count 500
time ./word2vec -train bnccorpus.txt -read-vocab vocabglo.txt -output vectorsvocglo400.txt -cbow 0 -size 400 -window 2 -negative 5 -hs 0 -sample 0 -threads 20 -binary 0 -iter 15 -min-count 500
time ./word2vec -train bnccorpus.txt -read-vocab vocabglo.txt -output vectorsvocglo500.txt -cbow 0 -size 500 -window 2 -negative 5 -hs 0 -sample 0 -threads 20 -binary 0 -iter 15 -min-count 500
time ./word2vec -train bnccorpus.txt -read-vocab vocabglo.txt -output vectorsvocglo600.txt -cbow 0 -size 600 -window 2 -negative 5 -hs 0 -sample 0 -threads 20 -binary 0 -iter 15 -min-count 500



./distance vectors.bin