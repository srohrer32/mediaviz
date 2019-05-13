#
# function to return members of dict and print non members (all lowercase)
#

import pandas as pd

def findMembers(input_names, names):
    if input_names == "" or input_names == []:
        raise RuntimeError("no inputs to determine membership")

    # setup output lists
    members = []
    nonmembers = []

    if isinstance(names, pd.DataFrame):
        names = set(names.str.lower())

    # now iter over placing in each list
    for el in input_names:
        el_lower = el.lower().lstrip()
        if el_lower in names:
            members.append(el)
        else:
            nonmembers.append(el)

    # return the members
    return members
