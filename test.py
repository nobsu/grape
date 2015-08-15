# -*- coding:utf-8 -*-
'''
Created on 2015年7月22日

@author: nob
'''
from grape.classifydoc.learn import load_data, main
from grape.common.mydb import Ndb


def mongotest():
    from grape.common.mymongo import get_db
    db = get_db()

    data = [{"x": 1, "tags": ["dog", "cat"]},
            {"x": 2, "tags": ["cat"]},
            {"x": 2, "tags": ["mouse", "cat", "dog"]},
            {"x": 3, "tags": []}]

    result = db.test.insert_many(data)
    print result.inserted_ids

if __name__ == '__main__':
    main()
