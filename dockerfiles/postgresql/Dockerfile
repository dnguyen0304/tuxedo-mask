FROM postgres:9.6.2-alpine

MAINTAINER Duy Nguyen <dnguyen0304@gmail.com>

COPY ./scripts/postgresql/00_initialize_postgresql.sh /docker-entrypoint-initdb.d/
COPY ./scripts/postgresql/01_create_applications_table.sh /docker-entrypoint-initdb.d/
COPY ./scripts/postgresql/02_create_applications_users_table.sh /docker-entrypoint-initdb.d/
COPY ./scripts/postgresql/90_initialize_tuxedo_mask.sh /docker-entrypoint-initdb.d/
