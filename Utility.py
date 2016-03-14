
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 23:12:52 2016

@author: tmquan
"""

from __future__ import print_function

import mxnet as mx      # For dnn 
import numpy as np      # For matrix operation
import pandas as pd     # For csv io
import cv2
import sys
import logging
import os
import scipy
import re 
import natsort
import matplotlib.pyplot as plt
import csv
import random
import subprocess
###############################################################################
from sklearn.cross_validation import KFold # For cross_validation
from scipy.misc import imresize
from scipy import ndimage
from scipy.stats import norm
from keras.utils.generic_utils import Progbar
from multiprocessing import Process
from joblib import Parallel, delayed
from random import randint
from skimage import data, img_as_float
from skimage import exposure
from pprint import pprint
###############################################################################
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
###############################################################################
def customF1(label, pred):
    """ Custom evaluation metric on F1 mean score.
    """
    #TODO:

###############################################################################


