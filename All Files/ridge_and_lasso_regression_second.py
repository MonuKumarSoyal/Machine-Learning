import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score


df = load_boston()
dataset = pd.DataFrame(df.data)
# print(dataset.head())

dataset.columns = df.feature_names
# print(dataset.head())


dataset["Price"] = df.target
print(dataset.head())

print(dataset.iloc[2, 5])

# x = dataset.iloc[:, :-1]
# y = dataset.iloc[:, -1]
# # print(x)
# # print(y)


# lin_regressor = LinearRegression()
# mse = cross_val_score(lin_regressor, x, y, scoring = "neg_mean_squared_error", cv = 5)
# mse_mean = np.mean(mse)
# print(mse_mean)











