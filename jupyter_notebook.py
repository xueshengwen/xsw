import pymongo
import charts
import datetime


client = pymongo.MongoClient('localhost',27017)
tieba = client['tieba']  
time_list = tieba['time_list'] 

index_time = []
count_time = []

start_day = datetime.date(2017,6,30)
end_day = datetime.date(2017,7,6)
days = datetime.timedelta(days=1)

while start_day <= end_day:
	index_time.append(start_day.strftime('%Y-%m-%d'))
	start_day += days
for date in index_time:
	a = list(time_list.find({'date':date}))
	count_time.append(len(a))
#
#线形图	
#options = {
#	'title':{'text':'百度发帖量统计'}，
#	'xAxis':{'categories':index_time},
#	'yAxis':{'text':'数量'}
#}	
#series = [{'date':count_time,'name':'python贴吧分析','type':'line'}]
#charts.plot(series,show='inline',options=options)


#柱状图
tem_list = []
for i,j in zip(count_time,index_time):
	date={
		'name':j,
		'date':[i],
		'type':'column'		
	}
	tem_list.append(date)
options = {
	'title':{'text':'百度发帖量统计'},
	'subtitle':{'text':'可视化统计表'}
	'plotOptions':{'column':{'dataLabels':{'enabled':True}}}
}	
charts.plot(tem_list,show='inline',options=options)