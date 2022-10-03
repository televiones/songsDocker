FROM mysql:5.7

ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE songs
ENV MYSQL_USER=televiones
ENV MYSQL_ROOT_HOST=localhost
ENV MYSQL_PASSWORD=televiones

COPY songs.sql /docker-entrypoint-initdb.d/