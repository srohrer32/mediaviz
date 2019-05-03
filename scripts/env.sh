#!/bin/bash
#
# script to setup environment variables
#

# add local dir to pick up the impl package
export PYTHONPATH="./$PYTHONPATH"

# add flask app location
export FLASK_APP="./impl/webgui/app.py"
