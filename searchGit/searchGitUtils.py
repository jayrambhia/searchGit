'''
Author : Jay Rambhia
email : jayrambhia777@gmail.com
Git : https://github.com/jayrambhia
gist : https://gist.github.com/jayrambhia
=============================================
Name : searchGitUtils
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

import urllib2
import os
from BeautifulSoup import BeautifulSoup

def setProxy():
	"""
	proxy = {'http':'http://jayrambhia:password@10.1.9.36:8080',
			'https':'https://jayrambhia:password@10.1.9.36:8080'}
			
	or
	
	proxy = {'http':'http://10.1.9.36:8080',
			'http':'https://10.1.9.36:8080',}
	"""
    proxy = {'http':'http://username:password@proxy:port',
                    'https':'https://username:password@proxy:port'}
    Proxy = urllib2.ProxyHandler(proxy)
    opener = urllib2.build_opener(Proxy)
    urllib2.install_opener(opener)
    return opener

def makeDir(path):
    if os.path.isdir(path):
        return
    dir1, dir2 = os.path.split(path)
    makeDir(dir1)
    os.mkdir(path)
    return

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

def getPrintUnicode(soup):
    
    body=''
    if isinstance(soup, unicode):
        soup = soup.replace('&#39;',"'")
        soup = soup.replace('&quot;','"')
        soup = soup.replace('&nbsp;',' ')
        soup = soup.replace('&gt;','>')
        soup = soup.replace('&lt;','<')
        body = body + soup
    else:
        if not soup.contents:
            return ''
        con_list = soup.contents
        for con in con_list:
            body = body + getPrintUnicode(con)
    return body

def getSoup(page):
    soup = BeautifulSoup(page.read())
    return soup
    
def getPage(URL):
    page = urllib2.urlopen(URL)
    return page

def getPageNumber(pagenum=0):
    pagenum += 1
    return pagenum
