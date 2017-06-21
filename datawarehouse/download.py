# -*- coding: utf-8 -*-
import sys
import os

if sys.version_info[0] == 2:
    from urllib import urlretrieve
else:
    from urllib.request import urlretrieve

DATA_DIR = os.path.join(os.path.expanduser('~'), 'datawarehouse')
if not os.path.isdir(DATA_DIR):
    os.mkdir(DATA_DIR)

def get_data_dir():
	return DATA_DIR

def set_data_dir(new_data_dir):
	global DATA_DIR
	if os.path.isdir(new_data_dir):
		DATA_DIR = new_data_dir

def maybe_download(filename, url):
    if not os.path.exists(filename):
        print("downloading " + filename + "...", end='')
        urlretrieve(url, filename)
        print("Done.")
