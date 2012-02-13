'''
Author : Jay Rambhia
email : jayrambhia777@gmail.com
Git : https://github.com/jayrambhia
gist : https://gist.github.com/jayrambhia
=============================================
Name : searchGist
Repo : searchGit
Git : https://github.com/jayrambhia/searchGit
version 0.1
'''
from BeautifulSoup import BeautifulSoup
import urllib2
from searchGitUtils import getunicode, setProxy, getSoup, getPage, getPageNumber

def getURL(query, pg_no):
	base_url = 'https://gist.github.com/gists/search?'
	query_url = 'q='+'+'.join(query.split())
	end_url = 'page='+str(pg_no)
	
	url = '&'.join([query_url, end_url])
	URL = base_url+url
	return URL
	
def doSearch(pg_no, query):
	URL = getURL(query,pg_no)
	print URL
	page = getPage(URL)
	soup = getSoup(page)
	return soup
	
def searchgists(soup, gist_dict={}, search_count=0):
	gistlist = soup.findAll('div',{'class':'info'})
	if gistlist:
		for gist in gistlist:
			gistlink = gist.find('a',{'href':True})
			if gistlink:
				title = getunicode(gistlink)
				url = gistlink['href']
				print 'https://gist.github.com'+url
				search_count+=1
				gist_dict[search_count] = {'title':title,'url':url}
	return (gist_dict, search_count)

def gistReader(gist_dict):
	for i in range(1,len(gist_dict.keys())+1):
		print 'gist',i
		print 'title:',gist_dict[i]['title']
		print 'url:','https://gist.github.com'+gist_dict[i]['url']

def searchGist(query):
	setProxy()
	pg_no = 0
	search_count = 0
	gist_dict={}

	while True:
		pg_no = getPageNumber(pg_no)
		soup = doSearch(pg_no, query)
		gist_dict, search_count_new = searchgists(soup, gist_dict, search_count)
		if search_count_new == search_count:
			break
		search_count = search_count_new
	
	gistReader(gist_dict)	
	return
	
def main():
	query = raw_input('query: ')
	searchGist(query)
	return
	
if __name__ == '__main__':
	main()
