#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import os
import re
def handle(filename1, filename2, dirname):
    FILES = []
    URLS = []
    with open(filename1) as f:
        FILES = [line.strip() for line in f]

    with open(filename2) as f:
        URLS = [line.strip() for line in f]
    for root,dirs,files in os.walk(dirname):
        for file in files:
            if file in FILES:
                f = open(os.path.join(dirname,file))
                lines = f.readlines()
                png = "\n".join(lines)
                reg = re.compile(r'(<a href=.*?>).*?(<\/a>)')
                reg2 = re.compile(r'<a href=("|\')(.*?)("|\')>')
                href2 = reg2.findall(png)
                m = re.search(reg,png)
                res = m.group(1)
                res2 = m.group(2)
                ref = re.sub(res, "", png)
                ref2 = re.sub(res2, "", ref)
                f.close()

                for i,b,c in href2:
                    if b in URLS:

                        f = open(os.path.join(dirname,file), 'w')
                        f.write(ref2)
                        f.close()
                    else:
                        print b + "  not in" + filename2
                        continue

def main():
    filename1 = 'all_html.txt'
    filename2 = 'site_index.txt'
    dirname = 'www.bgtopics.com'
    handle(filename1, filename2, dirname)


if __name__ == "__main__":
    main()