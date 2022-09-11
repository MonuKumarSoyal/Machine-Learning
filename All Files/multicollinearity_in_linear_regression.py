from turtle import pd
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# df = pd.read_csv('Advertising.csv')

# # print(df.info())

# x = df[['TV', 'radio', 'newspaper']]
# y = df['sales']

# # print(x)
# # print(y)

# x = sm.add_constant(x)
# # print(x)

# model = sm.OLS(y, x).fit() 
# # print(model.summary())

# print(x.iloc[:, 1:].corr())

# --------------------------------------------------- 

df1 = pd.read_csv('Salary_Data.csv')
# print(df1.head())
# print(df1.info())

a = df1[['YearsExperience', 'Age']]
b = df1['Salary']

# print(a)
# print(b)

a = sm.add_constant(a)
# print(a)
model1 = sm.OLS(b, a).fit()

# print(model1.summary())

print(a.iloc[:, 1:].corr())


