#!/usr/bin/env bash

set -eu

COMPONENT="tuxedomask"
BRANCH=$1

git clone https://github.com/dnguyen0304/tuxedo-mask.git ${COMPONENT}
cd ${COMPONENT}
git checkout ${BRANCH}
cd ..

PACKAGE="${COMPONENT}-$(grep -Po "version='\K\d\.\d\.\d" ${COMPONENT}/setup.py)"

mkdir ${PACKAGE}

# Include the source code.
cp -r ${COMPONENT}/${COMPONENT} ${PACKAGE}

# Include the dependencies.
pip install --requirement requirements.txt --target ${PACKAGE}

# Include the configuration.
cp -r configuration ${PACKAGE}

# Compress the package.
cd ${PACKAGE}
zip -9qr ${PACKAGE}.zip .
cp ${PACKAGE}.zip ${COMPONENT}-latest.zip
mv ${COMPONENT}-*.zip ${SHARED_VOLUME}
