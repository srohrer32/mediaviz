#
#  driver class for movies, loads data and forms
#


from impl.data_loader import DataLoader

import numpy as np
import pandas as pd


class MovieDriver():

    def __clean_imdb_data(self):
        # now make the dataframe to run inference on
        mems = self.dl.getMembers()

        for m in mems:
            new_df = self.dl.accessMember(m)
            new_df.set_index('tconst')
            if self.data.empty:
                self.data = new_df
            else:
                self.data = self.data.join(new_df, lsuffix="_l", rsuffix="_r")

        # now correct data types
        self.data['averageRating'] = self.data['averageRating'].astype(float)
        self.data['numVotes'] = self.data['numVotes'].astype(int)

        self.data.drop(self.data[self.data['genres'] == "\\N"].index,
                inplace=True)
        self.data['genres'] = self.data['genres'].str.split(',').str.get(0)
        self.data.drop(self.data[self.data['startYear'] == "\\N"].index,
                inplace=True)
        self.data['startYear'] = self.data['startYear'].astype(int)
        self.data.drop(self.data[self.data['startYear'] < 1990].index,
                inplace=True)

        # remove rows not used
        self.data.drop(self.data[(self.data['titleType'] != 'movie') &
                (self.data['titleType'] != 'tvMovie')].index,
                inplace=True)
        self.data.drop(self.data[self.data['isAdult'] == 1].index,
                inplace=True)

        # reindex now
        self.data.reset_index(inplace=True)
        # drop rest of columns
        self.data.drop(columns=['isAdult', 'runtimeMinutes', 'endYear',
            'originalTitle', 'tconst_r', 'tconst_l', 'index', 'titleType'],
            inplace=True)


    def __init__(self, model="skl"):
        if model == "skl":
            # make the data loader
            self.dl = DataLoader(media_type="movies")
            self.data = pd.DataFrame()
            # now that the data is loaded clean it
            self.__clean_imdb_data()
            # save labels
            self.labels = self.data['primaryTitle']
            del self.data['primaryTitle']
        else:
            raise NotImplementedError("have not implemented model type ", model)


    def getData(self):
        return self.data


    def getLabels(self):
        return self.labels

