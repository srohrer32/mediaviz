#
# class to load arbitrary date media, etc
#

from impl.parse.read_tsv import read_tsv

import os

class DataLoader():
    # declare the titles to read
    files = ["./data/title.ratings.tsv"]
    data = {}

    def _load_data(self, load_data_in):
        if load_data_in:
            self.data = load_data_in
        else:
            # iter over files checking if present then loading
            for fl in self.files:
                if os.path.isfile(fl):
                    self.data[fl] = read_tsv(fl)
                else:
                    raise RuntimeError("Please download: ", fl)


    def __init__(self, type_media="", load_data_in={}):
        if type_media == "movies":
            self.type_media = "movies"
        else:
            raise RuntimeError("Type of media provided does not exist, media: ", type_media)

        self._load_data(load_data_in)


    def access_member(self, member=""):
        if member == "":
            raise RuntimeError("Member dataset not provided")

        if member in self.data:
            return self.data[member]
        else:
            raise RuntimeError("Member ", member, " not found in data")


    def check_member(self, member=""):
        if member == "":
            raise RuntimeError("Member dataset not provided")

        if member in self.data:
            return True
        else:
            return False


    def get_members(self):
        return list(self.data.keys())