import pandas as pd
import numpy as np
from sklearn import preprocessing

df = pd.read_csv("titanic.csv")
print(df.head())

print(df["Embarked"].unique())


# not fully made
