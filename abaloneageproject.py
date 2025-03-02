# -*- coding: utf-8 -*-
"""AbaloneAgeProject

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yGap1Mx4JxbM3E9w-Idl2z-gFC4fxq8f
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler

cols = ["sex", "length", "diameter", "height", "wholeWeight", "shuckedWeight", "visceraWeight", "shellWeight", "rings"]
df = pd.read_csv("abalone.data", names = cols)
df = df.drop("sex", axis = "columns")
cols = ["length", "diameter", "height", "wholeWeight", "shuckedWeight", "visceraWeight", "shellWeight", "rings"]

df.head()

for label in cols[:-1]:
  plt.scatter(df[label], df["rings"])
  plt.title(label)
  plt.xlabel(label)
  plt.ylabel("Number of Rings")
  plt.show()

"""#Train, validation, test datasets"""

train, valid, test = np.split(df.sample(frac=1), [int(0.6*len(df)), int(0.8*len(df))])

def scale_dataset(dataframe, oversample=False):
  X = dataframe[dataframe.columns[:-1]].values
  y = dataframe[dataframe.columns[-1]].values

  scaler = StandardScaler()
  X = scaler.fit_transform(X)

  if oversample:
    ros = RandomOverSampler()
    X, y = ros.fit_resample(X, y)

  data = np.hstack((X, np.reshape(y, (-1, 1))))

  return data, X, y

train, X_train, y_train = scale_dataset(train, oversample=True)
valid, X_valid, y_valid = scale_dataset(valid, oversample=False)
test, X_test, y_test = scale_dataset(test, oversample=False)

"""#KNN"""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)

y_pred = knn_model.predict(X_test)