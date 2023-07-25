cd /proj/gb

docker build -t mariadb:latest .

docker run -it --name mari -p 3306:3306 -v /home/user/db_data/:/var/lib/mysql -d mariadb

docker run --name pma_mari -d --link mari:db -p 8081:80 phpmyadmin/phpmyadmin:latest
