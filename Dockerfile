#
# install the package on the local machine along with python and dependencies
#

FROM alpine
MAINTAINER Samuel Rohrer version: 0.1

# install python
RUN apt-get update && apt-get --yes install python3-pip

COPY quickstart.sh /
CMD ["/quickstart.sh"]

# install the necessary data and packages
CMD ["make", "install"]
# build the installation
CMD ["make", "package"]

# now run the tests
CMD ["make", "test"]
