#
# class to load arbitrary date media, etc
#

import pandas as pd
import os


class DataLoader():
    # data type maps
    ratings_dtypes = {
        'tconst': str,
        'averageRating': float,
        'numVotes': int
    }

    basics_dtypes = {
        'tconst': str,
        'titleType': str,
        'primaryTitle': str,
        'originalTitle': str,
        'isAdult': str,
        'startYear': str,
        'endYear': str,
        'runtimeMinutes': str,
        'genres': str
    }

    # declare the titles to read
    files = [("./data/title.ratings.tsv", ratings_dtypes),
             ("./data/title.basics.tsv", basics_dtypes)]

    data = pd.DataFrame()

    ld_data = {}

    def __loadData(self, load_data_in):
        if load_data_in:
            self.ld_data = load_data_in
        else:
            # iter over files checking if present then loading
            for (fl, flds) in self.files:
                if os.path.isfile(fl):
                    self.ld_data[fl] = pd.read_csv(fl, sep='\t', dtype=flds)
                else:
                    raise RuntimeError("Please download: ", fl)

    def __clean_imdb_data(self):
        # now make the dataframe to run inference on
        mems = self.getMembers()

        for m in mems:
            new_df = self.accessMember(m)
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

        # set index
        self.data.set_index('primaryTitle', inplace=True)

    def __init__(self, media_type="", load_data_in={}):
        if media_type == "movies":
            self.media_type = "movies"
        else:
            raise RuntimeError("Type of media provided does not exist, media: ", media_type)

        # load the data in
        self.__loadData(load_data_in)

    def cleanData(self):
        self.__clean_imdb_data()

        return self.data

    def accessMember(self, member=""):
        if member == "":
            raise RuntimeError("Member dataset not provided")

        if member in self.ld_data:
            return self.ld_data[member]
        else:
            raise RuntimeError("Member ", member, " not found in data")

    def checkMember(self, member=""):
        if member == "":
            raise RuntimeError("Member dataset not provided")

        if member in self.ld_data:
            return True
        else:
            return False

    def getMembers(self):
        return list(self.ld_data.keys())

    def getData(self):
        return self.data

    def getLabels(self):
        if isinstance(self.data, pd.DataFrame):
            return self.data.index
        else:
            return list(self.data.keys())
