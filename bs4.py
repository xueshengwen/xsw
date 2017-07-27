# -*- coding:utf-8 -*-
# pip install jupyter notebook 网页编辑器
import requests
from bs4 import BeautifulSoup
import pymongo


client = pymongo.MongoClient('localhost',27017)
tieba = client['tieba']  #哪个数据库
time_list = tieba['time_list'] #哪个表

start_url = 'https://tieba.baidu.com/p/5182673366?pn={}'
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
}
for i in range(1,5):
	try:
		url = start_url.format(i)
		response = requests.get(url,timeout=20,headers=headers)
	except:
		print 'error'
	soup = BeautifulSoup(response.text,'lxml')
	date = soup.select('div.post-tail-wrap > span:nth-of-type(4)')
	for item in date:
		time_list.insert_one({'date':item.text[:10]})