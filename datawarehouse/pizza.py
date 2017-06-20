# coding: utf-8
import os
import numpy as np

def shuffle_array(*args):
    """
    Shuffle the given data. Keeps the relative associations arr_j[i] <-> arr_k[i].

    Params
    ------
        args: (numpy arrays tuple) arr_1, arr_2, ..., arr_n to be shuffled.
    Return
    ------
        X, y : the shuffled arrays.
    """
    # Assert that there is at least one array
    if len(args) == 0:
        raise ValueError('shuffle must take at least one array')
    length = args[0].shape[0]
    # Assert that every array have the same 1st dimension length:
    for i, arr in enumerate(args):
        assert arr.shape[0] == length, "Every array should have the same shape: " \
                        " array {} length = {}  array 1 length = {} ".format(i+1, arr.shape[0], length)
    # Make the random indices
    indices = np.arange(length)
    np.random.shuffle(indices)
    # Return shuffled arrays
    return tuple(arr[indices] for arr in args)

def make_pizza_slice(n_samples=500, radius_sep=0.5, radius_max=1, start_angle=0, end_angle=1, shuffle=True):
    """
    Make the toy dataset.
    
    Parameters
    ----------
        n_samples : (int, default=500) the total number of samples in the dataset
        radius_sep : (float, default=0.5) the radius of the frontier between the 2 classes
        radius_max : (float, default=1) the radius of the complete data
        start_angle : the start angle
        end_angle : the end angle
    Return
    ------
        X: (numpy.ndarray, [n_samples, 2]) the data
        y: (numpy.ndarray, [n_samples]) the labels
    """
    assert radius_sep < radius_max, "radius_sep should be strictly smaller than radius_max."
    rho_0 = np.random.uniform(high=radius_sep, size=n_samples//2)
    rho_1 = np.random.uniform(low=radius_sep, high=radius_max, size=n_samples//2)
    rho = np.concatenate((rho_0, rho_1), axis=0)
    
    theta = np.random.uniform(low=start_angle, high=end_angle, size=n_samples)
    
    X = np.empty(shape=(n_samples, 2))
    X[:, 0] = rho*np.cos(theta)
    X[:, 1] = rho*np.sin(theta)
    
    y = np.zeros(n_samples)
    y[(n_samples//2):] = 1
    
    if shuffle:
        X, y = shuffle_array(X, y)
    return X, y
