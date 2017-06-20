# coding: utf-8
import sys
import os
import pandas as pd
from .download import maybe_download
from .download import get_data_dir



def load_gamma_telescope():
    """https://archive.ics.uci.edu/ml/datasets/MAGIC+Gamma+Telescope"""
    url='https://archive.ics.uci.edu/ml/machine-learning-databases/magic/magic04.data'
    filepath = os.path.join(get_data_dir(), "magic04.data")
    maybe_download(filepath, url)
    data = pd.read_csv(filepath)
    data.columns = ['fLength', 'fWidth', 'fSize', 'fConc', 
                'fConc1', 'fAsym', 'fM3Long', 'fM3Trans', 'fAlpha', 
                'fDist', 'class']
    X = data.drop(['class'], axis=1)
    y = data['class']
    return X, y
 