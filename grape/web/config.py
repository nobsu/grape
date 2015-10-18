# -*- coding:utf-8 -*-

from ..config import mysqlconf as dbconf

class Config():
    DEBUG = True
    SECRET_KEY = 'development key'

    SQLALCHEMY_DATABASE_URI = 'mysql://' + dbconf['user'] + ':' + dbconf['passwd'] + '@' + dbconf['host'] + ':' + str(dbconf['port']) + '/' + dbconf['db']
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:yiqiwanshua@localhost:3306/oneblog'

