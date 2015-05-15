# -*- coding: utf-8 -*-

# Scrapy settings for webcrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'webcrawler'

SPIDER_MODULES = ['webcrawler.spiders']
NEWSPIDER_MODULE = 'webcrawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'webcrawler (+http://www.yourdomain.com)'

MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27017
MONGODB_DB = 'crawler'
MONGODB_CRAWLER_SITE = 'website'
MONGODB_ARTICLES_LIST = 'articles_list'
MONGODB_ARTICLES_CONTENT = 'articles_content'
MONGODB_ARTICLES_SITE = 'articles_site'
MONGODB_ARTICLES_LIST_URL_MD5 = 'articles_list_url_md5'
MONGODB_SAFE = True


# Enables scheduling storing requests queue in redis.
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# Don't cleanup redis queues, allows to pause/resume crawls.
SCHEDULER_PERSIST = True

# Schedule requests using a priority queue. (default)
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'

# Schedule requests using a queue (FIFO).
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderQueue'

# Schedule requests using a stack (LIFO).
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderStack'

# Max idle time to prevent the spider from being closed when distributed crawling.
# This only works if queue class is SpiderQueue or SpiderStack,
# and may also block the same time when your spider start at the first time (because the queue is empty).
SCHEDULER_IDLE_BEFORE_CLOSE = 10

# # Store scraped item in redis for post-processing.
# ITEM_PIPELINES = [
#     'scrapy_redis.pipelines.RedisPipeline',

# ]
ITEM_PIPELINES = {
	'webcrawler.pipelines.ArticleContentPipeline': 300,

}

# Specify the host and port to use when connecting to Redis (optional).
REDIS_HOST = 'localhost'
REDIS_PORT = 6379

REDIS_QUEUE ='list_url_queue'
REDIS_MAP ='url_md5_map'
REDIS_NEW_QUEUE='list_new_url'

# PHANTOM_JS_PATH='/usr/local/bin/phantomjs'
PHANTOM_JS_PATH='C:\\lxdprogram\\phantomjs\\phantomjs.exe'
# Specify the full Redis URL for connecting (optional).
# If set, this takes precedence over the REDIS_HOST and REDIS_PORT settings.
REDIS_URL = 'redis://localhost:6379'








