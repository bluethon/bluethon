#!/bin/bash

#-------------------
# crontab -e
# m h  dom mon dow   command
# 0 1  *   *   *     /backup_db.sh
#-------------------

# Location to place backups.
backup_dir="/home/blue/dbback"
# databases=`psql -l -t | cut -d'|' -f1 | sed -e 's/ //g' -e '/^$/d'`
database='youkeneng'
# psql user
user='blue'

#String to append to the name of the backup files
# backup_date=`date +%d-%m-%Y`
backup_date=`date +%Y-%m-%d_%H%M%S`
#Numbers of days you want to keep copie of your databases
number_of_days=3000
# for i in $databases; do
    # if [ "$i" != "template0" ] && [ "$i" != "template1" ]; then
        # echo Dumping $i to $backup_dir$i\_$backup_date
        # pg_dump -Fc $i > $backup_dir$i\_$backup_date
    # fi
# done
dir=$backup_dir/$database/
if [[ ! -d "$dir" ]]; then
    mkdir -p $dir
fi

pg_dump -h localhost -Fc $database -U $user > $backup_dir/$database/$backup_date'.db'
find $backup_dir -type f -prune -mtime +$number_of_days -exec rm -f {} \;
