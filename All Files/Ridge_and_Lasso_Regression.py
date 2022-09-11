import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_boston   # load_boston is a dataset
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import Lasso, LinearRegression, lasso_path
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split




df = load_boston()
# print(df.unique())
# print(df)

dataset = pd.DataFrame(df.data)
print(dataset.head())

dataset.columns = df.feature_names # to assign the feature name at the top of the dataset (as heading)
# print(dataset.head())

# print(df.target.shape) # by this we get the size of the target (we get how many number of target vaiables are there)

dataset["Price"] = df.target
# print(dataset.head())

x = dataset.iloc[:, :-1] # independent features
y = dataset.iloc[:, -1] # dependent 

lin_regressor = LinearRegression()
# print(lin_regressor)

mse = cross_val_score(lin_regressor, x, y, scoring = 'neg_mean_squared_error', cv = 5)
# print(mse)  # it will be a list since the cv value is set to be 5 so in list we will have 5 values 

mean_mse = np.mean(mse) # to take average of the 5 values of mse

# print(mean_mse)

# --------------------------------------------------------------------
# Ridge regression 

ridge = Ridge()

parameters = {'alpha': [1e-15, 1e-10, 1e-8, 1e-3, 1e-2, 1, 5, 10, 20, 30, 35, 40, 45, 50, 55, 100]}
ridge_regressor = GridSearchCV(ridge, parameters, scoring = "neg_mean_squared_error", cv = 5)
ridge_regressor.fit(x, y)

# print(ridge_regressor.best_params_)
# print(ridge_regressor.best_score_)

lasso = Lasso()
parameters = {'alpha': [1e-15, 1e-10, 1e-8, 1e-3, 1e-2, 1, 5, 10, 20, 30, 35, 40, 45, 50, 55, 100]}
lasso_regressor = GridSearchCV(lasso, parameters, scoring = 'neg_mean_squared_error', cv = 5)
lasso_regressor.fit(x, y)

# print(lasso_regressor.best_params_)
# print(lasso_regressor.best_score_)


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 0)

prediction_ridge = ridge_regressor.predict(x_test)
prediction_lasso = lasso_regressor.predict(x_test)

sns.distplot(y_test-prediction_lasso)
plt.show()


sns.distplot(y_test-prediction_ridge)
plt.show()













