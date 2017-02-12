#!/usr/bin/env bash

set -e

tuxedo_mask_environment=${TUXEDO_MASK_ENVIRONMENT,,}

psql --set ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<EOF
    CREATE ROLE tuxedo_mask_$tuxedo_mask_environment;
    CREATE DATABASE tuxedo_mask_$tuxedo_mask_environment;

    GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO tuxedo_mask_$tuxedo_mask_environment;
    GRANT USAGE ON ALL SEQUENCES IN SCHEMA public TO tuxedo_mask_$tuxedo_mask_environment;
EOF
