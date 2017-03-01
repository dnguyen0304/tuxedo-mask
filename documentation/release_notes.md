# Release Notes

## v.1.2.0 (2017-03-01)
##### Changes
- Changed from `common.logging.handlers.KafkaHandler` to Logstash
- Changed to message specification

##### Features
- Added `tuxedo_mask.utilities.StackTraceFilter`
- Added default Tuxedo Mask configuration values for development
- Added default Tuxedo Mask configuration values for testing
- Added release notes
- Added tests for logging configuration

##### Bug Fixes
- Fixed Logstash Upstart configuration file using `bash` instead of `sh`
- Fixed Logstash input file path patterns not matching all files
- Fixed default uWSGI log file path configuration value
