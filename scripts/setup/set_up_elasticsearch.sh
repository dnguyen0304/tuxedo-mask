#!/usr/bin/env bash

# Requirements
# ------------
# Java
#
# Reminders
# ---------

set -e

installation_directory_path="/opt/elasticsearch/"

groupadd elasticsearch

mkdir --parents $installation_directory_path

wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.2.2.tar.gz
tar -xf elasticsearch-5.2.2.tar.gz --directory $installation_directory_path --strip-components 1
cp elasticsearch-5.2.2.tar.gz $installation_directory_path
rm elasticsearch-5.2.2.tar.gz

chown --recursive ubuntu:elasticsearch $installation_directory_path

/opt/elasticsearch/bin/elasticsearch &

curl --request PUT --url http://127.0.0.1:9200/tuxedomask --header "Content-Type: application/json" --data @- <<EOF
{
  "mappings": {
    "nginx.access": {
      "properties": {
        "timestamp": {
          "type": "date"
        },
        "request_method": {
          "type": "keyword"
        },
        "request_url": {
          "type": "keyword"
        },
        "request_endpoint": {
          "type": "keyword"
        },
        "request_scheme": {
          "type": "keyword"
        },
        "request_body": {
          "type": "text"
        },
        "response_status_code": {
          "type": "short"
        },
        "response_time": {
          "type": "half_float"
        },
        "response_size": {
          "type": "short"
        },
        "response_body_size": {
          "type": "short"
        },
        "client_ip_address": {
          "type": "ip"
        },
        "client_port": {
          "type": "integer"
        },
        "server_ip_address": {
          "type": "ip"
        },
        "server_port": {
          "type": "integer"
        },
        "application_protocol": {
          "type": "keyword"
        },
        "hostname": {
          "type": "keyword"
        },
        "nginx_version": {
          "type": "keyword"
        },
        "upstream_response_time": {
          "type": "half_float"
        },
        "version": {
          "type": "keyword"
        },
        "messauges_uuid": {
          "type": "keyword"
        },
        "type": {
          "type": "keyword"
        },
        "host": {
          "type": "keyword"
        },
        "path": {
          "type": "keyword"
        },
        "@timestamp": {
          "type": "date"
        },
        "@version": {
          "type": "keyword"
        }
      }
    }
  }
}
EOF
