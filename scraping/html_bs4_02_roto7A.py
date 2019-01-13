# -*- coding:utf-8 -*-

import re
import urllib2
from bs4 import BeautifulSoup

opener = urllib2.build_opener()
opener.addheaders=[
    ('User-Agent', "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36"),
    ('Accept-Language','ja,en-us;q=0.7,en;q=0.3')
]
urllib2.install_opener(opener)

url = "http://www.mizuhobank.co.jp/takarakuji/loto/loto7/index.html"
soup = BeautifulSoup(urllib2.urlopen(url).read())

#回数
table = soup.findAll("table")[0]
regex = u'第(.*?)回'
kuji_id = re.search(regex, unicode(table)).group(1)

print u"回数：" + kuji_id
