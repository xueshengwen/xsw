#/bin/bash
cat host.list|while read line
do 
	echo "-A INPUT -s $line -p tcp -m tcp --dport 3306 -j ACCEPT" >> /etc/iptables.up.rules
	iptables-restore < /etc/iptables.up.rules
done
