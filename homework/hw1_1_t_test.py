import numpy as np
from scipy import stats


# Step 1: Define the sample and the theoretical mean
sample = np.array([590, 748, 579, 544, 570, 598, 599, 673, 635, 714, 580, 565])  # sample observation, 12 participants
theoretical_mean = 570  # population mean (ms)

sample_mean = np.mean(sample)
std_dev = np.std(sample, ddof=1)

# Step 2: Perform a one-sample t-test
t_stat, p_value = stats.ttest_1samp(sample, theoretical_mean)
print("mean:",sample_mean, "t_stat:",t_stat, "p-value:",p_value,"std dev:",std_dev)

# Step 3: Define the significance level
alpha = 0.05  # typically, the significance level is 0.05 or 5%, but this can be adjusted based on your study design

# Step 4: Decide whether to reject the null hypothesis
if p_value < alpha:
    print(f'Reject the null hypothesis that the mean is {theoretical_mean}.')
    print(f'The test stat is {t_stat:.2f}, and the p-value is {p_value:.4f}.')
else:
    print(f'Fail to reject the null hypothesis that the mean is {theoretical_mean}.')
    print(f'The test stat is {t_stat:.2f}, and the p-value is {p_value:.4f}.')

# Part B
# sample for the second cohort
sample2 = np.array([570, 535, 606, 572, 568, 600, 554, 575])

# Perform Levene's test to decided whether to use standard t-test (equal_var = true) or welch's t-test (equal_var = false)
statistic, p_value = stats.levene(sample, sample2)

print(f"Test statistic: {statistic}")
print(f"P-value: {p_value}")

# Interpret the p-value
alpha = 0.05
if p_value < alpha:
    print("Variances are unequal (we reject the null hypothesis of equal variances)")
else:
    print("Variances are equal (we fail to reject the null hypothesis of equal variances)")

# Two-sample t-test
t_stat2, p_value2 = stats.ttest_ind(sample, sample2)  

print("\nTwo-sample t-test results:")
print("T-stat:", t_stat2)
print("P-value (two-tailed):", p_value2)
print("P-value (one-tailed):", p_value2 / 2)  # one-tailed p-value

# Decide whether to reject the null hypothesis
if p_value2 < alpha:
    print(f'Reject the null hypothesis that the mean reaction time is different for two cohorts')
    print(f'The test stat is {t_stat2:.2f}, and the p-value is {p_value2:.4f}.')
else:
    print(f'Fail to reject the null hypothesis that the mean reaction time is the same for two cohorts.')
    print(f'The test stat is {t_stat2:.2f}, and the p-value is {p_value2:.4f}.')