from turtle import pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# pd.pandas.set_option('display.max_columns', None)

dataset = pd.read_csv("train.csv")


# print(dataset.head(30))
# print(dataset.shape[1]) 


#  ------------------------------ Data Analysis part ------------------------------
# Finding missing values 
features_with_nan_value = [feature for feature in dataset.columns if dataset[feature].isnull().sum()>1]
print(len(features_with_nan_value)) # for finding the number of feature which are containing the nan values

# below is to display the percentage of the nan values
for feature in features_with_nan_value:
    print(feature, "--->", np.round(dataset[feature].isnull().mean(), 4),"% missing values")
    # print(feature)   # for printing the feature names


# below is to find the relationship between features containing nan values and target feature(which is "SalePrice")
for feature in features_with_nan_value:
    data = dataset.copy()

    data[feature] = np.where(dataset[feature].isnull(), 1, 0)
    
    print(data.groupby(feature)["SalePrice"].median().plot.bar())
    plt.title(feature)
    plt.subplot()
    plt.show()
    













