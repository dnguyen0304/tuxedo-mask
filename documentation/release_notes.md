# Release Notes

## v2.0.0 (Pending)
##### Changes
- Removed Tuxedo Mask Docker Hub repository
- Removed configurable environment in PostgreSQL Dockerfile
- Changed project name to "tuxedomask"
- Changed to container deployment

##### Features
- Added script for building PostgreSQL images
- Added script for building Tuxedo Mask images

##### Fixes
- Fixed `setup.py` including nonessential dependencies

## v1.3.0 (2017-03-02)
##### Changes
- Changed NGINX access log file path
- Changed NGINX access log to use verbose formatting (ME-518)

##### Features
- Added Elasticsearch component (ME-504)
- Added NGINX status page and Logstash log forwarding (ME-516)

## v1.2.1 (2017-03-01)
##### Fixes
- Fixed Logstash Upstart configuration file for development using `bash` instead of `sh`
- Fixed Logstash Upstart configuration file for testing referencing an undefined variable
- Fixed Logstash input file path patterns using regular expressions instead of glob
- Fixed referencing an incorrect logger name

## v1.2.0 (2017-03-01)
##### Changes
- Changed from `common.logging.handlers.KafkaHandler` to Logstash
- Changed to message specification

##### Features
- Added `tuxedomask.utilities.StackTraceFilter`
- Added default Tuxedo Mask configuration values for development
- Added default Tuxedo Mask configuration values for testing
- Added release notes
- Added tests for logging configuration

##### Fixes
- Fixed Logstash Upstart configuration file for testing using `bash` instead of `sh`
- Fixed Logstash input file path patterns not matching all files
- Fixed default uWSGI log file path configuration value
