# -*- coding:utf-8 -*-
'''
Created on 2015年7月11日

@author: nob
'''
from ..common.mymongo import get_db
from ..common.mydb import get_mysql

def get_trainingset(rank, limit=100):
    docs = []
    db = get_db()
    cursor = db.trainingset.find({'rank': rank}).limit(limit)
    for item in cursor:
        docs.append(item.text)
    return docs


def get_trainingset_mysql(rank, limit=100):
    db = get_mysql()
    db.query("select * from trainingset where class=%s limit %s" % (rank, limit))
    result = db.fetchAllRows();

    # 相当于php里面的var_dump
#     print result

    # 对行进行循环
    for row in result:
        # 使用下标进行取值
#         print type(row)
#         print row[1] # class
#         print row[2] # title
#         print row[4] # content
        yield row[4]

        # 对列进行循环
#         for colum in row:
#             print colum

    # 关闭数据库
    db.close()
#     return result;



if __name__ == '__main__':
    get_trainingset_mysql(2, 5);