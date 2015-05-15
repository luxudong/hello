# -*- coding: utf-8 -*-
from lxml import etree
from Date import Date
from lxml import etree
from scrapy.conf import settings
from db import Mongodb, RedisFactory, Init
from webcrawler.webclient.webservice import Webservice
from webcrawler.items import ArticleListItem, ArticleSiteItem


def parse(site, website_timstamp, response):
	
	page = etree.HTML(response)
	entries = page.xpath('//div[@class="entryContainer"]')
	articles = []

	for i in xrange(0,len(entries)):
		print i
		_item = ArticleListItem()
		
		title = entries[i].xpath('//div[@id="entry-title"]//h1[@class="entryTitle"]//a')[i].text
		url = entries[i].xpath('//div[@id="entry-title"]//h1[@class="entryTitle"]//a')[i].attrib['href']
		img = entries[i].xpath('//div[@class="entryMeta"]//img')[i]
		headImg = img.attrib['src']
		author_time = entries[i].xpath('//div[@class="entryMeta"]//span')[i].text.split('|')
		author = author_time[0].strip()
		created = author_time[1].strip()
		abstract = entries[i].xpath('//div[@class="blog_description"]')[i].text.strip()
		_item['title']=title
		_item['author']=author
		_item['headImg']=headImg
		_item['abstract']=abstract
		_item['url']=url
		_item['site']=site
		_item['isContentDownload']=False
		_item['created']=created

		articles.append(_item)
		cur = Date.str_to_timestamp(created)

		if website_timstamp >= cur:                   # 比较当前抓取的列表页更帖的时间与上一次该站点最新更帖时间
			print articles
			print '=================================cur',Date.timestamp_to_str(cur),'website_timestamp',Date.timestamp_to_str(website_timstamp)
			return articles
	print '========================================'
	print articles
	print '========================================'
	return articles

def insert_articles_site(response, site):
	'''
	存储站点源码
	'''
	from datetime import datetime
	db = Mongodb(settings['MONGODB_ARTICLES_SITE'])
	articles_site_item = ArticleSiteItem()
	articles_site_item['site'] = site
	articles_site_item['source'] = response      #lxd更改 原来为source
	articles_site_item['updated'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	db.collection.insert(dict(articles_site_item))
	
def main():

	website = Mongodb(settings['MONGODB_CRAWLER_SITE'])

	articles_list = Mongodb(settings['MONGODB_ARTICLES_LIST'])

	url_md5 = Mongodb(settings['MONGODB_ARTICLES_LIST_URL_MD5'])

	cache = RedisFactory()
	init = Init()
	_, dynamic_sites = website.find_sites() 				 # 获取动态站点

	for site in dynamic_sites:
		print site
		response = Webservice.dynamic_wget(site) 			 # 动态站点下载
		insert_articles_site(response, site)				 # 存储该站点源码
		website_timestamp = website.get_site_timestamp(site) # 站点更新时间
		print 'website_timestamp',Date.timestamp_to_str(website_timestamp)
		articles = parse(site, website_timestamp, response)	 # 分析站点数据
		website.update_website(site, articles[0]['created']) 	 # 更新最新的更贴时间  lxd更改为【‘created’】
		print '-----------------------------------------------'
		print articles
		for _article in articles:
			if not cache.hexist(settings['REDIS_MAP'], _article['url']):
				print _article
				articles_list.collection.insert(dict(_article))   # 存储文章列表页信息
				print cache.hset(settings['REDIS_MAP'], _article['url'], init.get_md5(_article['url']))

# def main():
# 	print 'start'
# 	response = Webservice.dynamic_wget('http://www.ibmbigdatahub.com/blog/our-omni-channel-world')
# 	print 'end'
# 	f = file('response.txt','w')
# 	f.write(response)

if __name__ == '__main__':
	main()
	





