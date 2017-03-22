#!/usr/bin/env bash

set -eu

NAMESPACE="tuxedomask"
BRANCH=$1

cd $(dirname $0)

BUILD_ROOT=$(pwd)

remove_directories() {

    directories=( "$@" )
    counter=${#directories[@]}

    for (( i=0; i<${counter}; i++ ));
    do
        if [ -d ${directories[$i]} ]; then
            rm -r ${directories[$i]}
        fi
    done

}

# Set up the buildtime environment.
remove_directories "build" "buildtime/${NAMESPACE}/configuration" "runtime/${NAMESPACE}/build"
mkdir build

# Include uWSGI.
docker build \
    --file buildtime/uwsgi/Dockerfile \
    --tag ${NAMESPACE}-uwsgi/buildtime:${BRANCH} \
    buildtime/uwsgi
docker run \
    --volume ${BUILD_ROOT}/build:/tmp/build \
    ${NAMESPACE}-uwsgi/buildtime:${BRANCH}

# Include Tuxedo Mask.
cp -r ../configuration buildtime/${NAMESPACE}

docker build \
    --file buildtime/${NAMESPACE}/Dockerfile \
    --tag ${NAMESPACE}-${NAMESPACE}/buildtime:${BRANCH} \
    buildtime/${NAMESPACE}
docker run \
    --volume ${BUILD_ROOT}/build:/tmp/build \
    ${NAMESPACE}-${NAMESPACE}/buildtime:${BRANCH} \
    ${BRANCH}

# Build the runtime container.
mv build runtime/${NAMESPACE}

environments=( "development" "testing" )
counter=${#environments[@]}

for (( i=0; i<${counter}; i++ ));
do
    docker build \
        --file runtime/${NAMESPACE}/Dockerfile \
        --tag dnguyen0304/${NAMESPACE}-${BRANCH}:${environments[$i]} \
        --build-arg NAMESPACE=${NAMESPACE} \
        --build-arg ENVIRONMENT=${environments[$i]^} \
        --build-arg UWSGI_CONFIGURATION_FILE_NAME="uwsgi.${environments[$i]}.config" \
        --build-arg TUXEDOMASK_CONFIGURATION_FILE_NAME="tuxedomask.${environments[$i]}.config" \
        runtime/${NAMESPACE}
done
