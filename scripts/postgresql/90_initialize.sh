#!/usr/bin/env bash

set -e

tuxedo_mask_environment=${TUXEDO_MASK_ENVIRONMENT,,}
applications_sid=$(cat /dev/urandom | tr -cd '0-9A-Za-z' | head -c 32)

psql --set ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "tuxedo_mask_$tuxedo_mask_environment" <<EOF
    CREATE ROLE tuxedo_mask_$tuxedo_mask_environment WITH LOGIN PASSWORD 'tuxedo_mask_$tuxedo_mask_environment';

    GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO tuxedo_mask_$tuxedo_mask_environment;
    GRANT USAGE ON ALL SEQUENCES IN SCHEMA public TO tuxedo_mask_$tuxedo_mask_environment;

    INSERT INTO applications (
        applications_sid,
        name,
        created_by
    )
    VALUES
        ('$applications_sid', 'tuxedo_mask', 1);
EOF
