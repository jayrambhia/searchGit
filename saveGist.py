'''
Author : Jay Rambhia
email : jayrambhia777@gmail.com
Git : https://github.com/jayrambhia
gist : https://gist.github.com/jayrambhia
=============================================
Name : saveGist
Repo : searchGit
Git : https://github.com/jayrambhia/searchGit
version 0.1
'''
from BeautifulSoup import BeautifulSoup
import urllib2
from getUnicode import getunicode, getPrintUnicode
import os


def saveGist(soup):
	div = soup.findAll('div')
	
	for d in div:
		if d.has_key('class'):
			if d['class'] == 'path':
				gistnum = getunicode(d).split()[-1]
	
	spans = soup.findAll('span')			
	for span in spans:
		if span.has_key('class'):
			if span['class'] == 'code':
				filename = getunicode(span).split()[0]
	filename = '_'.join([gistnum,filename])		
	f = open(filename,'w')
	
	for d in div:
		if d.has_key('class'):
			if d['class'] == 'line':
				f.writelines(getPrintUnicode(d)+'\n')	
	f.close()
	return		
	
def getSoup(url):
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page.read())
	return soup

def setProxy():
	proxy = {'http':'http://username:password@proxy:port',
					'https':'https://username:password@proxy:port'}
	Proxy = urllib2.ProxyHandler(proxy)
	opener = urllib2.build_opener(Proxy)
	urllib2.install_opener(opener)
	
def getgist(url):
	setProxy()
	soup = getSoup(url)
	saveGist(soup)	
	
def main():
	setProxy()
	url = raw_input('gist URL: ')
	getgist(url)
	
	return

if __name__ == '__main__':
	main()
