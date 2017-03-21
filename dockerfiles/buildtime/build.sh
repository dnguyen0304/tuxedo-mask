#!/usr/bin/env bash

set -eu

NAMESPACE="tuxedomask"
BRANCH=$1

cd $(dirname $0)

BUILD_ROOT=$(pwd)

# Set up the build environment.
if [ -d build ]; then
    rm -r build
fi
mkdir build

# Include uWSGI.
docker build \
    --file uwsgi/Dockerfile \
    --tag ${NAMESPACE}-uwsgi/buildtime:${BRANCH} \
    uwsgi
docker run \
    --volume ${BUILD_ROOT}/build:/tmp/build \
    ${NAMESPACE}-uwsgi/buildtime:${BRANCH}

# Include Tuxedo Mask.
cp -r ../../configuration t com${NAMESPACE}

docker build \
    --file ${NAMESPACE}/Dockerfile \
    --tag ${NAMESPACE}-${NAMESPACE}/buildtime:${BRANCH} \
    ${NAMESPACE}
docker run \
    --volume ${BUILD_ROOT}/build:/tmp/build \
    ${NAMESPACE}-${NAMESPACE}/buildtime:${BRANCH} \
    ${BRANCH}

# Tear down the build environment.
rm -r build
rm -r ${NAMESPACE}/configuration
