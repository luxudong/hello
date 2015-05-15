# -*- coding: utf-8 -*-
import scrapy
import datetime
from scrapy.selector import Selector
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle
from scrapy import log
from spiderCrawl.items import *

class QiushibaikeSpider(CrawlSpider):
    name = "qiushibaike"
    allowed_domains = ["woaidu.org"]
    start_urls = [
        # 'http://www.qiushibaike.com/hot/page/2',
        'http://www.woaidu.org/sitemap_1.html',
    ]
    rules = [
		# Rule(sle(allow=("/hot/page/\d{,4}")),follow=True,callback="parse_item"),
		Rule(sle(allow=("/sitemap_\d{,3}\.html")),follow=True,callback="parse_item"),
    ]

    def isempty(self,var):
		if len(var):
			return var[0]
		else:
			return None

    def parse_item(self, response):
        items = []
        sel = Selector(response)
        base_url = get_base_url(response)
        siteviews = sel.css('div.zuo div.zuo1 div.sousuolist')
        for view in siteviews:
        	item = SpidercrawlItem()
        	item['name'] = self.isempty(view.css('a').xpath('text()').extract())
        	items.append(item)
        # siteviews = sel.css('div.main div.content-block div.content-left div.article')
        # for view in siteviews:
        # 	item = SpidercrawlItem()
        # 	item['name'] = self.isempty(view.css('div.content').xpath('text()').extract())
        # 	item['funNumber'] = self.isempty(view.css('div.stats span.stats-vote i').xpath('text()').extract())
        # 	item['replyNumber'] = self.isempty(view.css('div.stats span.stats-comments a i').xpath('text()').extract())
        # 	relative_url = self.isempty(view.css('div.stats span.stats-comments').xpath('a/@href').extract())
        # 	item['replyUrl'] = urljoin_rfc(base_url, relative_url)
        # 	item['authorImageUrl'] = self.isempty(view.css('div.author a')[0].xpath('img/@src').extract())
        # 	item['authorName'] = self.isempty(view.css('div.author a')[1].xpath('text()').extract())
        # 	item['date'] = self.isempty(view.css('div.content').xpath('@title').extract())
        # 	item['imageUrl'] = self.isempty(view.css('div.thumb a').xpath('img/@src').extract())
        	# items.append(item)
        # 	log.msg("item : "+str(item) , level = log.INFO)
        log.msg("parsed in page : " + str(sel) , level=log.INFO)
        f = open('C:\\lxdworkplace\\crawl\\texttt.txt','w')
        f.write(str(response.body))
        return items

    def parse_start_url(self,response):
    	return self.parse_item(response)