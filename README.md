Tuxedo Mask
-----------
A lightweight, minimalist Identity and Access Management microservice.

Getting Started
---------------
### General
```
$ git clone https://github.com/dnguyen0304/tuxedo-mask.git
$ cd tuxedo-mask/ 
```

### PostgreSQL Database
A Docker image is available in a [public Docker Hub repository](https://hub.docker.com/r/dnguyen0304/tuxedo-mask-postgresql/).
```
$ sudo docker pull dnguyen0304/tuxedo-mask-postgresql:latest
$ sudo docker run --detach --name postgres --publish 5432:5432 --env POSTGRES_PASSWORD=postgres --env TUXEDO_MASK_ENVIRONMENT=<tuxedo_mask_environment> dnguyen0304/tuxedo-mask-postgresql:latest
```

To build a Docker container from source, run
```
$ sudo docker build --file dockerfiles/postgresql/Dockerfile .
```

### Python Package
A Docker image is available in a [public Docker Hub repository](https://hub.docker.com/r/dnguyen0304/tuxedo-mask-python/).
```
$ sudo docker pull dnguyen0304/tuxedo-mask-python:latest
```

To build a Docker container from source, run
```
$ sudo docker build --file dockerfiles/python/Dockerfile .
```

Configuration
-------------
### Shell Environment
To set the environment variables for the current and all future shell sessions, from the terminal run
```
$ echo 'export TUXEDOMASK_ENVIRONMENT="Development"' >> ~/.bashrc
$ echo 'export TUXEDOMASK_CONFIGURATION_FILE_PATH=/opt/tuxedo-mask/configuration/tuxedo_mask.development.config"' >> ~/.bashrc
$ source ~/.bashrc
```

Below is the list of acceptable values. Note they are case-sensitive.
- Production
- Staging
- Testing
- Development

### File
The file stubs are located in `tuxedo_mask/configuration`.
- `components.hashing.iterations`: Number of iterations to run the salting algorithm.
- `databases.postgresql.connection_string`: Formatted string containing the host and authentication information. See the [SQLAlchemy Engine Configuration documentation](http://docs.sqlalchemy.org/en/latest/core/engines.html) for more details.