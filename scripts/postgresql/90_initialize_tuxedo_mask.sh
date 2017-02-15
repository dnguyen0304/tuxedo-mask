#!/usr/bin/env bash

set -e

tuxedo_mask_environment=${TUXEDO_MASK_ENVIRONMENT,,}
applications_sid=$(cat /dev/urandom | tr -cd '0-9A-Za-z' | head -c 32)

psql --set ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "tuxedo_mask_$tuxedo_mask_environment" <<EOF
    INSERT INTO applications (
        applications_sid,
        name,
        created_by
    )
    VALUES
        ('$applications_sid', 'tuxedo_mask', 1);
EOF
