#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%%
dataset = pd.read_csv('../data/train.csv')
X = dataset.values[:, :-1]
y = dataset.values[:, -1]