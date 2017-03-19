FROM python:3.6-slim

MAINTAINER Duy Nguyen <dnguyen0304@gmail.com>

ARG NAMESPACE="tuxedomask"
ARG BUILD_DEPENDENCIES="unzip"
ARG PACKAGE_NAME
ARG ENVIRONMENT
ARG UWSGI_CONFIGURATION_FILE_NAME
ARG TUXEDOMASK_CONFIGURATION_FILE_NAME

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends ${BUILD_DEPENDENCIES}

RUN useradd ${NAMESPACE}


# Include uWSGI.
COPY uwsgi /usr/local/bin

RUN chown ${NAMESPACE}:${NAMESPACE} /usr/local/bin/uwsgi && \
    mkdir --parents /var/log/uwsgi && \
    chown --recursive ${NAMESPACE}:${NAMESPACE} /var/log/uwsgi


# Include Tuxedo Mask.
ENV UWSGI_CONFIGURATION_FILE_PATH="/opt/${NAMESPACE}/configuration/${UWSGI_CONFIGURATION_FILE_NAME}"
ENV TUXEDOMASK_ENVIRONMENT=${ENVIRONMENT}
ENV TUXEDOMASK_CONFIGURATION_FILE_PATH="/opt/${NAMESPACE}/configuration/${TUXEDOMASK_CONFIGURATION_FILE_NAME}"

COPY ${PACKAGE_NAME} /tmp

RUN mkdir --parents /opt/${NAMESPACE} && \
    mkdir --parents /var/log/${NAMESPACE}

WORKDIR /opt/${NAMESPACE}

RUN mv /tmp/${PACKAGE_NAME} . && \
    unzip ${PACKAGE_NAME} && \
    chown --recursive ${NAMESPACE}:${NAMESPACE} . && \
    chown --recursive ${NAMESPACE}:${NAMESPACE} /var/log/${NAMESPACE}


RUN rm -fr /var/lib/apt/lists/* && \
    apt-get purge -y --auto-remove ${BUILD_DEPENDENCIES}

USER ${NAMESPACE}
