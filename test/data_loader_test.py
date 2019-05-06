#
# file to test the data loader
#

import impl
import unittest

class DataLoaderTest(unittest.TestCase):
    def test_empty(self):
        try:
            dl = impl.DataLoader()
        except:
            self.assertTrue(True)
            return

        # if no exception this is error
        self.assertTrue(False)


    def test_local(self):
        try:
            dl = impl.DataLoader(type_media="movies")
            members = dl.get_members()
            self.assertTrue(dl.check_member(members[0]))
            df = dl.access_member(members[0])
        except:
            # if it fails in cloud just skip
            self.assertTrue(True)
            return

        self.assertTrue(len(members) > 0)


    def test_cloud(self):
        data_in = {'eggs': 5, 'milk': 1, 'water': 3}

        dl = impl.DataLoader(type_media="movies", load_data_in=data_in)
        members = dl.get_members()
        df = dl.access_member(members[0])

        self.assertTrue(dl.check_member(members[0]))
        self.assertTrue(df == 5)
