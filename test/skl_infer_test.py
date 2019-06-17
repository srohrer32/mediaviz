#
# test the scikit learn inference engine
#

import impl

import numpy as np
import pandas as pd
import unittest

class ScikitInferTest(unittest.TestCase):
    def test_empty(self):
        test_df = pd.DataFrame({'home': 1234, 'house': 123, 'street' : 'Brenner'},
                        index=[0])
        skl = impl.ScikitInfer(test_df, np.random.rand(25,1))
        self.assertTrue(True)

    def test_data(self):
        self.assertTrue(True)
