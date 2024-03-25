#!/bin/bash
set -o errexit
set -o pipefail
set -o nounset

if [ -f "${PWD}/backend/.env.local" ]; then
  source "${PWD}"/backend/.env.local
fi