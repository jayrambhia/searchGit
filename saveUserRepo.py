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
