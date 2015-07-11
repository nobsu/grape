# -*- coding:utf-8 -*-
'''
Created on 2015年7月11日

@author: nob
'''
from .db import get_db


def get_trainingset(rank, limit=100):
    docs = []
    db = get_db()
    cursor = db.trainingset.find({'rank': rank}).limit(limit)
    for item in cursor:
        docs.append(item.text)
    return docs