# -*- coding:utf-8 -*-
'''
Created on 2015年7月11日

@author: nob
'''
import hashlib
import urlparse

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

# 获取url中的参数
def parse_url_arg(url):
    result=urlparse.urlparse(url)
    return urlparse.parse_qs(result.query,True) 