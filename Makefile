#
# Makefile to build project
#

# make rule to build package
package:
	pip3 install .

# test
test:
	python3 tests/run_all_tests.py

# make rule to install package
install:
	$(shell export PYTHONPATH=./:$PYTHONPATH)
	$(shell ./scripts/data/download_imdb_data.sh)
	$(shell pip3 install -r requirements.txt)

# remove install artifacts
clean:
	$(shell rm -rf data)

.PHONY: clean