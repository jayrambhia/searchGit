'''
Author : Jay Rambhia
email : jayrambhia777@gmail.com
Git : https://github.com/jayrambhia
gist : https://gist.github.com/jayrambhia
=============================================
Name : getUnicode
Repo : searchGit
Git : https://github.com/jayrambhia/searchGit
version 0.1
'''
from BeautifulSoup import BeautifulSoup

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
		#print soup
		soup = soup.replace('&#39;',"'")
		soup = soup.replace('&quot;','"')
		soup = soup.replace('&nbsp;',' ')
		#print soup
		body = body + soup
	else:
		if not soup.contents:
			return ''
		con_list = soup.contents
		for con in con_list:
			body = body + getPrintUnicode(con)
	return body
