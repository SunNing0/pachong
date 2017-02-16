
# coding:utf8 
import urllib
import urllib2
import re
import json
import sys

reload(sys)
sys.setdefaultencoding('utf8')
url = 'http://www.cnblogs.com/allenblogs/archive/2010/09/13/1824842.html'
#此网址仅供学习爬虫技术使用，并无恶意。如果博主有所介意，麻烦通过github告知本人，本人立即删除，谢谢
user_agent = 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
headers = {'User-Agent':user_agent}
htmlfile = open('html.txt','w')
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    htmlfile.write(content)
    htmlfile.close()
    print content
    pattern = re.compile('<div class="feedbackItem">',re.S)

    #pattern = re.compile('<div.*?feedbackManage">.*?<a.*?>(.*?)</a>.*?<span.*?comment_date">(.*?)</span>',re.S)
    items = re.findall(pattern,content)
 #   print type(items)
#    print json.dumps(items,encoding="UTF-8",ensure_ascii=False)
    for item in items:
        print item[0],item[1],item[2]  
except urllib2.URLError,e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
