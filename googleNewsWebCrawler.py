# -*- coding: utf-8 -*-

# @author =__Uluç Furkan Vardar__

import requests
from bs4 import BeautifulSoup
#needed lib imported

def googleNewsCrawler():
	#url of the page
	url='https://news.google.com/news/headlines?ned=tr_tr&hl=tr&gl=TR'
	#---getting source code of all page and creatin of firs BeautifulSoup object
	source_code=requests.get(url)
	plain_text=source_code.text
	sourceSoup=BeautifulSoup(plain_text, "html.parser")
	#---
	#---step by step into to 'En çok okunan haberler headers, urls, minutes and sources'
	for innerSoup1 in sourceSoup.find_all('div', {'class': 'WyeMbd'}):
		innerSoup1Source = BeautifulSoup(str(innerSoup1), "html.parser")
		for innerSoup2 in innerSoup1Source.find_all('c-wiz', {'jsrenderer': 'Jzy2fd'}):
		    label=(innerSoup2.get('data-label'))
		    innerSoup2Source=BeautifulSoup(str(innerSoup2), "html.parser")
		    for innerSoup3 in innerSoup2Source.find_all('div',{'class':'deQdld'}):
				innerSoup3Source = BeautifulSoup(str(innerSoup3), "html.parser")
				for innerSoup4 in innerSoup3Source.find_all('c-wiz',{'class':'M1Uqc kWyHVd'}):
					innerSoup4Source = BeautifulSoup(str(innerSoup4), "html.parser")
					for innerSoup5 in innerSoup4Source.find_all('a',{'class':'nuEeue hzdq5d ME7ew'}):
						print "\nYeni haber"
						print "baslik ",label
						print(innerSoup5.string)
						print innerSoup5.get('href')
						print "kaynak,",
						for innerSoup6 in innerSoup4.find_all('span',{'class':'IH8C7b Pc0Wt'}):
							print innerSoup6.string
						print "paylaşılma zamanı, ",
						for innerSoup7 in innerSoup4.find_all('span',{'class':'d5kXP YBZVLb'}):
							print innerSoup7.string
	#---step by step into to Tags
	print "\n\ntagler*"
	for innerTag1 in sourceSoup.find_all('div', {'class':'QWD7rd JHzJp'}):
		innerTag1Source=BeautifulSoup(str(innerTag1),"html.parser")
		for innerTag2 in innerTag1Source.find_all('c-wiz', {'jsdata': 'deferred-i7'}):
			innerTag2Source=BeautifulSoup(str(innerTag2), "html.parser")
			for innerTag3 in innerTag2Source.find_all('div', {'class': 'Q3vG6d kzAuJ'}):
				print innerTag3.string
	#---
googleNewsCrawler()




