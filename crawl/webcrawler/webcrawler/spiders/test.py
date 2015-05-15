# -*- coding: utf-8 -*-

from datetime import datetime

from  scrapy.conf import settings
from db import Mongodb
from utils import Utils
from Date import Date
import scrapy


def test_insert_website(col):
	updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	mongo = Mongodb(col)
	if mongo.collection.find({"url":'https://www.analyticszone.com/homepage/web/displayBlogsPage.action'}).count()==0:
		mongo.collection.insert({
			"url":"https://www.analyticszone.com/homepage/web/displayBlogsPage.action",
			"category":0,
			"is_dynamic":True, # dynamic website
			"updated":updated  # site update time(Y-m-d HH:MM:SS)
		})

def test_insert_list_url_md5(col):
	articles_list = Mongodb(settings['MONGODB_ARTICLES_LIST'])
	for li in articles_list.collection.find():
		url = li['url']
		print url
		mongo = Mongodb(col)
		if mongo.collection.find({"url":url}).count()==0:
			mongo.collection.insert({
				"url":url,
				"md5": Utils.get_md5(url)
			})

if __name__ == '__main__':
	# test_insert_website(settings['MONGODB_CRAWLER_SITE'])
	mongo = Mongodb(settings['MONGODB_CRAWLER_SITE'])
	d = mongo.get_site_timestamp('https://www.analyticszone.com/homepage/web/displayBlogsPage.action')
	created ='2014-10-28 19:01:36'
	cur = Date.str_to_timestamp(created)
	if cur > d:
		print 'cur:%s>d:%s' %(cur, d)
	else:
		print 'cur:%s<=d:%s' %(cur, d)
	

	# mongo.collection.update({"url":"https://www.analyticszone.com/homepage/web/displayBlogsPage.action"},{"$set":{"updated":"2014-10-28 19:01:36"}})
	# test_insert_list_url_md5(settings['MONGODB_ARTICLES_LIST_URL_MD5'])