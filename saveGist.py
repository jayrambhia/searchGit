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
from searchGitUtils import getunicode, getPrintUnicode, setProxy, getSoup, getPage
import os


def saveText(soup):
	gistnum = getunicode(soup.find('div',{'class':'path'})).split()[-1]
	
	span = soup.find('span',{'class':'code'})			
	filename = getunicode(span).split()[0]
	filename = '_'.join([gistnum,filename])		
	
	f = open(filename,'w')
	lines = soup.findAll('div',{'class':'line'})
	for line in lines:
		f.writelines(getPrintUnicode(line)+'\n')	
	f.close()
	return		
	
def saveGist(url):
	setProxy()
	page = getPage(url)
	soup = getSoup(page)
	saveGist(soup)	
	
def main():
	url = raw_input('gist URL: ')
	getgist(url)
	
	return

if __name__ == '__main__':
	main()

