# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import datetime
import traceback
import os
import sys
import json
from pprint import pprint
from scrapy import log
from pymongo.connection import MongoClient

class GrapePipeline(object):
    #def process_item(self, item, spider):
    #   return item
    """
         hack ,,,save the data to mongodb
    """
    MONGODB_SERVER = "localhost"
    MONGODB_PORT = 27017 ###!!!!!!!!!!!!!!!!!!!!!
    MONGODB_DB = "books_fs"
    def _init_(self):
        """
            The only async froamework that PyMongo fully supports is Gevent
        """
        client = MongoClient(self.MONGODB_SERVER,self.MONGODB_PORT)
        self.db = client[self.MONGODB_DB]
    @classmethod
    def from_crawler(cls, crawler):
        cls.MONGODB_SERVER = crawler.settings.get('SingleMONGODB_SERVER', 'localhost')
        cls.MONGODB_PORT = crawler.settings.getint('SingleMONGODB_PORT', 27017)
        cls.MONGODB_DB = crawler.settings.get('SingleMONGODB_DB', 'books_fs')
        pipe = cls()
        pipe.crawler = crawler
        return pipe
    #保存
    def process_item(self,item,spider):
        msg_data = {
            'url':item.get('url',''),
            'msg':item.get('msg')
        }
        result = self.db['book_detail'].insert(msg_data)
        item['mongodb_id'] = str(result)
        log.msg("Item %s wrote to MongoDB database %s/book_detail" %
                (result,self.MONGODB_DB),
                level = log.DEBUG,spider = spider)
        return item
class JsonWriterPipeline(object):
    def __init__(self):
        self.file = open('/home/guochunyan/hack/grape/data/item.js','wb')
    def process_item(self,item,spider):
        line =json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item