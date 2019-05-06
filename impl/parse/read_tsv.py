#
# Functions to read TSV file
#

import pandas as pd

def read_tsv(filename=""):
    # if no file fail
    if filename == "":
        raise RuntimeError("no filename provided to read_tsv")

    return pd.read_csv(filename, sep='\t')