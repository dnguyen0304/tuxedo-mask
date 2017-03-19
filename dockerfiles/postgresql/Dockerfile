FROM postgres:9.6.2-alpine

MAINTAINER Duy Nguyen <dnguyen0304@gmail.com>

COPY 00_create_database.sh /docker-entrypoint-initdb.d/
COPY 01_create_table_applications.sh /docker-entrypoint-initdb.d/
COPY 02_create_table_users.sh /docker-entrypoint-initdb.d/
COPY 90_initialize.sh /docker-entrypoint-initdb.d/
