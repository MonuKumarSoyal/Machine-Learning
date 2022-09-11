from optparse import Values
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing

df = pd.read_csv("data.csv")
print(df.head())

# to store the age and salary attributes in array
x = df.iloc[:, 1:3].values
print("The value of x is :", x)


# to give the feature range in which we want to distribute the data
#           ------------------------   Min Max Scalar -------------------------

scalar = preprocessing.MinMaxScaler(feature_range = (0, 1))
# print(scalar)

converted_x = scalar.fit_transform(x)
print("Rescaled x is :", converted_x)
 

#         ------------------------        Standarization      --------------------------


standarized_x = preprocessing.StandardScaler().fit_transform(x)

print("The standarized x is :", standarized_x)
  


















