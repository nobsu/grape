# -*- coding:utf-8 -*-
'''
Created on 2015年7月11日

@author: nob
'''
from pymongo import MongoClient
from ..config import MongoConf

def get_db(dbname=None):
    """
    usage:  db.collection.insert_many([item1, item2])
            db[collection_name].insert(dict(item))
    """
    client = MongoClient(MongoConf.MONGODB_SERVER, MongoConf.MONGODB_PORT)
    db = client[dbname or MongoConf.MONGODB_DB]
    return db

