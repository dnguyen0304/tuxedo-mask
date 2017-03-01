#!/usr/bin/env bash

# Requirements
# ------------
# Java
#
# Reminders
# ---------
# Change the Logstash configuration file.
# Change the Logstash Upstart configuration file.

set -e

mkdir --parents /opt/logstash/

wget https://artifacts.elastic.co/downloads/logstash/logstash-5.2.1.tar.gz
tar -xf logstash-5.2.1.tar.gz --directory /opt/logstash/ --strip-components 1
cp logstash-5.2.1.tar.gz /opt/logstash/
rm logstash-5.2.1.tar.gz

chown --recursive ubuntu:${NAMESPACE,,} /opt/logstash

ln --symbolic /opt/tuxedomask/scripts/upstart/logstash.${ENVIRONMENT,,}.conf /etc/init/
initctl reload-configuration
start logstash.${ENVIRONMENT,,}
