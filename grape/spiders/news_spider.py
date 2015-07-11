# -*- coding:utf-8 -*-
'''
Created on 2015年7月10日

@author: nob
'''
import logging
import scrapy
from scrapy.spiders import Spider
from scrapy.http import Request
from grape.items import NewsItem, NewsDetailItem
import grape.utils

class NewsSpider(Spider):
    name = "baidu_news"
#     allowed_domains = [
#         "news.baidu.com",
#         "163.com",
#         "chinanews.com",
#         "sina.com.cn",
#         "",
#     ]
    start_urls = [u'http://news.baidu.com/ns?cl=2&rn=20&tn=news&word='+u'pp租车']

    def parse(self, response):
        next_link = response.xpath(u'//*[@id="page"]/a[text()="下一页"]/@href').extract()
        if next_link:
            yield Request(url=next_link, callback=self.parse)

        for news_item in response.xpath('//li[@class="result"]'):
            if news_item:
                detail_link = news_item.xpath('./h3[1]/a[1]/@href').extract()

                # 解析item
                news = NewsItem()
                news['newsid'] = utils.md5hex(detail_link)
                news['title'] =  news_item.xpath('./h3[1]/text()').extract()
                news['desc'] = ''
                news['time'] = ''
                news['url'] = detail_link[0]

                # 继续请求detail页面
                yield Request(url=detail_link[0], callback=self.parse_detail)

    def parse_detail(self, response):
        news_detail = NewsDetailItem()
        news_detail['newsid'] = utils.md5hex(response.url)
        news_detail['url'] = response.url
        news_detail['content'] =  response.xpath('//p/text()').extract()

        yield news_detail

