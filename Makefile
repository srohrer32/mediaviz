#
# Makefile to build project
#

# make rule to build package
package:
	pip3 install .

# make rule to install package
install:
	$(shell export PYTHONPATH=./:$PYTHONPATH)
	$(shell scripts/download_imdb_data.sh)
	$(shell pip3 install -r requirements.txt)

clean:
	$(shell rm -r data/)

.PHONY: clean