#
# file to test the data loader
#

import unittest

import impl


class DataLoaderTest(unittest.TestCase):
    def test_empty(self):
        try:
            dl = impl.DataLoader()
        except:
            self.assertTrue(True)
            return

        # if no exception this is error
        self.assertTrue(False)

    def test_cloud(self):
        data_in = {'eggs': 5, 'milk': 1, 'water': 3}

        dl = impl.DataLoader(media_type="movies", load_data_in=data_in)
        members = dl.getMembers()
        df = dl.accessMember(members[0])

        self.assertTrue(dl.checkMember(members[0]))
        self.assertTrue(df == 5)
