'''
Author : Jay Rambhia
email : jayrambhia777@gmail.com
Git : https://github.com/jayrambhia
gist : https://gist.github.com/jayrambhia
=============================================
Name : saveRepo
Repo : searchGit
Git : https://github.com/jayrambhia/searchGit
version 0.1
'''
from BeautifulSoup import BeautifulSoup
import urllib2
from getUnicode import getunicode, getPrintUnicode
import os

def saverepo(soup):
	div = soup.findAll('div')
	for d in div:
		if d.has_key('class'):
			if d.has_key('data-path'):
				data_path = d['data-path']
				break
	title = soup.find('title')
	title = getunicode(title).split()[-3]
	data_path = os.path.join(os.getcwd(),title,data_path)
	path, filename = os.path.split(os.path.split(data_path)[0])
	
	makeDir(path)
	
	filepath = os.path.join(path, filename)
	f = open(filepath,'w')
	for d in div:
		if d.has_key('class'):
			if d['class'] == 'line':
				f.writelines(getPrintUnicode(d)+'\n')
	f.close()
	return	

def checkLink(link):
	page = urllib2.urlopen(link)
	soup = BeautifulSoup(page.read())
	div = soup.findAll('div')
	repo_flag = 0
	for d in div:
		if d.has_key('class'):
			if d['class'] == 'highlight':
				repo_flag = 1
#				print 'Repo'
				break
	if repo_flag:
		saverepo(soup)
	else:
		accessLinks(getAllLinks(soup))
	return			

def getAllLinks(soup):
	td = soup.findAll('td')
	td_list=[]
	for t in td:
		if t.has_key('class'):
			if t['class'] == 'content':
				td_list.append(t)
	link_list=[]
	for tds in td_list:
		link_list.append(tds.contents[1]['href'])
	
	return link_list

def accessLinks(link_list):
	for link in link_list:
		link = 'https://github.com'+link
		checkLink(link)
	return	
	
def makeDir(path):
	if os.path.isdir(path):
		return
	dir1, dir2 = os.path.split(path)
	makeDir(dir1)
	os.mkdir(path)
	return

def mainRepoLink(link):
	page = urllib2.urlopen(link)
	soup = BeautifulSoup(page.read())
	accessLinks(getAllLinks(soup))
	return	


def setProxy():
	proxy = {'http':'http://username:password@proxy:port',
					'https':'https://username:password@proxy:port'}
	Proxy = urllib2.ProxyHandler(proxy)
	opener = urllib2.build_opener(Proxy)
	urllib2.install_opener(opener)

def setLink(link):
	#setProxy()
	if link:
		mainRepoLink(link)
	return
	
def main():
	setProxy()
	link = raw_input('GitHub Repo Link: ')
	setLink(link)
	
	return

if __name__ == '__main__':
	main()
