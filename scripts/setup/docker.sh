#!/bin/sh
#
# script to setup docker server for local tests
#

# make the machine
docker-machine create default

# set env vars
eval $(docker-machine env default)

# build image
docker build -t local_build .

# run the built image
docker run -ti local_build:latest