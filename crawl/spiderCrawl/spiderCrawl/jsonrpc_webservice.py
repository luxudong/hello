from scrapy.webservice import JsonRpcResource

class StatsResource(JsonRpcResource):
	"""docstring for StatsResource"""

	ws_name = 'stats'

	def __init__(self, crawler):
		JsonRpcResource.__init__(self, crawler, crawler.stats)
