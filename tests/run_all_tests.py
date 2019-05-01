

import impl
import unittest

class testAll(unittest.TestCase):
    def testA(self):
        assert(4 == 4)
        assert(5 == 4)

if __name__ == "__main__":
    unittest.main()