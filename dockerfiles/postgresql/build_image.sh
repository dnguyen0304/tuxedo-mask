#!/usr/bin/env bash

set -e

cd $(dirname $0)

CONTEXT_ROOT=$(pwd)
REPOSITORY_ROOT="${CONTEXT_ROOT}/../.."


cp ${REPOSITORY_ROOT}/scripts/postgresql/* ${CONTEXT_ROOT}

docker build --file Dockerfile ${CONTEXT_ROOT}

find ${CONTEXT_ROOT} -type f -name "*.sh" ! -name $(basename $0) -delete
