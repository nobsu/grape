# -*- coding:utf-8 -*-
'''
Created on 2015年7月11日

@author: nob
'''
import os
import random
import pickle
import jieba
import nltk
from .trainingset import get_trainingset
from .const import PROJECT_ROOT

DATA_FOLDER = os.path.join(PROJECT_ROOT, 'data')
word_features_file = my_log = os.path.join(DATA_FOLDER, "word_features.dat")
classifierdata_file = os.path.join(DATA_FOLDER, "classifierdata.dat")

word_features = pickle.load(open(word_features_file,'r'))
classifier = pickle.load(open(classifierdata_file,"r"))

def gender_features(doc):
    global word_features
    words  = jieba.cut(doc)
    fl = (" ".join(words )).split()
    fd = {}
    for word in word_features:
        fd[u'contains(%s)'%word] = (word in fl)
    return fd

def doc_classify(article):
    """输入一篇文章分类, 输出极性rank、文章、关键词"""
    global classifier 
    data = [0] * 3
    keywords = []

    keywords += jieba.analyse.extract_tags(article['text'], topK=10)
    rank = int(classifier.classify(gender_features(article['text'])))
    article['rank'] = rank

    print "所有keywords数量：",len(keywords)
    kwfd = nltk.FreqDist(keywords)
    keywords = kwfd.keys()[:10]
    return rank, article, keywords

def classifier_train():
    # 分别获取三种不同极性的标注微博100条
    negative = get_trainingset(rank=0, limit=100)
    neutral = get_trainingset(rank=1, limit=100)
    positive = get_trainingset(rank=2, limit=100)
    someweibo = [(text, 'neg') for text in negative]
    someweibo += [(text, 'neu') for text in neutral]
    someweibo += [(text, 'pos') for text in positive]
    random.shuffle(someweibo)