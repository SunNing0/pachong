
# encoding:utf-8 
import urllib
import urllib2
import re
import json

url = 'http://www.cnblogs.com/allenblogs/archive/2010/09/13/1824842.html'
user_agent = 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
headers = {'User-Agent':user_agent}
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    #print content
    pattern = re.compile('<title>(.*?)</title>',re.S)
    items = re.findall(pattern,content)
 #   print type(items)
    print json.dumps(items,encoding="UTF-8",ensure_ascii=False)
    for item in items:
        print item[0]  
except urllib2.URLError,e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
