# -*- coding:utf-8 -*-
'''
Created on 2015年7月11日

@author: nob
'''
from pymongo import MongoClient

MONGODB_SERVER = "127.0.0.1"
MONGODB_PORT = 27016
MONGODB_DB = "grape"

def get_db():
    """
    useage: db[collection_name].insert(dict(item))
    """
    client = MongoClient(MONGODB_SERVER, MONGODB_PORT)
    db = client[MONGODB_DB]
    return db