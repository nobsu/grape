# -*- coding:utf-8 -*-
'''
Created on 2015年7月22日

From a labeled news corpus to learn the classifications of the documents. 
@author: nob
'''
import pickle
import random

import jieba
import numpy
from sklearn import metrics
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.naive_bayes import MultinomialNB

from ..common.mydb import Ndb


def load_data():
    db = Ndb.getins()
#     sql = "SELECT id, class, title, url, content, source, time FROM `trainingset`"
#     sql = "SELECT id, class, title as document FROM `trainingset`"
    sql = "SELECT id, class, concat(title, '.', content) as document FROM `trainingset`"
    result = db.query(sql)
    data = []
    for item in result:
        data.append(item)
    return data

def input_data(train_data, test_data):
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

# with open('stopwords.txt', 'r') as f:
#     stopwords = set([w.strip() for w in f])
comma_tokenizer = lambda x: jieba.cut(x, cut_all=True)


def vectorize(train_words):
    v = HashingVectorizer(tokenizer=comma_tokenizer, n_features=30000, non_negative=True)
    train_data = v.fit_transform(train_words)
    return train_data


def evaluate(actual, pred):
    m_precision = metrics.precision_score(actual, pred)
    m_recall = metrics.recall_score(actual, pred)
    return m_precision, m_recall

def train_clf(train_data, train_tags):
    clf = MultinomialNB(alpha=0.01)
    clf.fit(train_data, numpy.asarray(train_tags))
    return clf

def persisting(clfobj, filename):
    fn = 'data/pkl/' + filename + '.pkl'
    with open(fn, 'w') as f:
        pickle.dump(clfobj, f) 


def main():
    data = load_data()
    random.shuffle(data)
    size = len(data)
    cent = size / 6
    train_data = data[:cent * 5 ]
    test_data = data[cent:]
    train_words, train_tags, test_words, test_tags = input_data(train_data, test_data)
    train_data = vectorize(train_words)
    test_data = vectorize(test_words)
    clf = train_clf(train_data, train_tags)
    pred = clf.predict(test_data)
    
    m_precision, m_recall = evaluate(numpy.asarray(test_tags), pred)
    print 'precision:{0:.3f}'.format(m_precision)
    print 'recall:{0:0.3f}'.format(m_recall)

    filename = 'clf_{0:.3f}_{1:.3f}'.format(m_precision, m_recall)
    persisting(clf, filename)


if __name__ == '__main__':
    main()
