#!/bin/sh
#
# script to setup docker server for local tests
#

# make the machine
docker-machine create default

# set env vars
eval "$(docker-machine env default)"

# build image
docker build -t local_build .

# run the built image
docker run -ti local_build:latest

# run the flask app on docker_machine_ip:5000
docker run --publish=5000:5000 -ti local_build:latest flask run --host=0.0.0.0