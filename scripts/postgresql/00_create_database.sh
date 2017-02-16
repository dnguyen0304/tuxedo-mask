#!/usr/bin/env bash

set -e

tuxedo_mask_environment=${TUXEDO_MASK_ENVIRONMENT,,}

psql --set ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<EOF
    CREATE DATABASE tuxedo_mask_$tuxedo_mask_environment;
EOF
