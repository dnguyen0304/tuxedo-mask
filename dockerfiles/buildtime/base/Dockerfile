FROM python:3.6-slim

MAINTAINER Duy Nguyen <dnguyen0304@gmail.com>

ARG SHARED_VOLUME="/tmp/build"
ARG RUNTIME_DEPENDENCIES="build-essential"

ENV SHARED_VOLUME=${SHARED_VOLUME}

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends ${RUNTIME_DEPENDENCIES}

RUN mkdir ${SHARED_VOLUME} && \
    mkdir /tmp/.build

WORKDIR /tmp/.build

RUN rm -fr /var/lib/apt/lists/*

VOLUME ${SHARED_VOLUME}

ENTRYPOINT ["./build.sh"]
