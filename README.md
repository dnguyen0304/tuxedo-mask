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
### Trace a Call
```
import logging

from tuxedo_mask import utilities

with utilities.Tracer('my_next_function_or_method') as tracer:
    my_next_function_or_method()

logger = logging.getLogger(__name__)
logger.debug(tracer.message, extra=tracer.to_json())
```

Architecture
------------
This service implements a five-tier architecture.
- At the API tier, *Resources* provide an interface for inbound client requests. Resources are purely for orchestrating work between the underlying Services, Repositories, Models, and Views. In this sense, they are comparable to Controllers in the classical MVC definition.
- At the services tier, *Services* house the primary business logic functions.
- At the data tier, *Repositories* enable Services to perform primitive CRUD operations. A Service may bind to 0 or more Repositories.
- At the domain tier, *Models* are how Repositories represent database entities and are the system's fundamental objects.
- At the presentation tier, *Views* "marshall" or serialize Models so Resources can respond to clients.