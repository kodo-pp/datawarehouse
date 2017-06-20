# -*- coding: utf-8 -*-
import sys
import os
import pandas as pd
import h5py
from .download import maybe_download
from .download import get_data_dir

def load_baldi2016_train_no_pile():
    """
    Loads data from the baldi2016 dataset, and downloads it if necessary.

    Return
    ------
        X, y : as Dataframe, where X is the data and y is the labels
    """
    url = "http://mlphysics.ics.uci.edu/data/hepjets/highlevel/train_no_pile_10000000.h5"
    filename = os.path.join( get_data_dir(), "train_no_pile_10000000.h5" )
    X, y = _load( filename, url )
    return X, y

def load_baldi2016_train_pile():
    """
    Loads data from the baldi2016 dataset, and downloads it if necessary.

    Return
    ------
        X, y : as Dataframe, where X is the data and y is the labels
    """
    url = "http://mlphysics.ics.uci.edu/data/hepjets/highlevel/train_pile_10000000.h5"
    filename = os.path.join( get_data_dir(), "train_pile_10000000.h5" )
    X, y = _load( filename, url )
    return X, y

def load_baldi2016_test_pile():
    """
    Loads data from the baldi2016 dataset, and downloads it if necessary.

    Return
    ------
        X, y : as Dataframe, where X is the data and y is the labels
    """
    url = "http://mlphysics.ics.uci.edu/data/hepjets/highlevel/test_pile_5000000.h5"
    filename = os.path.join( get_data_dir(), "test_pile_5000000.h5" )
    X, y = _load( filename, url )
    return X, y

def load_baldi2016_test_no_pile():
    """
    Loads data from the baldi2016 dataset, and downloads it if necessary.

    Return
    ------
        X, y : as Dataframe, where X is the data and y is the labels
    """
    url = "http://mlphysics.ics.uci.edu/data/hepjets/highlevel/test_no_pile_5000000.h5"
    filename = os.path.join( get_data_dir(), "test_no_pile_5000000.h5" )
    X, y = _load( filename, url )
    return X, y


def _load(filename, url):
    maybe_download(filename, url)
    file = h5py.File(filename,'r')
    columns = ["$m_{trim}$","$τ_{21}^{β=1}$","$C_2^{β=1}$","$C_2^{β=2}$","$D_2^{β=1}$","$D_2^{β=2}$"]
    X = pd.DataFrame(file["features"].value, columns=columns)
    y = pd.DataFrame(file["targets"].value.ravel())
    return X, y
