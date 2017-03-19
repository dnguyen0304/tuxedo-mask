#!/usr/bin/env bash

set -e

NAMESPACE="tuxedomask"

cd $(dirname $0)

BUILD_ROOT=$(pwd)
REPOSITORY_ROOT="${BUILD_ROOT}/../.."


# Set up the build environment for uWSGI.
if [ -d .build ]; then
    rm -r .build
fi
mkdir .build

# Include the binary.
virtualenv --python /usr/local/bin/python3.6 .build/virtual-environment
.build/virtual-environment/bin/pip install uwsgi
cp .build/virtual-environment/bin/uwsgi ${BUILD_ROOT}

# Tear down the build environment.
rm -r .build


# Set up the build environment for Tuxedo Mask.
BUILD_DEPENDENCIES="build-essential git libffi-dev libpq-dev"
PACKAGE_NAME="${NAMESPACE}-$(grep -Po "version='\K\d\.\d\.\d" ${REPOSITORY_ROOT}/setup.py)"

if [ -d .build ]; then
    rm -r .build
fi
mkdir .build
mkdir .build/${PACKAGE_NAME}

# Include the source code.
cp -r ${REPOSITORY_ROOT}/tuxedomask .build/${PACKAGE_NAME}

# Include the dependencies.
apt-get update -y
apt-get install -y --no-install-recommends ${BUILD_DEPENDENCIES}
virtualenv --python /usr/local/bin/python3.6 .build/virtual-environment
.build/virtual-environment/bin/pip install --requirement ${REPOSITORY_ROOT}/requirements.txt --target .build/${PACKAGE_NAME}

# Include the configuration.
cp -r ${REPOSITORY_ROOT}/configuration .build/${PACKAGE_NAME}

# Include the entry point.
cp ${REPOSITORY_ROOT}/scripts/entry_point/main.py .build/${PACKAGE_NAME}

# Compress the package.
cd .build/${PACKAGE_NAME}
zip -9r ${PACKAGE_NAME}.zip *
mv ${PACKAGE_NAME}.zip ${BUILD_ROOT}
cd ${BUILD_ROOT}

cp ${PACKAGE_NAME}.zip ${NAMESPACE}-latest.zip

# Tear down the build environment.
rm -r .build


declare -a ENVIRONMENTS=("development" "testing")
for ENVIRONMENT in ${ENVIRONMENTS[@]}
do
    docker build \
        --file Dockerfile \
        --build-arg PACKAGE_NAME=${PACKAGE_NAME}.zip \
        --build-arg ENVIRONMENT=${ENVIRONMENT^} \
        --build-arg UWSGI_CONFIGURATION_FILE_NAME="uwsgi.${ENVIRONMENT}.config" \
        --build-arg TUXEDOMASK_CONFIGURATION_FILE_NAME="tuxedomask.${ENVIRONMENT}.config" \
        ${BUILD_ROOT}
done

rm uwsgi
rm ${NAMESPACE}-*.zip
