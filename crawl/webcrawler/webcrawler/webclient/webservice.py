#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import json
import datetime
import urllib2
import requests
import cookielib
import urllib
from lxml import etree 
from scrapy.conf import settings
from webcrawler.spiders.db import Mongodb
from webcrawler.webclient.HttpConstants import HttpConstants

class Webservice:

	@classmethod
	def wget(self, url):
		if (not url.startswith('http://')) and (not url.startswith('https://')):
			raise Exception('url error')
		else:
			data = ''
			req = urllib2.Request(url=url, headers=HttpConstants.HEADERS)
			# req = urllib2.Request(url=url)
			try:
				# fd = urllib2.urlopen(req,timeout=30)
				fd = urllib2.urlopen(req)
			except urllib2.HTTPError, e:
				raise Exception('HTTP ERROR: %s' %e)
			except urllib2.URLError, e:
				raise Exception('URL ERROR: %s' %e)
			while 1:
				data_contents = fd.read(1024)
				if not len(data_contents):
					break
				else:
					data += data_contents
			return data

	@classmethod
	def wget_head(self, url):
		'''
		get http headers
		'''
		if (not url.startswith('http://')) and (not url.startswith('https://')):
			raise Exception('url error')
		else:
			req = urllib2.Request(url=url, headers=HttpConstants.HEADERS )
			try:
				fd = urllib2.urlopen(req)
			except urllib2.HTTPError, e:
				raise Exception('HTTP ERROR: %s' %e)
			except urllib2.URLError, e:
				raise Exception('URL ERROR: %s' %e)
			info = fd.info()
			return info

	@classmethod
	def dynamic_wget(self, url):
		'''
		u can use element.get_attribute('innerHTML) to get html
		use case: 
			driver.find_element_by_tag_name('body').get_attribute('innerHTML')
			
		'''
		from selenium import webdriver
		from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
		driver=None
		try:			
			# driver = webdriver.Firefox()
			
			webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.User-Agent']="Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4"
			webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.content-type'] ="Application/JSON"
			driver = webdriver.PhantomJS(executable_path=settings['PHANTOM_JS_PATH']) #/usr/local/bin/phantomjs			
		except Exception, e:
			raise Exception('cannot find phantomjs path, you should provide executable_path for phantomjs')
		else:
			driver.get(url)
			return driver.page_source
			
		driver.quit()

	@classmethod
	def post_website(self, add_crawler_site):

		payload = {'url': add_crawler_site}
		try:
			r = requests.post(HttpConstants.WEBSITE_URL, data=json.dumps(payload), headers=HttpConstants.HEADERS)
		except Exception, e:
			raise Exception('HTTP ERROR: %s' %e)
		else:
			return r.json()

	@classmethod
	def get_websites(self):
		dynamic_urls = None
		urls = None
		try:
			r = requests.get(HttpConstants.WEBSITE_URL, headers=HttpConstants.HEADERS)
		except Exception, e:
			raise Exception('HTTP ERROR: %s' %e)
		else:
			urls = []
			dynamic_urls = []
			for result in r.json()['results']:
				if not result['is_dynamic']:
					urls.append(result['url'])
				else:
					dynamic_urls.append(result['url'])

			return urls, dynamic_urls

	@classmethod
	def push_articles(self):
		
		list_db = Mongodb(settings['MONGODB_ARTICLES_LIST'])
		content_db = Mongodb(settings['MONGODB_ARTICLES_CONTENT'])
		count=0
		for col in list_db.collection.find({"isContentDownload":True}):
			url = col['url']
			title = col['title']
			author = col['author'].strip()
			abstracts = col['abstract']
			created = col['created'].strip()
			updated = created
			content, imgs = Webservice.parse_content(url)
			payload = {
				"title":title,
				"author":author,
				"abstracts":abstracts,
				"content":content,
				"category":1,
				"tags":["头条"],
				"imgs":[],
				"created":created,
				"updated":updated
			}
			count = count+1
			print count
			failed_times = 0
		
			while True:
				try:
					r = requests.post(HttpConstants.ARTICLE_PUSH_URL, data=json.dumps(payload), headers=HttpConstants.HEADERS)
					if r.status_code==201:
						print r.json()
						break
					print r.json()
					failed_times = failed_times + 1
					import time
					print 'request failed %d times'  %failed_times
					if failed_times == 5:
						break
					print 'took longer than 3 seconds...'
					time.sleep(3)
				except Exception, e:
					raise Exception('HTTP ERROR: %s' %e)

	@classmethod
	def parse_content(self, url):
		db = Mongodb(settings['MONGODB_ARTICLES_CONTENT'])
		mycontent =''
		imgs=[]
		for col in db.collection.find({"url":url}):
			source = col['source']
			
			page = etree.HTML(source)
			ltr = page.xpath('//div[@id="css-entry"]')[0]
			syn_bar = page.xpath('//div[@id="syn-bar"]')[0]
			other = page.xpath('//div[@id="css-widget-related-other-resources"]')[0]
			syn_bar_str = etree.tostring(syn_bar)
			other_str = etree.tostring(other)
			mycontent = etree.tostring(ltr)
			mycontent = mycontent.replace(syn_bar_str, '').replace(other_str, '')
		imgs_count = 0
		mc = etree.HTML(mycontent)
		for img in mc.xpath('//img'):
			imgs.append(img.attrib['src'])
		return mycontent.strip(), imgs


if __name__ == '__main__':
	Webservice.push_articles()
	
	



















