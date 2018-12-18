

import warnings
import logging
import itertools
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from hmmlearn.hmm import GaussianHMM
from sklearn.model_selection import train_test_split
from tqdm import tqdm
from docopt import docopt
from scipy.linalg import _fblas


# # Supress warning in hmmlearn
# warnings.filterwarnings("ignore")
# # Change plot style to ggplot (for better and more aesthetic visualisation)
# plt.style.use('ggplot')


if __name__ == '__main__':
    print("Beginning....")