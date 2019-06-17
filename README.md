# MediaViz

[![Build Status](https://travis-ci.com/srohrer32/mediaviz.svg?branch=master)](https://travis-ci.com/srohrer32/mediaviz)

This project is setup to build on every push, the dependencies follow:

 - `impl/` folder containing the Python package implementation.
 - `test/` folder containing unit tests for all modules. These can all be run using the command `make test`, and are run automatically on each push.
 - `scripts/` folder containing helpful scripts, some of which are called by other files.
 - `webgui/` folder containing the Flask web application and templates.

## Installation

 1. Clone repository to directory.
 2. If using virtualenv initialize here. See [documentation](https://virtualenv.pypa.io/en/stable/userguide/).
 3. Run `docker build -t local_build .`[run in cloud build].

## Running MediaViz
 1. Run `docker run --publish=5000:5000 -ti local_build:latest flask run --host=0.0.0.0` if running through container. To run over https run `docker run --publish=5000:5000 -ti local_build:latest flask run --cert=adhoc --host=0.0.0.0`.
 2. Navigate to webpage shown at prompt.
 3. Enjoy!