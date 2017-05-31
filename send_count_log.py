#! /usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import datetime
import MySQLdb
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import subprocess
# def send_email(site_name):
#     user = "support@dresspirit.com"
#     pwd = "mingDA1234"#"mBYTE123"
#     recipient = ["xueshengwen@mingdabeta.com", "zhangyachao@mingdabeta.com", "ruanhongyu@mingdabeta.com"]
#
#     subject = site_name + " Debug!"
#     body = "Please fix debug asap!"
#
#     msg = MIMEMultipart('alternative')
#     msg['Subject'] = subject
#     msg['From'] = user
#     msg['To'] = ','.join(recipient)
#
#     part2 = MIMEText(body)
#     msg.attach(part2)
#
#     #s = smtplib.SMTP_SSL('smtp.gmail.com')
#     s = smtplib.SMTP(host="smtp.gmail.com", port=587)
#     s.starttls()
#     s.login(user, pwd)
#     s.sendmail(user, recipient, msg.as_string())
#     s.quit()

# 打开数据库连接
now = int(time.time()-86400)
times = datetime.datetime.now().strftime("%Y-%m-%d")
def SQL(database):
    dict = {}
    db = MySQLdb.connect("45.79.71.23","mdtrade","trade@mingDA123",database)
    cursor = db.cursor()
    sql = "select type, count(lid) as num from log  where timestamp > %s and timestamp < Now() group by type;" %(now)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            type = row[0]
            count = row[1]
            dict[type]=count
        # for k,v in dict.iteritems():
        #     print "dict[%s]==" % k,v
    except:
        print "Error: unable to fecth data"

    sitename = database + str(dict)
    print sitename
    send_email(sitename)
    # 关闭数据库连接
    db.close()
def DUMP(host, user, passwd,dir,database):
    command = 'mysqldump -u%s -p%s -h %s -A | gzip > /data/database/%s/%s.gz' %(user,passwd,host,dir,database)
    subprocess.call(command, shell=True)

def run():
    for line in open('host.list'):
        line = line.strip('\n')
        host,user,passwd,database= line.split(':')
        DUMP(host, user, passwd, dir, database)


if __name__ == '__main__':
    run()
