# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from pymongo import MongoClient

class MongoPipeline(object):
    """
         hack ,,,save the data to mongodb
    """

    def __init__(self, mongo_uri, mongo_port, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_port = mongo_port
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGODB_SERVER'),
            mongo_port=crawler.settings.get('MONGODB_PORT', 27016),
            mongo_db=crawler.settings.get('MONGODB_DB', 'grape')
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri, self.mongo_port)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        collection_name = item.__class__.__name__
        self.db[collection_name].insert(dict(item))
        return item



class JsonWriterPipeline(object):
    def __init__(self):
        self.file = open('/home/guochunyan/hack/grape/data/item.js','wb')
    def process_item(self,item,spider):
        line =json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item