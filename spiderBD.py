#coding:utf-8
import urllib2
import re

class BDTB:
	baseUrl = 'http://tieba.baidu.com/p/4896490947/?see_lz=&pn='
	def getPage(self,pageNum):
		try:
			url = self.baseUrl+str(pageNum)
			request = urllib2.Request(url)
			response = urllib2.urlopen(request).read()
			#print response
			return response
		except Exception,e:
			print e
	def Title(self,pageNum):
		html = self.getPage(pageNum)
		reg = re.compile(r'<title>(.*?)')
		items = reg.findall(reg,html)

		for item in items:
			print item
			f = open('test.txt','w')
			f.write('标题'+'\t'+item)
			f.close()
		return items
		print items
	def Text(self,pageNum):
		html = self.getPage(pageNum)
		reg = re.compile(r'class="d_post_content j_d_post_content ">(.*?)</div><br>',re.S)
		req = re.findall(reg,html)
		if pageNum == 1:
			req = req[2:]
		for i in req:
			removeAddr = re.compile('<a.*?>|</a>')
			removeaddr = re.compile('<img.*?>')
			removeadd = re.compile('http.*?.html')
			i = re.sub(removeAddr,"",i)
			i = re.sub(removeaddr,"",i)
			i = re.sub(removeadd,"",i)
			i = i.replace('<br>','')
			print i
			f = open('test.txt','a')
			f.write('\n\n'+i)
			f.close()
dbtb = BDTB()
print 'spider is doing'
try:
	for i in range(1,5):
		print 'Doing spider %s page' %(i)
		dbtb.Title(i)
		dbtb.Text(i)
except Exception,e:
	print e




