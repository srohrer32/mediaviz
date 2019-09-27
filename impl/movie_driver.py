#
#  driver class for movies, loads data and forms
#


from impl.data_loader import DataLoader

import numpy as np
import pandas as pd


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
