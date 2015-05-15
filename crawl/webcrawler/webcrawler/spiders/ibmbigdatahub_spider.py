#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import json
import scrapy

from css import Css
from Date import Date
from db import Mongodb
from scrapy.conf import settings
from webcrawler.items import ArticleListItem


class BigDataHubSpider(scrapy.Spider):
    name = "ibmbigdatahub"
    db = Mongodb(settings['MONGODB_CRAWLER_SITE'])
    start_urls = db.find_sites_by_name(name)

    def parse(self, response):

        for x in xrange(1,11):
            _item = ArticleListItem()
            _item['title'] = response.xpath(Css.IBMBIGDATAHUB[x]['title']).extract()[0]
            _item['author'] = response.xpath(Css.IBMBIGDATAHUB[x]['author']).extract()[0]

            if response.xpath(Css.IBMBIGDATAHUB[x]['headImg']).extract() == []:
                _item['headImg'] = 'no img'
            else:
                _item['headImg'] = response.xpath(Css.IBMBIGDATAHUB[x]['headImg']).extract()[0]

            _item['abstract'] = response.xpath(Css.IBMBIGDATAHUB[x]['abstract']).extract()[0]
            _item['url'] = Css.IBMBIGDATAHUB['baseurl'] + response.xpath(Css.IBMBIGDATAHUB[x]['url']).extract()[0]
            _item['site'] = response.url
            _item['isContentDownload'] = False
            _item['created'] = Date.get_standard_time(response.xpath(Css.IBMBIGDATAHUB[x]['created']).extract()[0])
            yield _item





