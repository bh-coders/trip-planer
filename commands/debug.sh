#!/bin/bash
set -o errexit
set -o pipefail
set -o nounset

source ./commands/load-env.sh

if [ "${DEBUG}" = 1 ]; then
  docker-compose -f docker-compose.dev.yml --profile dev stop
  docker-compose -f docker-compose.dev.yml --profile dev-less start
  docker-compose -f docker-compose.dev.yml run --rm --service-ports backend
fi