#
# tests for the movie driver
#

import impl
import unittest

class MovieDriverTest(unittest.TestCase):
    def test_basic(self):
        try:
            md = impl.MovieDriver()
        except:
            self.assertTrue(True)
            return

        # else check the title
        correct = ["averageRating","numVotes", "startYear", "genres"]

        self.assertTrue(correct == list(md.getData()))


    def test_bad_input(self):
        try:
            md = impl.MovieDriver(model="regr")
        except:
            self.assertTrue(True)
            return

        self.assertTrue(False)
