# -*- coding:utf-8 -*-
'''
Created on 2015年7月10日

@author: nob
'''
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request
from scrapy.contrib.linkextractors import LinkExtractor
from grape.items import NewsItem, NewsDetailItem
from grape import utils

class NewsSpider(CrawlSpider):
    name = "baidu_news"
    allowed_domains = [
        "news.baidu.com",
        "163.com",
        "chinanews.com",
        "sina.com.cn",
        "",
    ]
    start_urls = [u'http://news.baidu.com/ns?cl=2&rn=20&tn=news&word='+u'pp租车']

    rules = (
        # 提取搜索百度结果
        Rule(LinkExtractor(allow=(r'news\.baidu\.com\/ns\?*', )), callback='parse'),

        # 提取新闻详情页
        Rule(LinkExtractor(allow=('')))
    )

    def parse(self, response):
        next_link = response.xpath('//*[@id="page"]/a[text()="下一页"]/@href').extract()
        if next_link:
            yield Request(url=next_link, callback=self.parse)

        for news_item in response.xpath('//li[@class="result"]').extract():
            if news_item:
                detail_link = news_item.xpath('//h3[1]/a[1]/@href').extract()

                # 解析item
                news = NewsItem()
                news['newsid'] = utils.md5(detail_link)
                news['title'] =  news_item.xpath('//h3[1]/text()').extract()
                news['desc'] = ''
                news['time'] = ''
                news['url'] = detail_link

                # 继续请求detail页面
                yield Request(url=detail_link, callback=self.parse_detail)

    def parse_detail(self, response):
        news_detail = NewsDetailItem()
        news_detail['newsid'] = utils.md5(response.url)
        news_detail['url'] = response.url
        news_detail['content'] =  response.xpath('//p/text()').extract()

        yield news_detail

