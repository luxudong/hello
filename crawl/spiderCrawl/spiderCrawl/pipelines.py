# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from pymongo import MongoClient


class SpidercrawlPipeline(object):

	def __init__(self):
		self.client = MongoClient("localhost",27017)
		self.db = self.client.qiubai
		self.collection = self.db.first

	def process_item(self, item, spider):
		qbdict = dict(item)
		self.collection.insert(qbdict)
		return item

	def spider_closed():
		pass