In the "GloVe-master/GloVe-master", the "demo.sh" file is changed to create vectors that we need. We add the "he_wiki_cleaned" file to "GloVe-master/GloVe-master". 

Then we run the demo.sh by the command on the "cmd command to obtain the vectors from GloVe and SGNS". 
After we run, the "build" folder, "coocurrence.bin", "coocurrence.shuff.bin", "vocab", "vectors200", "vectors300", "vectors400", "vectors500", "vectors600" are created.

After we run, in "GloVe-master/GloVe-master"：
we delete the original files from the GloVe-master.zip: ".gitignore", ".trais.yml", "LICENSE", "Makefile", "randomization.test", "README", "src" folder, "eval" folder;
we also delete the files "build" folder, "coocurrence.bin", "coocurrence.shuff.bin" which are created by the demo.sh; 
we also delete the "he_wiki_cleaned" file;
we also delete the "vocab", "vectors200", "vectors300", "vectors400", "vectors500", "vectors600" which are used in the code/loadglovewiki.npy.

In conclusion, here we use the "demo.sh" file to create the "vocab", "vectors200", "vectors300", "vectors400", "vectors500", "vectors600", which are used in the loadglovewiki.npy.
