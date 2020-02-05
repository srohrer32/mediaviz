#
# root run tests python script, globs other tests and runs all
#

import importlib
import glob
import os
import unittest


def _main():
    # initialize the test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # find the files
    tests = glob.glob("test/*_test.py")
    tests = [os.path.basename(x).split('.')[0] for x in tests]

    # import the modules and add to test suite
    for module in map(__import__, tests):
        suite.addTest(unittest.findTestCases(module))

    # initialize a runner and run the tests
    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)


# main method
if __name__ == "__main__":
    _main()
