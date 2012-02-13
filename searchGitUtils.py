'''
Author : Jay Rambhia
email : jayrambhia777@gmail.com
Git : https://github.com/jayrambhia
gist : https://gist.github.com/jayrambhia
=============================================
Name : searchGitUtils
Repo : searchGit
Git : https://github.com/jayrambhia/searchGit
version 0.1
'''
import urllib2
import os
from BeautifulSoup import BeautifulSoup

def setProxy():
	proxy = {'http':'http://username:password@proxy:port',
					'https':'https://username:password@proxy:port'}
	Proxy = urllib2.ProxyHandler(proxy)
	opener = urllib2.build_opener(Proxy)
	urllib2.install_opener(opener)
	
def makeDir(path):
	if os.path.isdir(path):
		return
	dir1, dir2 = os.path.split(path)
	makeDir(dir1)
	os.mkdir(path)
	return

def getunicode(soup):
	body=''
	if isinstance(soup, unicode):
		body = body + soup
	else:
		if not soup.contents:
			return ''
		con_list = soup.contents
		for con in con_list:
			body = body + getunicode(con)
	return body

def getPrintUnicode(soup):
	
	body=''
	if isinstance(soup, unicode):
		soup = soup.replace('&#39;',"'")
		soup = soup.replace('&quot;','"')
		soup = soup.replace('&nbsp;',' ')
		body = body + soup
	else:
		if not soup.contents:
			return ''
		con_list = soup.contents
		for con in con_list:
			body = body + getPrintUnicode(con)
	return body

def getSoup(page):
	soup = BeautifulSoup(page.read())
	return soup
	
def getPage(URL):
	page = urllib2.urlopen(URL)
	return page

def getPageNumber(pagenum=0):
	pagenum += 1
	return pagenum
