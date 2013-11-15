# coding: utf-8

import urllib2
from bs4 import BeautifulSoup

r=urllib2.urlopen("http://www.theguardian.com/uk").read()

soup = BeautifulSoup(r)

articles = []

block = soup.find_all(id="inner-wrapper")[0]

for i in block.find_all('a',attrs={'class': 'link-text'})[:20]:
    article = {}
    article_html = urllib2.urlopen(i.attrs['href']).read()
    s = BeautifulSoup(article_html)
    article_headline = s.find_all('h1')
    article_body = s.find_all(id="article-body-blocks")
    if len(article_body) and len(article_headline):
        article['body'] = article_body[0].text
        article['headline'] = article_headline[0]
        articles.append(article)
	print article['headline']
        print article['body']

print "Got %d articles" % len(articles)
