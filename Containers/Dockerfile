FROM alpine
RUN apk update && apk add mysql mysql-client bash \
	--update-cache \
	--repository https://alpine.global.ssl.fastly.net/alpine/edge/community \
	--repository https://alpine.global.ssl.fastly.net/alpine/edge/main \
	--repository https://dl-3.alpinelinux.org/alpine/edge/testing && \
	rm -rf /var/cache/apk/*

ENV MYSQL_ROOT_PASSWORD='gbmypwd'
ENV MYSQL_DATABASE='db'
ENV MYSQL_USER='mysql'
ENV MYSQL_PASSWORD='gbpwd'

COPY startup.sh /startup.sh
COPY my.cnf /etc/my.cnf.d/mariadb-server.cnf

RUN chmod +x /startup.sh

EXPOSE 3306

CMD ["/startup.sh"]

