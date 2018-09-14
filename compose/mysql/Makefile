
init_db: prune_db
	docker run --rm -t -v /home/pt/database_backup/sql/wtgldb2/p_wtgldb2_2018-08-03.sql:/tmp/a.sql --network mysql_default mysql:5.7 sh -c 'mysql -h mysql -u root -p123 wtgldb2 < /tmp/a.sql'
prune_db:
	docker-compose down
	docker volume prune
	docker-compose up -d
