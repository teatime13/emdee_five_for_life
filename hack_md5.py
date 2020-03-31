#!/usr/local/bin/python2.7
# coding: UTF-8

# 「Emdee five for life」
# 文字列が与えられるのでそれをmd5にして送信する

import md5 
import requests
import urllib2
from bs4 import BeautifulSoup

url = "http://docker.hackthebox.eu:31479/"
r = requests.session()

html = urllib2.urlopen(url)
soup = BeautifulSoup(html, "html.parser")
h3_tag = soup.h3
given_string = h3_tag.string

print given_string

m = md5.new()
m.update(given_string)

digest = m.hexdigest()

print(digest)


# POST送信
data = {
    'hash':digest,
}

out = r.post(url=url,data=data)

print(out.text)
