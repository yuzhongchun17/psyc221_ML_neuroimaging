from scipy.stats import chi2,chisquare
from scipy.stats import chi2_contingency # Chi-squared test

# 2(a) 2(b) one sample chi-sqaured test
p = 2 # define problem
observed = [85,15]
if p == 1:
    expected = [50,50]
else:
    expected = [75,25]

# chi-square statistic & p-value
chi2, p_value = chisquare(observed,expected)
df = 1  # replace with your degrees of freedom

print(f"Chi-square statistic: {chi2}")
print(f"Degrees of freedom: {df}")
print(f"P-value: {p_value}")


# 2(c) two proportion z-test
import numpy as np
from statsmodels.stats.proportion import proportions_ztest,  proportions_chisquare

count = np.array([85, 37])  # number of successes in each group
nobs = np.array([100, 50])  # number of trials in each group
z_stat, p_value = proportions_ztest(count, nobs)  # 'two-sided' for a two-tailed test
print(f'Z-statistic: {z_stat}\nP-value: {p_value}')

#Chi-Squared Test - Tests whether two categorical variables are related or independent.
print("Null hypothesis: the classifier is the same across ages.")
age40_correct = 85
age40_wrong = 15
age60_correct = 37
age60_wrong = 13
table = [[age40_correct,age40_wrong ],[age60_correct, age60_wrong]]
print("contigency table:",table)
print("expected:",expected)
stat, p, dof, expected = chi2_contingency(table)   
print("chi2-stat:",stat)
print(f'p-value with Chi-Squared Test: {p:.4f}')
if p < 0.05:
    print("p<0.05 --> we reject the null hypothesis.")
else:
    print("p>0.05 --> we cannot reject the null hypothesis.")
