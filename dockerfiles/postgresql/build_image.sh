#!/usr/bin/env bash

set -e

cd $(dirname $0)

cp ../../scripts/postgresql/* .

docker build --file Dockerfile .

find . -type f -name "*.sh" ! -name $(basename $0) -delete
