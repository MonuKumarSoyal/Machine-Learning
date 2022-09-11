# import imp
# from lib2to3.pytree import convert
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


dataset = pd.read_csv("titanic.csv")

# print(dataset.isnull()) # this is to check how many null values are present in the dataset

sns.heatmap(dataset.isnull(), yticklabels = False, cbar = False, cmap = "viridis")
plt.show()

# sns.set_style("whitegrid")
# sns.countplot(x = "Survived", data = dataset)
# plt.show() 

# sns.set_style("whitegrid")
# sns.countplot(x = "Survived", hue = "Sex", data = dataset, palette = "RdBu_r")
# plt.show()

# plt.figure(figsize = [9, 7])
# sns.boxplot(x = "Pclass", y = "Age", data = dataset, palette = "winter")
# plt.grid()
# plt.show()





# def impute_age(cols):
#     Age = cols[0]
#     Pclass = cols[1]

#     if pd.isnull(Age):
#         if Pclass == 1:
#             return 37
        
#         elif Pclass == 2:
#             return 29
        
#         else:
#             return 24
    
#     else:
#         return Age

# dataset["Age"] = dataset[["Age","Pclass"]].apply(impute_age, axis = 1)

# sns.set_style("whitegrid")
# sns.heatmap(dataset.isnull(), yticklabels = False, cmap = "viridis", cbar = False)
# plt.show()

# dataset.drop("Cabin", axis = 1, inplace = True)
# print(dataset.head())



# print(pd.get_dummies(dataset["Embarked"], drop_first = True).head())


# S = pd.get_dummies(dataset["Sex"], drop_first = True)
# embark = pd.get_dummies(dataset["Embarked"], drop_first = True)

# print(embark)
# print(S)

# to drop column from the dataset
# print(dataset["Name"].head())


# dataset.drop(["Embarked", "Name", "Ticket", "Sex"], axis = 1, inplace = True)
# print(dataset.head())

# dataset = pd.concat([dataset, S, embark], axis = 1)
# print(dataset.head())

# print(dataset["Name"].head())