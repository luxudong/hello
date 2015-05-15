# -*- coding: utf-8 -*-

# Scrapy settings for spiderCrawl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

import os

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

BOT_NAME = 'spiderCrawl'

SPIDER_MODULES = ['spiderCrawl.spiders']
NEWSPIDER_MODULE = 'spiderCrawl.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'spiderCrawl (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
	'spiderCrawl.pipelines.SpidercrawlPipeline':300,
}

USER_AGENT = ''
DOWNLOAD_DELAY = 1
DOWNLOADER_MIDDLEWARES = {
	'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
	'spiderCrawl.rotate_useragent.RotateUserAgentMiddleware':400,
}

WEBSERVICE_ENABLED = True
WEBSERVICE_PORT = [6080,7030]
WEBSERVICE_LOGFILE = 'spiderCrawl.log'
WEBSERVICE_HOST = '127.0.0.1'
WEBSERVICE_RESOURCES = {
	'scrapy.contrib.webservice.enginestatus.EngineStatusResource':None,
	'scrapy.contrib.webservice.stats.StatsResource':None,
	'spiderCrawl.jsonrecource_webservice.EngineStatusResource':1,
	'spiderCrawl.jsonrpc_webservice.StatsResource':1,
}

JSONRPC_ENABLED = True
JSONRPC_LOGFILE = 'jsonrp.log'
JSONRPC_PORT = [6080,7030]
JSONRPC_HOST = '127.0.0.1'