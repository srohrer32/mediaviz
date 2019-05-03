# MediaViz

[![Build Status](https://travis-ci.com/srohrer32/mediaviz.svg?branch=master)](https://travis-ci.com/srohrer32/mediaviz)

This project is setup to build on every push, the dependencies follow:

 - `impl/` folder containing the Python package implementation.
 - `tests/` folder containing unit tests for all modules. These can all be run using the command `make test`, and are run automatically on each push.
 - `scripts/` folder containing helpful scripts, some of which are called by other files.

## Installation

 1. Clone repository to directory.
 2. If using virtualenv initialize here. See [documentation](https://virtualenv.pypa.io/en/stable/userguide/).
 3. Run `make install`, this make take a minute to fetch all data and install Python dependencies.
 4. Run `make package`[for local testing] ***or*** `docker build -t local_build .`[run in cloud build].

## Running MediaViz
 1. Run `flask run` if running locally. Run `docker run --publish=5000:5000 -ti local_build:latest flask run --host=0.0.0.0` if running through container.
 2. Navigate to webpage shown at prompt.
 3. Enjoy!