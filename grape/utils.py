# -*- coding:utf-8 -*-
'''
Created on 2015年7月10日

@author: nob
'''
def md5(str):
    import hashlib
    m = hashlib.md5()   
    m.update(str)
    return m.hexdigest()