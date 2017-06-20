# coding: utf-8
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

__version__ = "0.1"
__author__ = "Victor Estrade"

from .higgsml import load_higgs
from .baldi2016 import load_baldi2016_train_no_pile
from .baldi2016 import load_baldi2016_train_pile
from .baldi2016 import load_baldi2016_test_pile
from .baldi2016 import load_baldi2016_test_no_pile
from .mnist import load_mnist
from .magic_gamma import load_gamma_telescope
from .pizza import make_pizza_slice