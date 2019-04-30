#
# install the package on the local machine along with python and dependencies
#

FROM ubuntu
MAINTAINER Samuel Rohrer

# install python
RUN apt-get update
RUN apt-get install python3-pip

# install the necessary data and packages
CMD ["make", "install"]
# build the installation
CMD ["make", "package"]

# now run the tests
