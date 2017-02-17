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
$ sudo docker run --detach --name postgres --publish 5432:5432 \
> --env POSTGRES_PASSWORD=postgres \
> --env TUXEDO_MASK_ENVIRONMENT="Development" \
> dnguyen0304/tuxedo-mask-postgresql:latest
```

To build a Docker container from source, run
```
$ sudo docker build --file dockerfiles/postgresql/Dockerfile .
```

### Python Package
A Docker image is available in a [public Docker Hub repository](https://hub.docker.com/r/dnguyen0304/tuxedo-mask-python/).
```
$ sudo docker pull dnguyen0304/tuxedo-mask-python:latest
$ sudo docker run -it --rm \
> --env TUXEDOMASK_ENVIRONMENT="Development" \
> --env TUXEDOMASK_CONFIGURATION_FILE_PATH=/opt/tuxedo-mask/configuration/tuxedo_mask.development.config" \
> dnguyen0304/tuxedo-mask-python:latest
```

See the section on [Shell Environment Configuration](#shell-environment) for more details.

To build a Docker container from source, run
```
$ sudo docker build --file dockerfiles/python/Dockerfile .
```

Configuration
-------------
### Shell Environment
When building from source or outside a Docker container, to set the environment variables for the current and all future shell sessions, from the terminal run
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

Examples
--------
*Adding an Authentication Service*
repositories first and just really add()
- Add a reference to the package `__all__` index in `repositories/__init__.py`.
```
# Define a client. This is the unit of work.
$ touch tuxedo_mask/clients/foo_client.py
```
- Subclass `clients.BaseClient`, and implement the abstract methods.

        # This is not a truly complete implementation of the Repository
        # pattern. The Unit of Work should also be abstract to ensure
        # a consistent interface.
### Trace a Call
```
import logging

from tuxedo_mask import utilities

with utilities.Tracer('my_next_function_or_method') as tracer:
    my_next_function_or_method()

logger = logging.getLogger(__name__)
logger.debug(tracer.message, extra=tracer.to_json())
```