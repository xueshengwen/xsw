#!/bin/bash
for ym in `cat dns.txt`
do
	   ip=`ping -c1  $ym |awk -F '[ )(]' 'NR ==1 {print $4}'`
	      echo "$ip|$ym"  >> ip.txt
	  done
