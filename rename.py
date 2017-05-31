#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import urllib
def Test1(rootDir):
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        for d in dirs:
            Dirpath = os.path.join(root, d)
        for f in files:
            newf = f.replace('.htm.html','.htm')
            Filepath = os.path.join(root, newf)

            Newpath = os.path.join(root, f)

            os.rename(Newpath,Filepath)

Test1('escvs2016.org')

# for line in open('file.txt').readlines():
#     url = line
#     data = urllib.urlopen('http://' + url).read()
#     path = 'C:/Users/Administrator/Desktop/bilibili/www.extempo.com/wp-content/themes/paradigm-premium-wordpress-theme-1/Paradigm/css/lightbox/prettyPhoto/' + url.split('/')[-2]
#     if os.path.isdir(path):
#         pass
#     else:
#         os.mkdir(path)
#     filename = path + '/' + url.strip().split('/')[-1]
#     output = open(filename,'wb')
#     output.write(data)
#     output.close()


