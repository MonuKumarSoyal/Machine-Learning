import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv("googleplaystore.csv")


print(dataset.Survived)
sns.distplot(dataset.Survived)
plt.show()

# sns.distplot(dataset.Survived, bins = 10, kde = False) .........  by writing kde = False we will not get the probability density graph
# plt.show()

# plt.style.use("dark_background")



# sns.distplot(dataset.Survived, bins = 10, color = "r")
# plt.title("Graph for probability Distribution of Survived in Titanic Ship", color = "r", size = 20)
# plt.show()



# print(dataset.head()) # for displaying the entire dataset we can use dataset.to_string() funtion 

# print(dataset['Content Rating'].value_counts())

# by below line we are removing the "Adults only 18+" and Unrated category form the dataset 
# dataset = dataset[~dataset["Content Rating"].isin(["Adults only 18+","Unrated"])]

# resetting the index in the dataset 
# dataset.reset_index(inplace = True, drop = True)

# Analyzing the Content Rating column 
# print(dataset["Content Rating"].value_counts())


# below is to draw a pie chart
# plt.figure(figsize =[3, 3])
# dataset["Content Rating"].value_counts().plot.pie()
# plt.show()

# below is to drow the bar graph 

# plt.figure(figsize = [9, 7])
# dataset["Content Rating"].value_counts().plot.bar()
# plt.show()


# scatter plot using sns.jointplot 
# sns.jointplot(dataset.Size, dataset.Rating)
# sns.jointplot(dataset.Size, dataset.Rating)
# plt.show()



# sns.pairplot(dataset[['Reviews', 'Size', 'Price','Rating']])
# plt.show()


# plotting a heat graph 
# sns.heatmap(dataset)  this will throw an error since many values in the dataset are integers so for that we have to make them as character
# plt.show() 

