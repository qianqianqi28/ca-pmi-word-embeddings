The folder "decomposed matrix" includes 38 .npy files:
vocab, vocabthr1000_dic, and vocabthr1000_dic_index are from code/createvacabulary.ipynb.
cooccur_dense_thr10000, cooccur_sparse_thr10000, vocabthr10000_dic, and vocabthr10000_dic_index are from code/initialmatrixwiki052024.ipynb.
thre10000_raw_ttest is copied from decomposed matrix/thre10000_ttest.npy.
the other 30 .npy files are created by code/bnccreatematrixinneed.ipynb.

The folder "decomposed matrix" includes 2 .txt files:
vocabthr1000 is from code/createvacabulary.ipynb.
vocabthr10000 is from code/initialmatrixwiki052024.ipynb.

It is worth noting that in this Wiki052024, we perform SVD on the created ttest (raw_ttest), root-ttest, rootroot-ttest to obtain the CA solution. However, in Text8 and BNC, we perform CA on the raw, root, rootroot matrices. These two methods can obtain the same CA solution.

These 40 files are not shown in this repository.