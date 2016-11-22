#/bin/bash
DATE=$(date +%Y%m%d)
sudo mysqldump -u root -pMDhost2014 mysql > /data/backup/mysql_$DATE.sql
find /data/backup/* -type f -mtime +2 -exec rm -f {} \;
