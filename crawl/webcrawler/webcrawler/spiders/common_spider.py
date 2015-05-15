#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import scrapy
from scrapy.conf import settings
from db import Mongodb, RedisFactory
from webcrawler.items import ArticleContentItem


class CommonSpider(scrapy.Spider):
    name = "common"
    article_list = Mongodb(settings['MONGODB_ARTICLES_LIST'])  
    start_urls = article_list.find_list_urls()

    def parse(self, response):

		article = ArticleContentItem()
		article['url'] = response.url
		article['source'] = response.xpath("//html/body").extract()[0]
		article['isParse'] = False
		return article
