import scrapy
from tutorial.items import DmozItem
class DmozSpider(scrapy.Spider):
	"""docstring for DmozSpider"""
	name = "dmoz"
	allowed_domains = ["dmoz.org"]
	start_urls = [
		"http://www.ibmbigdatahub.com/blogs"
	]

	def parse(self, response):
		# filename = response.url.split("/")[-2]
		# for sel in response.xpath('//ul/li'):
		# 	item = DmozItem()
		# 	item['title'] = sel.xpath('a/text()').extract()
		# 	item['link'] = sel.xpath('a/@href').extract()
		# 	item['desc'] = sel.xpath('text()').extract()
		# 	yield item
			# title = sel.xpath('a/text()').extract()
			# link = sel.xpath('a/@href').extract()
			# desc = sel.xpath('text()').extract()
			# print title, link, desc
			
			# with open(filename, 'wb') as f:
			# 	f.write(title[0])
		filename = response.url.split("/")[-1]
		with open(filename, 'wb') as f:
			f.write(response.body)