import numpy as np
from scipy import stats

# Step 1: Define the data and the theoretical mean
data = np.array([590, 748, 579, 544, 570, 598, 599, 673, 635, 714, 580, 565])  # 12 participants (ms)
theoretical_mean = 570  # theoretical mean (ms)

# Step 2: Perform a one-sample t-test
t_stat, p_value = stats.ttest_1samp(data, theoretical_mean)

# Step 3: Define the significance level
alpha = 0.05  # typically, the significance level is 0.05 or 5%, but this can be adjusted based on your study design

# Step 4: Decide whether to reject the null hypothesis
if p_value < alpha:
    print(f'Reject the null hypothesis that the mean is {theoretical_mean}.')
    print(f'The test statistic is {t_stat:.2f}, and the p-value is {p_value:.4f}.')
else:
    print(f'Fail to reject the null hypothesis that the mean is {theoretical_mean}.')
    print(f'The test statistic is {t_stat:.2f}, and the p-value is {p_value:.4f}.')

# Step 5 (Optional): Compute confidence interval
# Part A
# Data for the first cohort
data1 = np.array([590, 748, 579, 544, 570, 598, 599, 673, 635, 714, 580, 565])
standard_reaction_time = 570

# Calculating sample statistics
mean1 = np.mean(data1)
std_dev1 = np.std(data1, ddof=1)  # ddof=1 for sample standard deviation
n1 = len(data1)
sem1 = std_dev1 / np.sqrt(n1)  # standard error of the mean
df1 = n1 - 1  # degrees of freedom

# Performing the t-test
t_statistic1 = (mean1 - standard_reaction_time) / sem1
p_value1 = stats.t.sf(np.abs(t_statistic1), df1) * 2  # two-tailed p-value

# print("First cohort:")
# print("Sample mean:", mean1)
# print("Sample standard deviation:", std_dev1)
# print("T-statistic:", t_statistic1)
# print("Degrees of freedom:", df1)
# print("P-value:", p_value1)

# Part B
# Data for the second cohort
data2 = np.array([570, 535, 606, 572, 568, 600, 554, 575])

# Two-sample t-test
t_statistic2, p_value2 = stats.ttest_ind(data1, data2, equal_var=False)  # Assuming unequal variances

print("\nTwo-sample t-test results:")
print("T-statistic:", t_statistic2)
print("P-value (two-tailed):", p_value2)
print("P-value (one-tailed):", p_value2 / 2)  # one-tailed p-value