#!/usr/bin/env python
#coding:utf-8
# Created: 2016/7/13

import sys
import os
import time


def main():
    while True:
        time.sleep(5)
        try:
            ret = os.popen('ps -C squid3 -o pid,cmd').readlines()
            if len(ret)< 2:
                print"squid3 process killed, restarting service in 5 seconds."
                time.sleep(5)
                os.system("service squid3 restart")
        except:
            print"Error", sys.exc_info()[1]

if __name__ == "__main__":
    main()
