#
#  driver class for movies, loads data and forms
#

from impl.data_loader import DataLoader

import pandas as pd

class MovieDriver():

    def __clean_data(self):
        # now make the dataframe to run inference on
        mems = self.dl.getMembers()

        for m in mems:
            new_df = self.dl.accessMember(m)
            new_df.set_index('tconst')
            if self.data.empty:
                self.data = new_df
            else:
                self.data = self.data.join(new_df, lsuffix="_l", rsuffix="_r")

        # remove columns not used
        self.data.drop(self.data[self.data['isAdult'] == 1].index, inplace=True)
        self.data.drop(self.data[self.data['titleType'] == 'short'].index,
                inplace=True)
        self.data.drop(columns=['isAdult', 'runtimeMinutes', 'endYear',
            'originalTitle', 'tconst_r', 'tconst_l'], inplace=True)

        # reindex now
        self.data.reset_index(inplace=True)


    def __init__(self):
        # make the data loader
        self.dl = DataLoader(media_type="movies")
        self.data = pd.DataFrame()

        self.__clean_data()
