import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv("uni_Bi_Multi_Variate.csv")

# print(dataset.head())  it is just to print first 5 line of the dataset 

# print(dataset.shape)   by this we get the dimension of the dataset
data_setosa = dataset.loc[dataset["species"] == "setosa"]            # for storing those rows where species are setosa
data_virginica = dataset.loc[dataset["species"] == "virginica"]      # for storing those rows where species are virginica
data_versicolor= dataset.loc[dataset["species"] == "versicolor"]     # for storing those rows where species are versicolor


# ----- for printing the above data

# print(data_setosa)  
# print(data_virginica)
# print(data_versicolor)

# -----------------------------------------------------


# plt.plot(data_setosa["sepal_length"], np.zeros_like(data_setosa["sepal_length"]), 'o') # for plotting the graph between setosa and sepal_length 

# plt.plot(data_virginica["sepal_length"], np.zeros_like(data_virginica["sepal_length"]), 'o')  # for plotting the graph between virginica and sepal_length 

# plt.plot(data_versicolor["sepal_length"], np.zeros_like(data_versicolor["sepal_length"]), 'o')  # for plotting the graph between versicolor and sepal_length 
# plt.show()

# -------------------------------------------------------

# sns.FacetGrid(dataset, hue = "species", size = 5).map(plt.scatter, "sepal_length", "sepal_width").add_legend();
# sns.FacetGrid(dataset, hue = "species", size = 5).map(plt.scatter, "petal_length", "sepal_width").add_legend();


# sns.distplot(data_setosa["sepal_length"])  # this is to plot a graph of the sepal_length with respect to count(here density)
# plt.show()

# sns.pairplot(dataset, hue = "species", size = 3)    # plotting the graph for multivariate
# plt.show()




