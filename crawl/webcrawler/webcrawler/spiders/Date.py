#!/usr/bin/env python
# -*- coding: utf-8 -*-

#staticmethod can use Date.str_to_timestamp("2015-01-01 00:00:00")
class Date:
	@staticmethod
	def str_to_timestamp(date):
		"""date value example: 2015-01-01 00:00:00"""
		import time
		return int("%d" % time.mktime(time.strptime(date, '%Y-%m-%d %H:%M:%S')))
		
	@staticmethod
	def timestamp_to_str(timestamp):
		"""timestamp value example: 1420041600"""
		import time
		return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(timestamp)))

	@staticmethod
	def get_work_day():
		from datetime import date
		from datetime import timedelta
		now = date.today()
		monday = now - timedelta(days=now.weekday())
		monday = monday.strftime("%Y%m%d")
		friday = now - timedelta(days=now.weekday()-4)
		friday = friday.strftime("%Y%m%d")
		return "%s ~ %s" % (monday, friday)


if __name__ == '__main__':
	import datetime
	s = '2015-01-01 00:00:00'
	d = datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
	
# 	d = s.strip()
# 	print d
# 	print Date.str_to_timestamp(d)