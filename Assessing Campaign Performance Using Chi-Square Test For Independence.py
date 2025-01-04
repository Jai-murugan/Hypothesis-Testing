#################################
# AB Testing - Task for ABC Grocery
################################

# Import required packages

import pandas as pd
from scipy.stats import chi2_contingency, chi2

# Importing data

campaign_data = pd.read_excel("grocery_database.xlsx", sheet_name = "campaign_data")

# Filtering data

campaign_data = campaign_data.loc[campaign_data["mailer_type"] != "Control"]

# Summmarize to get observed frequencies

observed_values = pd.crosstab(campaign_data["mailer_type"], campaign_data["signup_flag"])

mailer1_sigup_rate = 123 / (252 + 123)
mailer2_sigup_rate = 127 / (209 + 127)

print(mailer1_sigup_rate, mailer2_sigup_rate)

# State Hypothesis and acceptance rate

null_hypothesis = "There is no relationship betweeen mailer type and sigup rate. Thery are independent."
alternate_hypothesis = "There is relationship betweeen mailer type and sigup rate. Thery are not independent."
acceptance_criteria = 0.05

# Calculate expected frequencies & chi square statistics

chi2_statistic, p_value, dof, expected_values = chi2_contingency(observed_values, correction = False)
print(chi2_statistic, p_value)

# Find the critical value for our test

critical_value = chi2.ppf(1 - acceptance_criteria, dof)  # To calculate acceptance criteria formula
print(critical_value)

# Print the results (Chi square Statistics)

if chi2_statistic >= critical_value:
    print(f"As our chi- sqaure statistic of {chi2_statistic} is higher than our critical value of {critical_value} - we reject the null hypothesis, and conclude that: {alternate_hypothesis}")
else:
    print(f"As our chi- sqaure statistic of {chi2_statistic} is lower than our critical value of {critical_value} - we retain the null hypothesis, and conclude tha: {null_hypothesis}")
    
# Print the results (p-value)
if p_value <= acceptance_criteria:
    print(f"As our p_value of {p_value} is lower than our acceptance_criteria of {acceptance_criteria} - we reject the null hypothesis, and conclude that: {alternate_hypothesis}")
else:
    print(f"As our p_value of {p_value} is higher than our acceptance_criteria of {acceptance_criteria} - we retain the null hypothesis, and conclude tha: {null_hypothesis}")
    


















