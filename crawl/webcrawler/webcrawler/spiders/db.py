# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import redis
import hashlib
import pymongo
from Date import Date
from lxml import etree
from scrapy.conf import settings
from webcrawler.items import URLMd5Item

class Init:

	def __init__(self):
		from db import RedisFactory, Mongodb
		self.cache = RedisFactory()
		self.db = Mongodb(settings['MONGODB_ARTICLES_LIST_URL_MD5'])

	def init_redis(self):
		for col in self.db.collection.find():
			url = col['url']
			md5 = col['md5']
			if not self.cache.hexist(settings['REDIS_MAP'], url):
				self.cache.hset(settings['REDIS_MAP'], url, md5)

	def add_new_url_md5(self):
		if self.cache.exist(settings['REDIS_QUEUE']):
			for url in self.cache.query_all(settings['REDIS_QUEUE']):
				if not self.cache.hexist(settings['REDIS_MAP'], url):
					url_md5 = URLMd5Item()
					url_md5['md5'] = self.get_md5(url)
					url_md5['url'] = url
					self.db.collection.insert(dict(url_md5))
		else:
			return

	def get_md5(self, string):
		md5_str = hashlib.md5()
		md5_str.update(string)
		md5_digest = md5_str.hexdigest()
		return md5_digest


class Mongodb:
	
	def __init__(self, col):
		self.server = settings['MONGODB_SERVER']
		self.port = settings['MONGODB_PORT']
		self.db = settings['MONGODB_DB']
		self.col = col
		connection = pymongo.Connection(self.server, self.port)
		db = connection[self.db]
		self.collection = db[self.col]

	def find_sites(self):
		websites = []
		dynamic_websites = []
		for site in self.collection.find():
			if not site['is_dynamic']:
				websites.append(site['url'])
			else:
				dynamic_websites.append(site['url'])

		return websites,dynamic_websites

	def find_list_urls(self):
		list_urls = []
		for col in self.collection.find({"isContentDownload":False}):
			url = col['url']
			list_urls.append(url)

		return list_urls

	def update_website(self, site, updated):
		self.collection.update(
			{"url":site},
			{"$set":{"updated":updated}}
		)

	def get_site_timestamp(self, site):
		for site in self.collection.find({"url":site}):
			return Date.str_to_timestamp(site['updated'])

	def add_new_url_md5(self, url):
		self.collection.insert({
			"url":url,
			"md5": Utils.get_md5(url)
		})

	def update_content_download(self):
		db = Mongodb(settings['MONGODB_ARTICLES_CONTENT'])
		for col in db.collection.find():
			url = col['url']
			self.collection.update({"url":url},{"$set":{"isContentDownload":True}})

class RedisFactory:

	def __init__(self):
		self.cache = redis.StrictRedis(
			host=settings['REDIS_HOST'], 
			port=settings['REDIS_PORT'],
			db=0
		)

	def hset(self, name, key, val):
		return self.cache.hset(name, key, val)

	def hget(self, name, key):
		value = self.cache.hget(name, key)
		return value

	def hexist(self, name, key):
		return self.cache.hexists(name, key)

	def hkeys(self, name):
		return self.cache.hkeys(name)

	def push(self, queue, item):
		return self.cache.rpush(queue, item)

	def pop(self, queue):
		return self.cache.blpop(queue)

	def query_all(self, queue):
		return self.cache.lrange(queue, 0, -1)

	def query(self, queue, start, end):
		return self.cache.lrange(queue, start, end)

	def query_z(self, z_name, start, end):
		return self.cache.zrange(z_name, start, end)

	def query_all_z(self, z_name):
		return self.cache.zrange(z_name, 0, -1)
	
	def delete(self, key):
		return self.cache.delete(key)

	def exist(self, name):
		return self.cache.exists(name)

if __name__ == '__main__':

	db = Mongodb(settings['MONGODB_ARTICLES_LIST'])
	r = RedisFactory()
	for x in db.collection.find():
		if r.exist(settings['REDIS_QUEUE']):
			if not r.hexist(settings['REDIS_MAP'], x['url']):
				print r.push(settings['REDIS_QUEUE'], x['url'])
			else:
				print r.hget(settings['REDIS_MAP'], x['url'])










