#!/usr/bin/env bash

set -e

NAMESPACE="tuxedomask"

cd $(dirname $0)

BUILD_ROOT=$(pwd)

# Set up the build environment.
if [ -d build ]; then
    rm -r build
fi
mkdir build

# Include uWSGI.
docker build \
    --file "${BUILD_ROOT}/buildtime/uwsgi/Dockerfile" \
    --tag ${NAMESPACE}-uwsgi/buildtime:latest \
    buildtime/uwsgi
docker run --volume ${BUILD_ROOT}/build:/tmp/build ${NAMESPACE}-uwsgi/buildtime:latest

# Tear down the build environment.
rm -r build
