import matplotlib.pyplot as plt
import numpy as np;
import pandas as pd
import sklearn.linear_model
import os
import tarfile
import urllib.request

# DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master"
# HOUSING_PATH = os.path.join("datasets", "housing")
# HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"
#
# def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
#     os.makedirs(housing_path, exist_ok=True)
#     tgz_path = os.path.join(housing_path, "housing.tgz")
#     xx = urllib.request.urlretrieve(housing_url)
# #     housing_tgz = tarfile.open(tgz_path)
# #     housing_tgz.extractall(path=housing_path)
# #     housing_tgz.close()
#
# fetch_housing_data()

import tensorflow as tf
print(tf.__version__)
tf.compat.v1.enable_eager_execution()
print(tf.executing_eagerly())

a = tf.constant([1, 2])
b = tf.constant([3, 4])
print(a + b)