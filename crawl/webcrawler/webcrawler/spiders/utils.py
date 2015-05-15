import hashlib

from db import RedisFactory, Mongodb
from scrapy.conf import settings


class Utils:

	@classmethod
	def get_md5(self,string):
		md5_str = hashlib.md5()
		md5_str.update(string)
		md5_digest = md5_str.hexdigest()
		return md5_digest

	@classmethod
	def init_redis(self):
		db = RedisFactory()
		mongo = Mongodb(settings['MONGODB_ARTICLES_LIST_URL_MD5'])

		for col in mongo.collection.find():
			url = col['url']
			md5 = col['md5']
			db.set(url, md5)

	

