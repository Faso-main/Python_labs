import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
columns = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Species"]
iris_data = pd.read_csv(url, header=None, names=columns)

sns.set(style="whitegrid")
