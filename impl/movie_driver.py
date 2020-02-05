#
#  driver class for movies, loads data and forms
#


from impl.data_loader import DataLoader

import numpy as np
import pandas as pd

import os


class MovieDriver:

    def __init__(self):
        # make the data loader
        self.dl = DataLoader(media_type="movies")
        # save labels and data
        self.data = self.dl.cleanData()
        self.labels = self.dl.getLabels()

    def getData(self):
        return self.data

    def getLabels(self):
        return self.labels

    def __generateMovies(self, numMovies):
        return random.sample(self.labels, numMovies)

    def pickRandomMovies(self):
        # one byte of random numbers ... 0 -> 255  ... 0 -> 7
        self.numMovies = os.urandom(1) % 16

    return self.__generateMovies(self.numMovies)

