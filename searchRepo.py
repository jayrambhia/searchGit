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
from BeautifulSoup import BeautifulSoup
import urllib2

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

def getRepo(repo_con_list):
#	print repo_con_list
	repo_author = ''
	repo_url = ''
	repo_language = ''
	repo_des=''
	repo_detail = ''
	for repo_con in repo_con_list:
		if isinstance(repo_con, unicode):
			continue
		else:
			if repo_con.has_key('class'):
				if repo_con['class'] == 'title':
					repo_sub_con_list = repo_con.contents
#					print 'repo_sub_con_list',repo_sub_con_list
					for repo_sub_con in repo_sub_con_list:
#						print 'repo_sub_con',repo_sub_con
						if isinstance(repo_sub_con, unicode):
							continue
						else:
							if repo_sub_con.has_key('href'):
								repo_url = repo_sub_con['href']
#								print repo_url
								repo_author = getunicode(repo_sub_con)
#								print repo_author
							elif repo_sub_con.has_key('class'):
								if repo_sub_con['class'] == 'language':
									repo_language = getunicode(repo_sub_con)
#									print repo_language
				elif repo_con['class'] == 'description':
					repo_des = repo_con.contents[0]
#					print repo_des
				elif repo_con['class'] == 'details':
					repo_detail = getunicode(repo_con)
#					print repo_detail
	repo_detail_dict = {'author':repo_author, 'url':repo_url, 'language':repo_language,'description':repo_des,'detail':repo_detail}
	return repo_detail_dict

def getURL(language, query, pg_no):
	base_url = 'https://github.com/search?'
	type_url = 'type=Repositories'
	lang_url = 'language='+language
	query_url = 'q='+'+'.join(query.split())
	end_url = 'repo=&amp;langOverride=&amp;x=0&amp;y=0&amp;start_value='+str(pg_no)

	url = '&amp;'.join([type_url, lang_url, query_url, end_url])
	URL = base_url+url

	return URL

def getSoup(page):
	soup = BeautifulSoup(page.read())
	return soup

def getPage(URL):
	page = urllib2.urlopen(URL)
	return page

def getPageNumber(pagenum=0):
	pagenum += 1
	return pagenum

def searchRepo(soup, repo_dict={}, search_count=0):
	results = soup.findAll('div',id='code_search_results')
	for result in results:
		div_list = result.findAll('div')
		for div in div_list:
			repo_url = ''
			if div.has_key('class'):
				if div['class'] == 'result':
					repo_con_list = div.contents
					repo_detail_dict = getRepo(repo_con_list)
					search_count+=1
					repo_dict[search_count] = repo_detail_dict
	return (repo_dict, search_count)

def doSearch(pg_no, query, language):
	URL = getURL(language,query,pg_no)
	print URL
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
def main():
	proxy = {'http':'http://username:password@proxy:port',
					'https':'https://username:password@proxy:port'}
	Proxy = urllib2.ProxyHandler(proxy)
	opener = urllib2.build_opener(Proxy)
	urllib2.install_opener(opener)

	query = raw_input('query: ')
	language = raw_input('Language: ')

	if language:
		language = language.capitalize()

	pg_no = 0
	search_count = 0
	repo_dict={}

	while True:
		pg_no = getPageNumber(pg_no)
		soup = doSearch(pg_no, query, language)
		repo_dict, search_count_new = searchRepo(soup, repo_dict, search_count)
		if search_count_new == search_count:
			break
		search_count = search_count_new
	#print repo_dict
	repoReader(repo_dict)
	return repo_dict

if __name__ == '__main__':
	main()						
