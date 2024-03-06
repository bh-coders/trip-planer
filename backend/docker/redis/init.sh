#!/bin/bash
# if any of the commands in your code fails for any reason, the entire script fails
set -o errexit
# fail exit if one of your pipe command fails
set -o pipefail
# exits if any of your variables is not set
set -o nounset

echo "Add sysctl vm.overcommit_memory=1"
echo "1" > /proc/sys/vm/overcommit_memory

export REDIS_PASSWORD="${CACHE_STORAGE_PASSWORD}"

echo "Starting redis server..."

echo "Redis server is up"

# Start redis server
redis-server --bind 0.0.0.0 --requirepass "${REDIS_PASSWORD}" --maxmemory 256mb --maxmemory-policy allkeys-lru --appendonly yes

echo "Redis server started"

