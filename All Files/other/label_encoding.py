import pandas as pd 
import numpy as np
from sklearn import preprocessing

df = pd.read_csv("Iris.csv")
# print(df.head())

print(df["Species"].unique())

encoder = preprocessing.LabelEncoder()

df["Species"] = encoder.fit_transform(df["Species"])

print(df["Species"].unique())