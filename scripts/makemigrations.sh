#!/usr/bin/env bash

set -e

export PYTHONPATH=src

export DB__HOST=${POSTGRES__HOST}
export DB__PORT=${POSTGRES__PORT}
export DB__DATABASE=${POSTGRES__DATABASE}
export DB__USER=${POSTGRES__USER}
export DB__PASSWORD=${POSTGRES__PASSWORD}

alembic --config src/db/alembic.ini revision --autogenerate --message=auto
