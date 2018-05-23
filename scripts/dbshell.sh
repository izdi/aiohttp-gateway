#!/usr/bin/env bash

set -e

PGPASSWORD=${POSTGRES__PASSWORD} psql -h ${POSTGRES__HOST} -p ${POSTGRES__PORT} -U ${POSTGRES__USER} ${POSTGRES__DATABASE}
