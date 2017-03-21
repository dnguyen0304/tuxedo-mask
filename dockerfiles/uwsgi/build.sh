#!/usr/bin/env bash

set -eu

python -m venv virtual-environment
virtual-environment/bin/pip install --requirement requirements.txt
cp virtual-environment/bin/uwsgi ${SHARED_VOLUME}
