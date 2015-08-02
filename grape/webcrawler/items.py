# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class GrapeItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class NewsItem(Item):
    newsid = Field()
    title = Field()
    url = Field()
    desc = Field()
    time = Field()

class NewsDetailItem(Item):
    newsid = Field()
    url = Field()
    content = Field()