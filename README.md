# Tuxedo Mask: "Who is Tuxedo Mask?"
A lightweight, minimalist Identity and Access Management microservice.

## Getting Started
### General
```
$ git clone https://github.com/dnguyen0304/tuxedo-mask.git tuxedomask
$ cd tuxedomask
```

### PostgreSQL
A Docker image is available in a [public Docker Hub repository](https://hub.docker.com/r/dnguyen0304/tuxedomask-postgresql/).
```
$ sudo docker pull dnguyen0304/tuxedomask-postgresql:latest
$ sudo docker run --detach --name postgres --publish 5432:5432 \
> --env POSTGRES_PASSWORD=postgres \
> dnguyen0304/tuxedomask-postgresql:latest
```

To build a Docker image from source, run
```
$ cd docker
$ sudo ./postgresql/build_image.sh
```

### Tuxedo Mask
See the section on [Shell Environment Configuration](#shell-environment) for more details.

To build a Docker image from source, run
```
$ cd dockerfiles
$ sudo ./tuxedomask/build_image.sh
```

Configuration
-------------
### Shell Environment
When building from source or outside a Docker container, to set the environment variables for the current and all future shell sessions, from the terminal run
```
$ echo 'export TUXEDOMASK_ENVIRONMENT="Development"' >> ~/.bashrc
$ echo 'export TUXEDOMASK_CONFIGURATION_FILE_PATH=/opt/tuxedomask/configuration/tuxedomask.development.config"' >> ~/.bashrc
$ source ~/.bashrc
```

Below is the list of acceptable values. Note they are case-sensitive.
- Production
- Staging
- Testing
- Development

### File
The file stubs are located in `tuxedomask/configuration`.
- `components.hashing.iterations`: Number of iterations to run the salting algorithm.
- `databases.postgresql.connection_string`: Formatted string containing the host and authentication information. See the [SQLAlchemy Engine Configuration documentation](http://docs.sqlalchemy.org/en/latest/core/engines.html) for more details.

Examples
--------
### Trace a Call
```
import logging

from tuxedomask import utilities

with utilities.Tracer('my_next_function_or_method') as tracer:
    my_next_function_or_method()

logger = logging.getLogger(__name__)
logger.debug(tracer.message, extra=tracer.to_json())
```