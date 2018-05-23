FROM python:3.6.5
LABEL maintainer="izdieu@gmail.com"

ARG APP_DIR=/var/app

ENV PIPENV_PIPFILE=$APP_DIR/Pipfile

RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main' >> /etc/apt/sources.list.d/postgresql.list \
    && wget --no-check-certificate -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O- | apt-key add - \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client-9.6 \
    && rm -rf /var/lib/apt/lists/*
RUN pip install pipenv

COPY Pipfile* $APP_DIR/
RUN pipenv install --system --deploy --ignore-pipfile

COPY scripts/ $APP_DIR/scripts/
COPY src/ $APP_DIR/src/

WORKDIR $APP_DIR
