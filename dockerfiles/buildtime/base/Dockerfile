FROM python:3.6-slim

MAINTAINER Duy Nguyen <dnguyen0304@gmail.com>

ARG SHARED_VOLUME="/tmp/build"

ENV SHARED_VOLUME=${SHARED_VOLUME}

RUN RUNTIME_DEPENDENCIES="build-essential" && \
    apt-get update -y && \
    apt-get install -y --no-install-recommends ${RUNTIME_DEPENDENCIES}

RUN mkdir ${SHARED_VOLUME} && \
    mkdir /tmp/.build

WORKDIR /tmp/.build

RUN rm -fr /var/lib/apt/lists/*

VOLUME ${SHARED_VOLUME}

ENTRYPOINT ["./build.sh"]
