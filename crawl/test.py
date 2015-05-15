from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import urllib2
from io import StringIO, BytesIO
class WebSpider(object):
	"""docstring for WebSpider"""
	def download(self,url):
		user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
		hearder = {"User_Agent" : user_agent}
		request = urllib2.Request(url = url , headers = hearder)
		response = None

		try:
			response = urllib2.urlopen(request)
		except urllib2.HTTPError, e:
			print "HTTPError"
		except urllib2.URLError, e:
			print "URLError"
		except Exception, e:
			print "Exception"
		finally:
			print "WebSpider finished"
			print "-------------------------------"
		
		data = response.read()
		return data
		# return StringIO(data.decode("utf-8"))

class MyHtmlParser(HTMLParser):
	"""docstring for MyHtmlParser"""
	def handle_starttag(self, tag, attrs):
		# if attrs.get('class') != None:
		# 	print attrs['class']
		# print "Start tag:", tag
		if tag == 'div':
			print "tag:", tag ,attrs
			for attr in attrs:
				# print "		attr:", attr
				if attr[0] == 'class':
					print attr[1]
					if attr[1] == 'entryContainer':
						print '-------------------------------------------------------------------------',attr
			# print "		attr:", attr[0]

	# def handle_endtag(self, tag):
	# 	print "End tag  :", tag

	# def handle_data(self, data):
	# 	print "Data 	:", data

	# def handle_comment(self, data):
	# 	print "Comment  :", data

	# def handle_entityref(self, name):
	# 	c = unichr(name2codepoint[name])
	# 	print "Name end:", c

	# def handle_charref(self, name):
	# 	print 'yes'
	# 	# c = ''
	# 	# if name.startswith('x'):
	# 	# 	c = unichr(int(name[1:], 16))
	# 	# else:
	# 	# 	c = unichr(int(name))
	# 	# print "Num ent  :", c

	# def handle_decl(self, data):
	# 	print "Decl 	:", data

# webspider = WebSpider()
# data = webspider.download("https://www.analyticszone.com/homepage/web/displayBlogsPage.action#")
# if data:
# 	parser = MyHtmlParser()
# 	parser.feed(data)
		
		
class MyHtmlParser1(HTMLParser):
	"""docstring for MyHtmlParser"""
	def __init__(self):
		HTMLParser.__init__(self)
		self.flag = 0
		self.title = ""
		self.href = ""
	def handle_starttag(self, tag, attrs):
		# print "Encountered a start tag:", tag
		if tag == 'div':
			if len(attrs) == 0:
				pass
			else:
				for attr in attrs:
					if attr[0] == "class":
						if attr[1] == "entryContainer":
							print attr
							self.flag = 1
		if self.flag == 1 and tag == 'a':
			if len(attrs) == 0:
				pass
			else:
				for attr in attrs:
					if attr[0] == "href":
						print attr[1]
						self.href = attr[1]
	# def handle_endtag(self,tag):
	# 	print "Encountered an end tag :", tag
	def handle_data(self, data):
		if self.flag == 1:
			self.title = data
			print "Encountered some data :", data
			self.flag = 0

# f = open('hhh.html','r')
# html = f.read()

webspider = WebSpider()
html = webspider.download("https://www.analyticszone.com/homepage/web/displayBlogsPage.action#")

print html
# data = "<div class='aaa'>123</div><div class='aaa'>234</div><div class='aaa'>345</div>"
parser = MyHtmlParser1()
parser.feed(html)