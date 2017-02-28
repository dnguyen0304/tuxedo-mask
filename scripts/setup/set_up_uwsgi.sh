#!/usr/bin/env bash

# Requirements
# ------------
# Tuxedo Mask

mkdir --parents /var/log/uwsgi/

cd /opt/tuxedomask/
.virtual-environment/bin/pip install uwsgi

chown --recursive ubuntu:tuxedomask /var/log/uwsgi/
