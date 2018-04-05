# -*- coding: utf-8 -*- 
import re  
import urllib,urllib2
import HTMLParser

agent = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'}

def unescape(text):
    parser = HTMLParser.HTMLParser()
    return (parser.unescape(text))

def TranslateByGoogle(text, fromLang="auto", toLang="zh-CN"):
    base_link = "http://translate.google.cn/m?hl=%s&sl=%s&q=%s"
    text = urllib.quote_plus(str(text))
    link = base_link % (toLang, fromLang, text)
    request = urllib2.Request(link, headers=agent)
    try:
        raw_data = urllib2.urlopen(request).read()
        data = raw_data.decode("utf-8")
        expr = r'class="t0">(.*?)<'
        re_result = re.findall(expr, data)
        if (len(re_result) == 0):
            result = ""
        else:
            result = unescape(re_result[0])
        return (result)
    except Exception, e:
        print e