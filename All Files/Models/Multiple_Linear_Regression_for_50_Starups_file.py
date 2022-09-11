import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


df = pd.read_csv("50_Startups.csv")
# print(df)

# storing the independent and dependent features in x and y respectively
x = df.iloc[:, :-1]
y = df.iloc[:, -1]

# converting the categorical feature "State" into numerical values
# drop.first = True  will remove first column of different labels and then get_dummies function will generate the dummy variables for different labels
states = pd.get_dummies(x["State"], drop_first=True)

# for dropping the old "State" feature containing the categorical labels
x = x.drop("State", axis=1)

# concatenating the new "State" feature (namely as states) with x
x = pd.concat([x, states], axis=1)

# print(x)

# splitting the dataset df into train and test dataset
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=0)

# print(x_train)
# print(x_test)
# print(y_train)
# print(y_test)

# to initialization the Linear Regression model now regression_model is our Regression model
regression_model = LinearRegression()
regression_model.fit(x_train, y_train)  # Training the model

y_predicted = regression_model.predict(
    x_test)  # predicting the y_test for x_test

# print(y_test)
# print(y_predicted)

# getting the R^2 score to get the performance of our model
score = r2_score(y_test, y_predicted)

print(score)
