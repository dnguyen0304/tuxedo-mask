FROM dnguyen0304/tuxedomask-buildtime:latest

RUN RUNTIME_DEPENDENCIES="git libffi-dev libpq-dev zip" && \
    apt-get update -y && \
    apt-get install -y --no-install-recommends ${RUNTIME_DEPENDENCIES}

COPY build.sh .
COPY configuration ./configuration
COPY requirements.txt .

RUN rm -fr /var/lib/apt/lists/*
