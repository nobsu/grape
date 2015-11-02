# -*- coding:utf-8 -*-
'''
Created on 2015年7月22日

@author: nob
'''
import os

class MongoConf(object):
    MONGODB_SERVER = "127.0.0.1"
    MONGODB_PORT = 27017
    MONGODB_DB = "grape"

mysqlconf = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'yiqiwanshua',
    'db': 'grape',
    'charset': 'utf8',
}

PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))