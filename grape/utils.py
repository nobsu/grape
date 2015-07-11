# -*- coding:utf-8 -*-
'''
Created on 2015年7月10日

@author: nob
'''
import hashlib

def md5(str):
    m = hashlib.md5()   
    m.update(str)
    return m.hexdigest()

def md5hex(word):  
     """ MD5加密算法，返回32位小写16进制符号 
     """   
     if isinstance(word, unicode):  
         word = word.encode("utf-8")  
     elif not isinstance(word, str):  
         word = str(word)  
     m = hashlib.md5()  
     m.update(word)  
     return m.hexdigest() 