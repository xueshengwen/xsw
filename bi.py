#!/usr/bin/env python
# -*- conding: utf-8 -*-
from Tkinter import *
from ScrolledText import ScrolledText
import re
import requests
import threading
import sys
import urllib
reload(sys)
sys.setdefaultencoding('utf-8')
url_name = []#url+name
a = 1
def get():
	global a 
	hd = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
	url = 'http://www.budejie.com/' + str(a)
	varl.set('yijinghuoqushipin:%s'%(a))
	html = requests.get(url,headers = hd).text
	a += 1
	url_content = re.compile(r'(<div class="j-r-list-c">.*?</div>.*?</div>)', re.S)
	url_contents = re.findall(url_content,html)
	for i in url_contents:
		url_reg = r'data-mp4="(.*?)">'
		url_items = re.findall(url_reg,i)
		if url_items:
			name_reg = re.compile(r'<a href="/detail-.{8}.html">(.*?)</a>', re.S)
			name_items = re.findall(name_reg,i)

			for i,k in zip(name_items,url_items):
				url_name.append([i,k])
				print i,k
	return url_name
id = 1
def write():
	global id
	while id<10:
		url_name = get()
		for i in url_name:
			urllib.urlretrieve(i[1],'video\\%s.mp4' % (i[0].decode('utf-8').encode('gbk')))
			text.insert(END,str(id)+'.'+i[1]+'\n'+i[0]+'\n')
			url_name.pop(0)
			id += 1
	varl.set('mogutou:shipin,over!')
def start():
	th = threading.Thread(target=write)
	th.start()
			

			
top = Tk()
top.title('baisibudejie')
text = ScrolledText(top,font=('english',10))
text.grid()
button = Button(top,text='start',font=('english',10),command=start)
button.grid()
varl = StringVar()
label = Label(top,font=('english',10),fg='red',textvariable=varl)
label.grid()
varl.set('spider is coming...')
top,mainloop()



