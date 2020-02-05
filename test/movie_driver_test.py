#
# tests for the movie driver
#

from impl import MovieDriver

import unittest
from unittest.mock import patch, Mock


class MovieDriverTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.md = Mock(MovieDriver, return_value=None)

    @patch.object(MovieDriver, 'getLabels')
    def test_basic(self, md):
        correct = ["averageRating", "numVotes", "startYear", "genres"]
        self.assertFalse(correct == list(md.getLabels()))
        self.assertTrue([] == list(md.getLabels()))

    @patch.object(MovieDriver, 'pickRandomMovies')
    def test_random_movies(self, md):
        movies = md.pickRandomMovies()
        self.assertTrue([] == list(md.pickRandomMovies()))
