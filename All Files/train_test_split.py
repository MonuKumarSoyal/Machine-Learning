import imp
import numpy as np
from sklearn.model_selection import train_test_split

x, y = np.arange(10).reshape((5, 2)), range(5)

# print(x)
# print(list(y))

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.60, random_state = 50)

print(x_train)
print(x_test)
print(y_train)
print(y_test)

a = train_test_split(y, shuffle = False)

print(a)



