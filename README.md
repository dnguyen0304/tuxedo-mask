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
