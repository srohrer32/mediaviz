#
#  driver class for movies, loads data and forms
#


import os
import random

from impl.data_loader import DataLoader


class MovieDriver:

    def __init__(self):
        # make the data loader
        self.dl = DataLoader(media_type="movies")

        # save labels and data
        self.data = self.dl.cleanData()
        self.labels = self.dl.getLabels()

        # one byte of random numbers ... 0 -> 255  ... 0 -> 7
        self.numMovies = int.from_bytes(os.urandom(1), 'little') % 0xF


    def getData(self):
        return self.data

    def getLabels(self):
        return self.labels

    def __generateMovies(self):
        return random.sample(self.labels, self.numMovies)

    def pickRandomMovies(self):
        return self.__generateMovies()
