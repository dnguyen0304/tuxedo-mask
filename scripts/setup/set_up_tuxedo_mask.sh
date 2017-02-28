#!/usr/bin/env bash

# Requirements
# ------------
# Python
# git
#
# Reminders
# ---------
# Change the Tuxedo Mask configuration file.

apt-get install -y --no-install-recommends build-essential git libffi-dev libpq-dev

groupadd tuxedomask

mkdir --parents /opt/tuxedomask/

cd /opt/tuxedomask
git clone https://github.com/dnguyen0304/tuxedo-mask.git .
/usr/local/bin/python3.6 -m venv .virtual-environment
source .virtual-environment/bin/activate
python setup.py install

chown --recursive duyn:tuxedomask /opt/tuxedomask/
