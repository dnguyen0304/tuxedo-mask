#!/usr/bin/env bash

set -e

tuxedo_mask_environment=${TUXEDO_MASK_ENVIRONMENT,,}

psql --set ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "tuxedo_mask_$tuxedo_mask_environment" <<EOF
    DROP TABLE IF EXISTS users;

    CREATE TABLE users (
        users_id        serial                                  PRIMARY KEY,
        users_sid       varchar(32)                 NOT NULL    UNIQUE,
        applications_id int                         NOT NULL    REFERENCES applications (applications_id),
        username        varchar(32)                 NOT NULL,
        password        varchar(255)                NOT NULL,
        created_at      timestamp with time zone    NOT NULL    DEFAULT CURRENT_TIMESTAMP,
        created_by      int                         NOT NULL,
        updated_at      timestamp with time zone,
        updated_by      int
    );
EOF
