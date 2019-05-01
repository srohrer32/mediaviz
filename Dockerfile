#
# install the package on the local machine along with python and dependencies
#

FROM ubuntu
MAINTAINER Samuel Rohrer version: 0.1

# install python
RUN apt-get update && apt-get --yes install python3-pip

# copy repo and change to it
COPY . /tmp/
WORKDIR /tmp/

# set env vars
ENV PYTHONPATH=./$PYTHONPATH
ENV FLASK_APP=./impl/webgui/app.py
ENV LC_ALL=C.UTF-8
EXPOSE 5000

# install packages
RUN pip3 install -r requirements.txt
RUN pip3 install .

# now run the tests
RUN python3 tests/run_all_tests.py
