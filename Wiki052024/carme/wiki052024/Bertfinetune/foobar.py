#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from collections import Counter
from math import sqrt
from random import Random
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
import string
import re
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse import csc_matrix
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import svds
#from scipy.stats.stats import spearmanr
from scipy.stats import spearmanr
from random import shuffle
import math
import random
from numpy import *
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from datetime import datetime
#from sparsesvd import sparsesvd
from numpy.linalg import matrix_rank
from scipy.stats import chi2_contingency
from matplotlib.pyplot import *
from numpy import inf
from scipy.linalg import svd
from scipy.linalg import eigh

from foobar import *


def build_ttest(cooccur):
    P = cooccur / np.sum(cooccur)
    w = np.array(P.sum(axis = 1))
    c = np.array(P.sum(axis=0)).T
    D_w_root_recip = np.diag(np.reciprocal(w ** (1/2)))
    D_c_root_recip = np.diag(np.reciprocal(c ** (1/2)))     
    ttest = D_w_root_recip @ (P - np.outer(w, c.T)) @ D_c_root_recip
    return ttest 

def build_count_transform(cooccur, contratype = "pmi"):
    

    if contratype == 'pmi':
        P = cooccur / np.sum(cooccur)
        sum_w = np.array(P.sum(axis = 1))
        sum_c = np.array(P.sum(axis=0)).T
        sum_w_recip_diag = np.diag(np.reciprocal(sum_w))
        sum_c_recip_diag = np.diag(np.reciprocal(sum_c))
        pmi = sum_w_recip_diag @ P @ sum_c_recip_diag
        pmi = np.log2(pmi)
        pmi[pmi == -inf] = 0
        return pmi
    elif contratype == 'ppmi':
        P = cooccur / np.sum(cooccur)
        sum_w = np.array(P.sum(axis = 1))
        sum_c = np.array(P.sum(axis=0)).T
        sum_w_recip_diag = np.diag(np.reciprocal(sum_w))
        sum_c_recip_diag = np.diag(np.reciprocal(sum_c))
        pmi = sum_w_recip_diag @ P @ sum_c_recip_diag
        pmi = np.log2(pmi)
        pmi[pmi == -inf] = 0
        ppmi = np.where(pmi < 0, 0, pmi)
        return ppmi
    elif contratype == 'root':
        rootcooccur = np.sqrt(cooccur)
        return rootcooccur
    elif contratype == 'rootroot':
        rootrootcooccur = np.sqrt(np.sqrt(cooccur))
        return rootrootcooccur
    elif contratype == 'rootcca':
        sum_w = np.array(cooccur.sum(axis = 1))
        sum_c = np.array(cooccur.sum(axis=0)).T
    
        sum_w_root_recip_diag = np.diag(np.reciprocal(sum_w ** (1/4)))
        sum_c_root_recip_diag = np.diag(np.reciprocal(sum_c ** (1/4)))
        
        rootcca = sum_w_root_recip_diag @ np.sqrt(cooccur) @ sum_c_root_recip_diag
        return rootcca

    
is_sorted = lambda a: np.all(a[:-1] <= a[1:])


def svdcadense(coutra, method = "ca"):
    
    if method == "ca":
        P = coutra / np.sum(coutra)
        w = np.array(P.sum(axis = 1))
        c = np.array(P.sum(axis=0)).T
        D_w_root_recip = np.diag(np.reciprocal(w ** (1/2)))
        D_c_root_recip = np.diag(np.reciprocal(c ** (1/2)))     
        input_ca = D_w_root_recip @ (P - np.outer(w, c.T)) @ D_c_root_recip
        ca_u, ca_s, ca_vt = svd(input_ca)
        ca_v = np.transpose(ca_vt)
        return ca_u, ca_s, ca_v
        
    elif method == "svd":
        svd_u, svd_s, svd_vt = svd(coutra)   
        svd_v = np.transpose(svd_vt)
        return svd_u, svd_s, svd_v
    
def build_gsvd(pmi, cooccur, a, b):
    beta = 1
    P = cooccur / np.sum(cooccur)
    sum_w = np.array(P.sum(axis = 1))
    sum_c = np.array(P.sum(axis=0)).T
    sum_c_beta = (sum_c ** (beta)) / np.sum(sum_c ** (beta)) 

    sum_w_pro_root = sum_w ** (a/2)
    sum_c_pro_root = sum_c_beta ** (b/2)
        
    sum_w_pro_root_diag = np.diag(sum_w_pro_root)
    sum_c_pro_root_diag = np.diag(sum_c_pro_root)
  
    input_gsvd = sum_w_pro_root_diag @ pmi @ sum_c_pro_root_diag

    gsvd_u, gsvd_s, gsvd_vt = svd(input_gsvd)
    gsvd_v = np.transpose(gsvd_vt)
    return gsvd_u, gsvd_s, gsvd_v


def svdvectors(svd_words, max_dim = 500, dim = 10):
    return svd_words[range(0, svd_words.shape[0]), :][:, range(max_dim - dim, max_dim)]

def svdvectorsincrease(svd_words, dim = 300):
    return svd_words[range(0, svd_words.shape[0]), :][:, range(dim)]

def loadglovemodel(File):
    glove_model = {}
    with open(File,'r') as f:
        for line in f:
            split_line = line.split()
            word = split_line[0]
            embedding = np.array(split_line[1:], dtype=np.float64)
            glove_model[word] = embedding
    return glove_model


def loadglovevocab(File):
    glove_model_vocab = {}
    with open(File,'r') as f:
        for line in f:
            split_line = line.split()
            word = split_line[0]
            embedding = np.array(split_line[1], dtype=np.float64)
            glove_model_vocab[word] = embedding
    return glove_model_vocab

def merge(list1, list2):
 
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
     
    return merged_list


def fittingmatrixvectors(fitting_matrix):
        fitting_matrix_words = np.asarray(fitting_matrix).flatten().reshape(fitting_matrix.shape)
        return fitting_matrix_words
    
def read_test_word_pairs_set(path):
    test = []
    with open(path) as f:
        for line in f:
            x, y, sim = line.strip().lower().split()
            test.append(((x, y), sim))
    return test

def similarity(x, y, vectors, vocab, measure):
    wx = vectors[vocab[x][0]]
    wy = vectors[vocab[y][0]]
    if measure == 'cosine':
        return np.dot(wx, wy)/(np.sqrt(np.dot(wx, wx))*np.sqrt(np.dot(wy, wy)))
    elif measure == 'dot':
        return np.dot(wx, wy)
    elif measure == 'euclidean':
        return 1 / (1+np.linalg.norm(wx-wy, axis = 0))
    
def evaluate_word_pairs(vectors, test_word_pairs_set, vocab, measure):
    results = []
    count = 0
    for (x, y), sim in test_word_pairs_set:
        if x not in vocab or y not in vocab:
            continue
        count = count + 1
        results.append((similarity(x, y, vectors, vocab, measure), sim))
    #actual, expected = zip(*results)
    return results, count#spearmanr(actual, expected)[0], count

def ws_evaluate(vectors, vocab, mearsure = 'cosine', path = "D:\\carme\\test dataset\\similarities\\wordsim353.txt"):
    
    test_word_pairs_set = read_test_word_pairs_set(path)
    
    evaluate_word_pairs_create = evaluate_word_pairs(vectors, test_word_pairs_set, vocab, mearsure)
    actual, expected = zip(*evaluate_word_pairs_create[0])
    
    return spearmanr(actual, expected)[0]

