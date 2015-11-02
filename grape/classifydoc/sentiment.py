# -*- coding:utf-8 -*-
'''
Created on 2015年7月11日

@author: nob
'''
import pickle
import random

import jieba
import numpy
from sklearn import metrics
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.naive_bayes import MultinomialNB


def input_data(train_data, test_data):
    """
    训练样本输入处理:
    :param train_data: list(dict()) [{'document' : 'text', 'class' : 1},{}]
    :param test_data:
    :return:
    """
    train_words = []
    train_tags = []
    test_words = []
    test_tags = []
    for item in train_data:
        train_words.append(item['document'])
        train_tags.append(item['class'])
    for item in test_data:
        test_words.append(item['document'])
        test_tags.append(item['class'])
    return train_words, train_tags, test_words, test_tags


# 使用结巴分词
comma_tokenizer = lambda x: jieba.cut(x, cut_all=True)

def vectorize(docs):
    """
    文档向量化
    :param docs list: iterable over raw text documents
    :return:
    """
    v = HashingVectorizer(tokenizer=comma_tokenizer, n_features=30000, non_negative=True)
    train_data = v.fit_transform(docs)
    return train_data


def evaluate(actual, pred):
    """
    分类器评估：精确度、召回率
    :param actual:
    :param pred:
    :return:
    """
    m_precision = metrics.precision_score(actual, pred)
    m_recall = metrics.recall_score(actual, pred)
    return m_precision, m_recall

def train_clf(train_data, train_tags):
    """
    训练一个分类器
    :param train_data:
    :param train_tags:
    :return:
    """
    clf = MultinomialNB(alpha=0.01)
    clf.fit(train_data, numpy.asarray(train_tags))
    return clf

def persisting(clfobj, filename):
    """
    分类器持久化
    :param clfobj:
    :param filename:
    :return:
    """
    fn = 'data/pkl/' + filename + '.pkl'
    with open(fn, 'w') as f:
        pickle.dump(clfobj, f)
