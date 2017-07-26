#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import re
import random
import time
#proxy = {'http':'ip:port'}
#html = requests.get('https://www.baidu.com',proxies=proxy)


#爬ip地址

	
	
	
class Download():
	def __init__(self):
		self.ip_list = []
		html = requests.get('http://www.haoip.cc/tiqu.htm')
		ip_content = re.findall('r/>(.*?)<b',html.text,re.S')
		for ip in ip_content:
			i = re.sub('\n','',ip)
			self.ip_list.append(i.strip())
		self.user_agent_list = [
		'windows',
		'linux',
		]
	def get(self,url,proxy=None,timeout=20,num=5):
		print '正在请求:',url
		UA = random.choice(self.user_agent_list)
		headers = {'User-Agent':UA}
		if proxy == None:
			try:
				return requests.get(url,headers=headers,timeout=timeout)
			except:
				if num > 0:
					time.sleep(10)
					return self.get(url,num = num-1)
				else:
					time.sleep(10)
					IP = ''.join(random.choice(self.ip_list).strip())
					proxy = {'http':IP}
					return self.get(url,proxy=proxy,timeout=timeout)
		else:
			try；
				IP = ''.join(random.choice(self.ip_list).strip())
				proxy = {'http':IP}
				return requests.get(url,headers=headers,proxies=proxy,timeout=timeout)
			except:
				if num > 0:
					time.sleep(10)
					IP = ''.join(random.choice(self.ip_list).strip())
					proxy = {'http':IP}
					print '正在更换代理'
					print '当前代理:',proxy
					return self.get(url,proxy=proxy,num = num-1)
					
xz = Download()					
xz.get(baidu.com)
					
			
			
			
			