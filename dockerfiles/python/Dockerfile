FROM python:3.6-slim

MAINTAINER Duy Nguyen <dnguyen0304@gmail.com>

ARG build_dependencies="build-essential git libffi-dev libpq-dev"

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends $build_dependencies

RUN mkdir --parents /opt/tuxedo_mask/

COPY . /opt/tuxedo_mask/

WORKDIR /opt/tuxedo_mask/

RUN python -m venv .virtual-environment && \
    /bin/bash -c "source .virtual-environment/bin/activate" && \
    python setup.py install

RUN rm -fr /var/lib/apt/lists/* && \
    apt-get purge -y --auto-remove $build_dependencies