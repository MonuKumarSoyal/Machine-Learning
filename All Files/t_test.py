import numpy as np
import pandas
import seaborn as sns
import scipy.stats as stats
import matplotlib.pyplot as plt
from scipy.stats import ttest_1samp


# 1st ----------------------------------------------------

# age =  np.array(range(1, 33))

# age_mean = age.mean()
# # print(age_mean)

# age_sample = np.random.choice(age, 10)

# # print(age_sample)

# t_test, p_value = ttest_1samp(age_sample, 16.5)

# print("The P value is :", p_value)
# print("The value of T-test is :", t_test)

# if p_value < 0.05 :
#     print("We are rejecting the null hypothesis")
# else:
#     print("We are accepting the null hypothesis")



# 2nd -------------------------------------------------------
# collage_ages = stats.poisson.rvs(loc = 18, mu = 35, size = 1500)
# classA_ages  = stats.poisson.rvs(loc = 18, mu = 30, size = 60)

# # print(classA_ages.mean())
# # print(collage_ages.mean())

# T_test, P_value = ttest_1samp(classA_ages, collage_ages.mean())

# print("The T-test for second Dataset :", T_test)
# print("The P-value for second Dataset :", P_value)

# if P_value < 0.05 :
#     print("We are rejecting the null hypothesis")
# else:
#     print("We are accepting the null hypothesis")

# 3rd -----------------------------------------------------------

# collage_ages = stats.poisson.rvs(loc = 18, mu = 35, size = 1500)
# classX_ages  = stats.poisson.rvs(loc = 18, mu = 30, size = 60)
# classY_ages  = stats.poisson.rvs(loc = 18, mu = 33, size = 60)


# T1_test, P1_value = stats.ttest_ind(classX_ages, classY_ages, equal_var = False)

# print("The T-test for second Dataset :", T1_test)
# print("The P-value for second Dataset :", P1_value)

# if P1_value < 0.05 :
#     print("We are rejecting the null hypothesis")
# else:
#     print("We are accepting the null hypothesis")


# 4th paired test    -------------------------------------------------------

# weight1 = []
# for i in range(1, 21):
#     weight1.append(i)

# weight2 = weight1 + stats.norm.rvs(scale = 5, loc = -1.25, size = 20)

# # print(weight1)
# # print(weight2)

# weight_df = pandas.DataFrame({"weight1":np.array(weight1), "weight2":np.array(weight2), "weight_difference":np.array(weight1)-np.array(weight2)})

# # print(weight_df)

# t3_test, p3_value = stats.ttest_rel(weight1, weight2)

# print("The value of t-test is :", t3_test)
# print("The value of p-value is :", p3_value)

# if p3_value < 0.05:
#     print("we are rejecting the null hypothesis")
# else:
#     print("we are accepting null hypothesis")

# 5th correlation ---------------------------------------------------

df = sns.load_dataset("iris")

# print(df.shape)
print(df.corr())
sns.pairplot(df)
plt.show()

