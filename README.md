# Description

Provide simple helper functions to download and load some datasets.

For HiggsML and HiggsTauTau also include a ```tau_energy_scale()``` function that computes systematic effect on 

# Install 

Use the classical `pip install git+https://github.com/victor-estrade/datawarehouse.git` to install on your local machine.

Or install from source using the *setup.py* script

`python setup.py install`


# Data location

The dataset will be downloaded from the web in a `datawarehouse/` directory located in your home directory at the first call of one of the `load_X()` function.

To change this setting you can change line 10 in the *datawarehouse/download.py* to point to another directory.
