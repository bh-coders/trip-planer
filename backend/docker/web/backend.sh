#!/bin/bash
# if any of the commands in your code fails for any reason, the entire script fails
set -o errexit
# fail exit if one of your pipe command fails
set -o pipefail
# exits if any of your variables is not set
set -o nounset

export FASTAPI_HOST=$FASTAPI_HOST
export FASTAPI_PORT=$FASTAPI_PORT

if [ "${FASTAPI_HOST}" = "localhost" ]; then
  export FASTAPI_HOST=0.0.0.0
fi

uvicorn src.main:app --host "${FASTAPI_HOST}" --port "${FASTAPI_PORT}" --reload