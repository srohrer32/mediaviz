#
# class to load arbitrary date media, etc
#

import pandas as pd
import os

class DataLoader():

    # data type maps
    ratings_dtypes = {
                'tconst' : str,
                'averageRating' : float,
                'numVotes' : int
            }


    basics_dtypes = {
                'tconst' : str,
                'titleType' : str,
                'primaryTitle' : str,
                'originalTitle' : str,
                'isAdult' : str,
                'startYear' : str,
                'endYear' : str,
                'runtimeMinutes' : str,
                'genres' : str
            }


    # declare the titles to read
    files = [("./data/title.ratings.tsv", ratings_dtypes),
                ("./data/title.basics.tsv", basics_dtypes)]

    data = {}

    def __loadData(self, load_data_in):
        if load_data_in:
            self.data = load_data_in
        else:
            # iter over files checking if present then loading
            for (fl, flds) in self.files:
                if os.path.isfile(fl):
                    self.data[fl] = pd.read_csv(fl, sep='\t', dtype=flds)
                else:
                    raise RuntimeError("Please download: ", fl)


    def __init__(self, media_type="", load_data_in={}):
        if media_type == "movies":
            self.media_type = "movies"
        else:
            raise RuntimeError("Type of media provided does not exist, media: ", media_type)

        # load the data in
        self.__loadData(load_data_in)


    def accessMember(self, member=""):
        if member == "":
            raise RuntimeError("Member dataset not provided")

        if member in self.data:
            return self.data[member]
        else:
            raise RuntimeError("Member ", member, " not found in data")


    def checkMember(self, member=""):
        if member == "":
            raise RuntimeError("Member dataset not provided")

        if member in self.data:
            return True
        else:
            return False


    def getMembers(self):
        return list(self.data.keys())