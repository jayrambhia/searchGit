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

def getRepoLinks(soup):
	repo_links=[]
	links = soup.findAll('h3')
	for link in links:
		link_contents = link.contents
		for link_content in link_contents:
			if isinstance(link_content, unicode):
				continue
			if link_content.has_key('href'):
				repo_links.append(link_content['href'])
	return repo_links

def main():
	saveRepo.setProxy()
	link = 'https://github.com/jayrambhia'
	#link = raw_input('Github user link: ')
	page = urllib2.urlopen(link)	
	soup = BeautifulSoup(page.read())
	
	repo_links = getRepoLinks(soup)
	
	for repo_link in repo_links:
		repo_link = 'https://github.com'+repo_link
		
		saveRepo.setLink(repo_link)
		print 'Repo Saved'
	return
	
if __name__ == '__main__':
	main()
