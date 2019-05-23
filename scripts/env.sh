#!/bin/bash
#
# script to setup environment variables
#

# add local dir to pick up the impl package
export PYTHONPATH="./$PYTHONPATH"

# add flask app location
export FLASK_APP="./webgui/app.py"

# turn on correct character set
export LC_ALL="C.UTF-8"
