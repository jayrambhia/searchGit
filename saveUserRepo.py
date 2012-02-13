'''
Author : Jay Rambhia
email : jayrambhia777@gmail.com
Git : https://github.com/jayrambhia
gist : https://gist.github.com/jayrambhia
=============================================
Name : saveUserRepo
Repo : searchGit
Git : https://github.com/jayrambhia/searchGit
version 0.1
'''
import saveRepo
from BeautifulSoup import BeautifulSoup
import urllib2
from searchGitUtils import setProxy, getPage, getSoup
from saveRepo import saveRepo

def getRepoURLs(soup):
	repo_URLs=[]
	urls = soup.findAll('h3')
	for url in urls:
		link = url.find('a',{'href':True})
		if link:
			repo_URLs.append(link['href'])
	return repo_URLs

def saveUserRepo(url):
	setProxy()
	soup = getSoup(getPage(url))
	repo_url_list = getRepoURLs(soup)
	for repo_url in repo_url_list:
		repo_url = 'https://github.com'+repo_url
		saveRepo(repo_url)
		print 'Repo Saved'
	return
	
def main():
	url = 'https://github.com/jayrambhia'
	#url = raw_input('Github user link: ')
	saveUserRepo(url)
	return
	
if __name__ == '__main__':
	main()
