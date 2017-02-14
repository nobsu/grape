# -*- coding:utf-8 -*-
'''
Created on 2015年7月22日

turn this on a training set and attempt to predict the label
@author: nob
'''
import os
import pickle
from ..config import PROJECT_ROOT
from .sentiment import vectorize


DATA_FOLDER = os.path.join(PROJECT_ROOT, 'data/pkl')
clf_file = os.path.join(DATA_FOLDER, "clf_0.913_0.931.pkl")

clf = pickle.load(open(clf_file, "rb"))


allclftype = ['news', 'weibo', 'car']
classdict = {0 : u'中性', 1 : u'正向', 2 : u'负向'}


def document_classify(clf_type, content, title):
    """
    文档分类
    :param clf_type:
    :param content:
    :param title:
    :return:
    """
    ret = []
    docs = []
    docs.append(content + title)

    # 文档列表向量化
    vdata = vectorize(docs)

    # 分类预测
    pred = clf.predict(vdata)
    for c in pred:
        ret.append(classdict.get(c, u'未知类别'))
    return ret


def load_classifier(clf_type):
    if clf_type in allclftype:
        pass



def persisting(clfobj, filename):
    fn = 'data/pkl/' + filename + '.pkl'
    with open(fn, 'w') as f:
        pickle.dump(clfobj, f)