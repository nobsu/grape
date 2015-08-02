# -*- coding:utf-8 -*-
'''
Created on 2015年7月22日

@author: nob
'''

class MongoConf(object):
    MONGODB_SERVER = "127.0.0.1"
    MONGODB_PORT = 27017
    MONGODB_DB = "grape"

class MysqlConf(object):
    HOST = '127.0.0.1'
    PORT = 3306
    USER = 'production'
    PASSWD = 'BEEQXXTGICARSCLU'
    DB = 'grape'
    CHARSET = 'utf8'

mysqlconf = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'yiqiwanshua',
    'db': 'grape',
    'charset': 'utf8',
}
# mysqlconf = {
#     'host': '127.0.0.1',
#     'port': 3306,
#     'user': 'production',
#     'passwd': 'BEEQXXTGICARSCLU',
#     'db': 'grape',
#     'charset': 'utf8',
# }