import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("housing.csv")
# print(df.info())
# print(df["ocean_proximity"].unique())

x = df.iloc[:, :-2]
y = df.iloc[:, -2]

# print(x.head())

# adding the "ocean_proximity" feature in the x dataset
x["ocean_proximity"] = df["ocean_proximity"]

# print(x.head())

new_ocean_proximity = pd.get_dummies(x["ocean_proximity"], drop_first=True)

x = x.drop(["ocean_proximity", "total_bedrooms"], axis=1)


# concatenating the "new_ocean_proximity" feature in the x dataset
x = pd.concat([x, new_ocean_proximity], axis=1)

# print(x.head())


x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=0)

# print(x_train)
# print(x_test)
# print(y_train)
# print(y_test)

regression_model = LinearRegression()
regression_model.fit(x_train, y_train)

y_predicted = regression_model.predict(x_test)

score = r2_score(y_test, y_predicted)

print(score)
