#
# some basic asserts run as test cases
#

import unittest

class BasicTest(unittest.TestCase):
    def test_a(self):
        assert(5 == 5)

    def test_b(self):
        assert("foo" == "foo")

    def test_c(self):
        assert("bar" == 'bar')

    def test_d(self):
        assert(9 == 9)
