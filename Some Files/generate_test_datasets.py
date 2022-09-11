import this
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# mean = 0.5
# std_div = 0.1

# np.random.seed(10)

# X = np.random.normal(mean, std_div, (395, 1))
# # print(X)

# Y = np.random.normal(mean*2, std_div*3, (395, 1))
# # print(Y)

# plt.scatter(X, Y, c = "g")
# plt.show()


point1 = abs(np.random.normal(1, 12, 100))
point2 = abs(np.random.normal(2, 8, 100))
point3 = abs(np.random.normal(3, 2, 100))
point4 = abs(np.random.normal(10, 15, 100))

x = np.c_[point1, point2, point3, point4]
# print(x)

y = [int(np.random.randint(0, 4)) for i in range(100)]
# print(y)


df = pd.DataFrame()


df["col1"] = point1
df["col2"] = point2
df["col3"] = point3
df["col4"] = point4

plt.subplot(2, 2, 1)
plt.title("column_1")
plt.scatter(y, point1, c = "g", label = "column_1")


plt.subplot(2, 2, 2)
plt.title("column_2")
plt.scatter(y, point2, c = "b", label = "column_3")


plt.subplot(2, 2, 3)
plt.title("column_3")
plt.scatter(y, point3, c = "r", label = "column_3")


plt.subplot(2, 2, 4)
plt.title("column_4")
plt.scatter(y, point4, c = "b" , label = "column_4")




plt.savefig("Generate Test Dataset.jpg")


plt.show()