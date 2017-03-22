FROM python:3.6-slim

MAINTAINER Duy Nguyen <dnguyen0304@gmail.com>

ARG NAMESPACE
ARG BUILDTIME_DEPENDENCIES="unzip"
ARG PACKAGE="${NAMESPACE}-latest.zip"
ARG ENVIRONMENT
ARG UWSGI_CONFIGURATION_FILE_NAME
ARG TUXEDOMASK_CONFIGURATION_FILE_NAME

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends ${BUILDTIME_DEPENDENCIES}

RUN useradd ${NAMESPACE}

# Include uWSGI.
COPY build/uwsgi /usr/local/bin

RUN chown ${NAMESPACE}:${NAMESPACE} /usr/local/bin/uwsgi && \
    mkdir /var/log/uwsgi && \
    chown --recursive ${NAMESPACE}:${NAMESPACE} /var/log/uwsgi

# Include Tuxedo Mask.
ENV UWSGI_CONFIGURATION_FILE_PATH="/opt/${NAMESPACE}/configuration/${UWSGI_CONFIGURATION_FILE_NAME}"
ENV TUXEDOMASK_ENVIRONMENT=${ENVIRONMENT}
ENV TUXEDOMASK_CONFIGURATION_FILE_PATH="/opt/${NAMESPACE}/configuration/${TUXEDOMASK_CONFIGURATION_FILE_NAME}"

RUN mkdir /tmp/.build && \
    mkdir /opt/${NAMESPACE} && \
    mkdir /var/log/${NAMESPACE}

COPY build/${PACKAGE} /tmp/.build

WORKDIR /opt/${NAMESPACE}

RUN mv /tmp/.build/${PACKAGE} . && \
    unzip -q ${PACKAGE} && \
    chown --recursive ${NAMESPACE}:${NAMESPACE} . && \
    chown --recursive ${NAMESPACE}:${NAMESPACE} /var/log/${NAMESPACE}

RUN rm -fr /var/lib/apt/lists/* && \
    apt-get purge -y --auto-remove ${BUILDTIME_DEPENDENCIES}

USER ${NAMESPACE}
