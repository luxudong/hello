# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
import pymongo

class MongodbPipeline:
	
	def __init__(self, col):
		self.server = settings['MONGODB_SERVER']
		self.port = settings['MONGODB_PORT']
		self.db = settings['MONGODB_DB']
		self.col = col
		connection = pymongo.Connection(self.server, self.port)
		db = connection[self.db]
		self.collection = db[self.col]

class WebcrawlerPipeline(object):
    def process_item(self, item, spider):
        return item


class ArticleContentPipeline(object):
	def process_item(self, item, spider):

		db = MongodbPipeline(settings['MONGODB_ARTICLES_CONTENT'])
		db.collection.insert(dict(item))
		_db = MongodbPipeline(settings['MONGODB_ARTICLES_LIST'])
		_db.collection.update({'url':item.url},{"$set":{"isContentDownload":True}})

		return item
