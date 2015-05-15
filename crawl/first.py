import urllib2
import urllib
import cookielib
from lxml import etree
from lxml.html import fromstring
from io import StringIO, BytesIO
import lxml.html.soupparser
url = "https://www.analyticszone.com/homepage/web/displayBlogsPage.action#"
# url = "http://m.qiushibaike.com/hot/page/"
# url = "http://bbs.csdn.net/callmewhy"
user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
header = {'User_Agent' : user_agent}
req = urllib2.Request(url=url, headers = header)
# req.add_header("Connection", "keep-alive")
# req.add_header("Pragma", "no-cache")
# req.add_header("Cache-Control", "no-cache")
# req.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
# req.add_header("Accept-Encoding", "gzip, deflate, sdch")
# req.add_header("Accept-Language", "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4")
# req.add_header("Cookie", "bdshare_firstime=1420341919215; _qqq_uuid_=055579e1c53b3b7b4ad88409f3e5fbed3b82ff28; __utma=210674965.1309533783.1420338153.1420359626.1420425750.4; __utmc=210674965; __utmz=210674965.1420338153.1.1.utmcsr=blog.csdn.net|utmccn=(referral)|utmcmd=referral|utmcct=/pleasecallmewhy/article/details/8932310; Hm_lvt_2670efbdd59c7e3ed3749b458cafaa37=1420338153,1420338598,1420341919,1420425729; Hm_lpvt_2670efbdd59c7e3ed3749b458cafaa37=1420438326")

# req.add_header('User_Agent' , user_agent)
#print header
# mycookie = urllib2.HTTPCookieProcessor(cookielib.CookieJar())
# openner = urllib2.build_opener(mycookie)
# print req.headers
response = None
try:
	
	response = urllib2.urlopen(req)

except urllib2.HTTPError , e:
	print "hello123213",e.code
except urllib2.URLError , e:
	print "urlerror" , e.reason
except Exception , e:
	print 'Exception' , e
if response:
	html = response.read()
	# print html

	# print html
	# html = "<div class=\"ssdf\" id = \"231748\">haode</div>"	

	# dom = etree.fromstring(html)
	# print dom[0].tag

	dom = soupparser.fromstring(StringIO(html.decode("utf-8")))
	print len(dom)

	parser = etree.HTMLParser()
	tree = etree.parse(StringIO(html.decode("utf-8")),parser)
	result = etree.tostring(tree.getroot(),pretty_print=True,method="html")
	r = tree.xpath("//div")
	for tmp in r:
		print tmp.attrib
		# if tmp.attrib['class'] == "entryContainer":
		# 	print tmp.attrib['class']
		# else:
		# 	print tmp.attrib['class']
		# print tmp.attrib
		# if tmp.attrib['class'] , "entryContainer"):
		# 	print tmp.text
	

	#print result
	# page = etree.HTML(html.lower().decode('utf-8'))	
	# hrefs = page.xpath(u"//div")
	# for href in hrefs:
	# 	if href:
	# 		print href.attrib


			
	# print html
	# html = html.decode("utf-8")
	# print (html)
	# parser = etree.HTMLParser()
	# tree = etree.parse(StringIO(html),parser)
	# result = etree.tostring(tree.getroot(),pretty_print=True,method="html")
	# print (result)
	# print "result",result
	# print "url:",response.geturl()
	# print "info:",response.info()
	# print "code:",response.getcode()
	# print "len:",len(response.read())
	# astr = urllib.quote('this is "k"')
	# print astr
	# print urllib.unquote(astr)
	# bstr = urllib.quote_plus('this is "k"')
	# print bstr
	# print urllib.unquote_plus(bstr)

	# params = {"a":"1" , "b":"2"}
	# print urllib.urlencode(params)

	# l2u = urllib.pathname2url(r'd:\a\test.py')
	# print l2u
	# print urllib.url2pathname(l2u)
