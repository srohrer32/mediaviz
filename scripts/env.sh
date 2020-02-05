#!/bin/bash
#
# script to setup environment variables
#

# add local dir to pick up the impl package
export PYTHONPATH="./$PYTHONPATH"

# add flask app location
#   find the application root directory
CWD="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/$(basename "${BASH_SOURCE[0]}")"
#   remove the two subdirectories to set FLASK_APP correctly
CWD=$(dirname $(dirname $CWD))
export FLASK_APP=$CWD"/webgui/app.py"

# turn on correct character set
export LC_ALL="C.UTF-8"
