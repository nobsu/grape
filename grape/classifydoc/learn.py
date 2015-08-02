# -*- coding:utf-8 -*-
'''
Created on 2015年7月22日

From a labeled news corpus to learn the classifications of the documents. 
@author: nob
'''
# load data set
import jieba
from sklearn.feature_extraction.text import CountVectorizer

from ..common.mydb import Ndb

comma_tokenizer = lambda x: jieba.cut(x, cut_all=True)

def load_data():
    db = Ndb.getins()
    sql = "SELECT id, class, title, url, content, source, time FROM `trainingset`"
    result = db.query(sql)
    return result

def feature_extract():
    docs = []
    classes = []
    for item in load_data():
        docs.append(item['title'] + item['content'])
        classes.append(item['class'])

    count_vec = CountVectorizer(tokenizer=comma_tokenizer)
#     count_vec.fit_transform(raw_documents, y)

if __name__ == '__main__':
    
    load_data()