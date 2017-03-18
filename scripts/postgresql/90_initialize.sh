#!/usr/bin/env bash

set -e

applications_sid=$(cat /dev/urandom | tr -cd '0-9A-Za-z' | head -c 32)

psql --set ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "tuxedomask" <<EOF
    CREATE ROLE tuxedomask WITH LOGIN PASSWORD 'tuxedomask';

    GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO tuxedomask;
    GRANT USAGE ON ALL SEQUENCES IN SCHEMA public TO tuxedomask;

    INSERT INTO applications (
        applications_sid,
        name,
        created_by
    )
    VALUES
        ('$applications_sid', 'tuxedomask', 1);
EOF
