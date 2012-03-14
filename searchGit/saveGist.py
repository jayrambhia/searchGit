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
    saveText(soup)  
    
def main():
    url = raw_input('gist URL: ')
    saveGist(url)
    
    return

if __name__ == '__main__':
    main()

