from scipy.stats import chi2

# 1(a) 1(b) one sample chi-sqaured test

# chi-square statistic
chi_stat = (85-75)**2/75 + (15-25)**2/25 # replace with your chi-square statistic
df = 1  # replace with your degrees of freedom

# calculate p-value
p_value = 1 - chi2.cdf(chi_stat, df)

print(f"Chi-square statistic: {chi_stat}")
print(f"Degrees of freedom: {df}")
print(f"P-value: {p_value}")


# 1(c) two proportion z-test
import numpy as np
from statsmodels.stats.proportion import proportions_ztest,  proportions_chisquare

count = np.array([85, 37])  # number of successes in each group
nobs = np.array([100, 50])  # number of trials in each group
z_stat, p_value = proportions_ztest(count, nobs)  # 'two-sided' for a two-tailed test
print(f'Z-statistic: {z_stat}\nP-value: {p_value}')


