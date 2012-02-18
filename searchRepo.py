'''
Author : Jay Rambhia
email : jayrambhia777@gmail.com
Git : https://github.com/jayrambhia
gist : https://gist.github.com/jayrambhia
=============================================
Name : searchRepo
Repo : searchGit
Git : https://github.com/jayrambhia/searchGit
version 0.1
'''
#            Copyright (c) 2012 Jay Rambhia

# Permission is hereby granted, free of charge, to any person obtaining 
# a copy of this software and associated documentation files (the "Software"), 
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the 
# Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included 
# in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY 
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from BeautifulSoup import BeautifulSoup
import urllib2
from getUnicode import getunicode
from searchGitUtils import setProxy, getunicode, getSoup, getPage, getPageNumber
def getRepo(result):
	repo_author = ''
	repo_url = ''
	repo_language = ''
	repo_des=''
	repo_detail = ''

	title = result.find('',{'class':'title'})
	repo_url = title.find('a',{'href':True})['href']
	repo_author = getunicode(title.find('a',{'href':True}))
	repo_language = getunicode(result.find('span',{'class':'language'}))
	repo_des = getunicode(result.find('div',{'class':'description'}))
	repo_detail = getunicode(result.find('div',{'class':'details'}))
	repo_detail_dict = {'author':repo_author, 'url':repo_url, 'language':repo_language,'description':repo_des,'detail':repo_detail}
	return repo_detail_dict

def getURL(language, query, pg_no):
	base_url = 'https://github.com/search?'
	type_url = 'type=Repositories'
	lang_url = 'language='+language
	query_url = 'q='+'+'.join(query.split())
	end_url = 'repo=&langOverride=&x=0&y=0&start_value='+str(pg_no)
	
	url = '&'.join([type_url, lang_url, query_url, end_url])
	URL = base_url+url

	return URL

def searchResults(soup, repo_dict={}, search_count=0):
	result = soup.findAll('div',id='code_search_results')
	if result:
		repo_url=''
		result_list = soup.findAll('div',{'class':'result'})
		for result in result_list:
					repo_detail_dict = getRepo(result)
					search_count+=1
					repo_dict[search_count] = repo_detail_dict
	return (repo_dict, search_count)

def searchPage(pg_no, query, language):
	URL = getURL(language,query,pg_no)
	#print URL
	page = getPage(URL)
	soup = getSoup(page)
	return soup

def repoReader(repo_dict):
	for i in range(1,len(repo_dict.keys())+1):
		print 'Repository:',i
		print 'Author:',repo_dict[i]['author']
		print 'URL:','https://github.com'+repo_dict[i]['url']
		print 'language:',repo_dict[i]['language']
		print 'Description:',' '.join(repo_dict[i]['description'].split())
		print 'Details:',' '.join(repo_dict[i]['detail'].split())
		print ''

def searchRepo(query, language):
	setProxy()
	if language:
		language = language.capitalize()
	
	pg_no = 0
	search_count = 0
	repo_dict={}

	while True:
		pg_no = getPageNumber(pg_no)
		soup = searchPage(pg_no, query, language)
		repo_dict, search_count_new = searchResults(soup, repo_dict, search_count)
		if search_count_new == search_count:
			break
		search_count = search_count_new
	repoReader(repo_dict)
	return repo_dict
					
def main():
	query = raw_input('query: ')
	language = raw_input('Language: ')
	repo_dict = searchRepo(query, language)
								
if __name__ == '__main__':
	main()						
