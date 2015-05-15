# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WebcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ArticleListItem(scrapy.Item):
	title = scrapy.Field()
	author = scrapy.Field()
	headImg = scrapy.Field()
	abstract = scrapy.Field()
	url = scrapy.Field()
	site = scrapy.Field()
	isContentDownload = scrapy.Field()
	created = scrapy.Field()

class ArticleSiteItem(scrapy.Item):
	site = scrapy.Field()
	source = scrapy.Field()
	updated = scrapy.Field()


class ArticleContentItem(scrapy.Item):
	url = scrapy.Field()
	source = scrapy.Field()
	isParse = scrapy.Field()

class URLMd5Item(scrapy.Item):
	url = scrapy.Field()
	md5 = scrapy.Field()



