#!/usr/bin/env bash

set -e

tuxedo_mask_environment=${TUXEDO_MASK_ENVIRONMENT,,}

psql --set ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "tuxedo_mask_$tuxedo_mask_environment" <<EOF
    DROP TABLE IF EXISTS applications;

    CREATE TABLE applications (
        applications_id     serial                                  PRIMARY KEY,
        applications_sid    varchar(32)                 NOT NULL    UNIQUE,
        name                varchar(32)                 NOT NULL    UNIQUE,
        created_at          timestamp with time zone    NOT NULL    DEFAULT CURRENT_TIMESTAMP,
        created_by          int             NOT NULL,
        updated_at          timestamp with time zone,
        updated_by          int
    );
EOF
