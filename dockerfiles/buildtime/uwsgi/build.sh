#!/usr/bin/env bash

set -eu

COMPONENT="uwsgi"

python -m venv virtual-environment
virtual-environment/bin/pip install --requirement requirements.txt
cp virtual-environment/bin/${COMPONENT} ${SHARED_VOLUME}
