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
from searchGitUtils import getunicode, getPrintUnicode, makeDir, setProxy
import os

def saveText(soup):
	data_path = soup.find('div',{'class':True,'data-path':True})['data-path']
	title = soup.find('title')
	title = getunicode(title).split()[-3]
	data_path = os.path.join(os.getcwd(),title,data_path)
	path, filename = os.path.split(os.path.split(data_path)[0])
	makeDir(path)
	filepath = os.path.join(path, filename)
	f = open(filepath,'w')
	lines = soup.findAll('div',{'class':'line'})
	for line in lines:
		f.writelines(getPrintUnicode(line)+'\n')
	f.close()
	print filepath, 'saved'
	return	

def checkURL(url):
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page.read())
	div = soup.findAll('div')

	if soup.find('div',{'class':'highlight'}):
		saveText(soup)
		#print 'file saved'
	else:
		accessURL(getAllURLs(soup))
	return			

def getAllURLs(soup):
	td_list=[]
	url_list=[]
	td_list = soup.findAll('td',{'class':'content'})
	for tds in td_list:
		url_list.append(tds.contents[1]['href'])
	
	return url_list

def accessURL(url_list):
	for url in url_list:
		url = 'https://github.com'+url
		checkURL(url)
	return	

def mainRepoURL(url):
	try:
		page = urllib2.urlopen(url)
	except urllib2.HTTPError:
		print 'URL not found'
		return
	soup = BeautifulSoup(page.read())
	accessURL(getAllURLs(soup))
	return	

def saveRepo(url):
	setProxy()
	if url:
		mainRepoURL(url)
	return
	
def main():
	url = raw_input('GitHub Repo URL: ')
	saveRepo(url)
	
	return

if __name__ == '__main__':
	main()
