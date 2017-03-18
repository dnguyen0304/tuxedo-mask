#!/usr/bin/env bash

set -e

psql --set ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<EOF
    CREATE DATABASE tuxedomask;
EOF
