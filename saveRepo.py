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

def saveimg(soup):
    title = soup.find('title')
    title = getunicode(title).split()[-3]
    div = soup.find("div",{"class":"breadcrumb","data-path":True})
    data_path = div['data-path']
    data_path = os.path.join(os.getcwd(),title,data_path)
    path, filename = os.path.split(os.path.split(data_path)[0])
    makeDir(path)
    filepath = os.path.join(path, filename)
    print filepath,"saved"
    f = open(filepath,"wb")
    
    img = soup.find("div",{"class":"image"})
    url = img.find("img")["src"]
    url = "".join(["https://github.com",url])
    
    page = opener.open(url)
    f.write(page.read())
    f.close()

def checkURL(url):
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read())
    div = soup.findAll('div')

    if soup.find('div',{'class':'highlight'}):
        saveText(soup)
        #print 'file saved'
    elif soup.find("div",{"class":"image"}):
        saveimg(soup)
        
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
    global opener
    opener = urllib2.build_opener()
    urllib2.install_opener(opener)
    opener = setProxy()
    if url:
        mainRepoURL(url)
    return
    
def main():
    url = raw_input('GitHub Repo URL: ')
    saveRepo(url)
    
    return

if __name__ == '__main__':
    main()
