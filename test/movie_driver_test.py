#
# tests for the movie driver
#

import impl
import unittest

class MovieDriverTest(unittest.TestCase):
    def test_basic(self):
        md = impl.MovieDriver()

        # else check the title
        correct = ["averageRating","numVotes", "startYear", "genres"]


        self.assertTrue(correct == list(md.getData()))

