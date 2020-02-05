#
# tests for parse functions in impl
#

import impl

import pandas as pd
import unittest


class MembersTest(unittest.TestCase):
    def test_normal(self):
        dict_names = {"iron man", "avengers", "toy story 2", "cars", "bee movie"}
        input_names = ["avengers end game", "toy story", "cars", "bee movie"]
        output = impl.findMembers(input_names, dict_names)
        assert (output == ["cars", "bee movie"])

    def test_no_dict(self):
        dict_names = {}
        input_names = ["avengers end game", "toy story", "cars", "bee movie"]
        output = impl.findMembers(input_names, dict_names)
        assert (output == [])

    def test_normal_all(self):
        dict_names = {"iron man", "avengers", "toy story 2", "cars", "bee movie"}
        input_names = ["iron man", "avengers", "toy story 2", "cars", "bee movie"]
        output = impl.findMembers(input_names, dict_names)
        assert (output == ["iron man", "avengers", "toy story 2", "cars", "bee movie"])

    def test_normal_no_input(self):
        dict_names = {"iron man", "avengers", "toy story 2", "cars", "bee movie"}
        input_names = ["iron man 3", "toy story 3", "cars 2", "bee movie 4"]
        output = impl.findMembers(input_names, dict_names)
        assert (output == [])

    def test_normal_no_dict(self):
        dict_names = {}
        input_names = ["iron man 3", "toy story 3", "cars 2", "bee movie 4"]
        output = impl.findMembers(input_names, dict_names)
        assert (output == [])
