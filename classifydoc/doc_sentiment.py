# -*- coding:utf-8 -*-
'''
Created on 2015年7月11日

@author: nob
'''
import random
import jieba
from .trainingset import get_trainingset

# word_features_file = my_log = os.path.join(Config.DATA_FOLDER, "word_features.dat")
# classifierdata_file = os.path.join(Config.DATA_FOLDER, "classifierdata.dat")

def gender_features(weibo):
    global word_features
    a = jieba.cut(weibo)
    fl = (" ".join(a)).split()
    fd = {}
    for word in word_features:
        fd[u'contains(%s)'%word] = (word in fl)
    return fd


def classifier_train():
    # 分别获取三种不同极性的标注微博100条
    negative = get_trainingset(rank=0, limit=100)
    neutral = get_trainingset(rank=1, limit=100)
    positive = get_trainingset(rank=2, limit=100)
    someweibo = [(text, 'neg') for text in negative]
    someweibo += [(text, 'neu') for text in neutral]
    someweibo += [(text, 'pos') for text in positive]
    random.shuffle(someweibo)