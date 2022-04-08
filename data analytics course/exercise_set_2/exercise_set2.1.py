import numpy as np
import pandas as pd

df = df = pd.read_csv("loans.csv")


# remove the customer ID column
df = df.drop("Customer ID", axis=1)

#print the head of the data
heads = df.head(n=0)

# Remove rows from the data that have a too large of a loan
df = df[df['Current Loan Amount'].notnull()]
df['Current Loan Amount'] = df['Current Loan Amount'].astype('int64')
df = df[df["Current Loan Amount"] < 99999999]

# remove rows that have the annual income as NaN
df['Annual Income'].fillna((df['Annual Income'].mean()), inplace=True)

#Get the average Current Loan Amount (I use .describe here so that 
#I get a little more informaiton out of the dataframe)
current_loan_amount_avg = df["Current Loan Amount"].describe()

#Get the highest and lowest Annual Income in the dataset
df['Annual Income'] = df['Annual Income'].astype('int64')
highest_income = df.nlargest(1, "Annual Income")
lowest_income = df.nsmallest(1, "Annual Income")

#  Get the Home Ownership value of the
# Loan ID = bbf87a87-22cd-4d10-bd9b-7a9cc1b6e59d
home_ownership_value_row = df[df['Loan ID'] == "bbf87a87-22cd-4d10-bd9b-7a9cc1b6e59d"]
home_ownership_value_single = home_ownership_value_row.iloc[0]["Home Ownership"]


# Get the Actual Annual Income of the loan with the ID =
# 76fa89b9-e6a8-49af-afa1-8151315aba8e
df["Actual Annual Income"] = df["Annual Income"] - (12 * df["Monthly Debt"])

annual_income_row = df[df["Loan ID"] == "76fa89b9-e6a8-49af-afa1-8151315aba8e"]

actual_annual_income = annual_income_row.iloc[0]["Actual Annual Income"]

#Get the Loan ID of the loan with the smallest Actual Annual Income
smallest_actual_income_row = df.nsmallest(1, "Actual Annual Income")
smallest_actual_income_id = smallest_actual_income_row.iloc[0]["Loan ID"]

# How many loans are "Long term"?
long_term_loan_filter = df[df["Term"] == "Long Term"]
long_term_loan_filter_number = len(long_term_loan_filter['Term'])

#How many loaners have more than 1 bankruptcy?
bankruptcy = df[df["Bankruptcies"] > 1]
bankruptcy_number = len(bankruptcy["Bankruptcies"])

#How many Short Term loans are for Home Improvements?
stl = df[df["Term"] == "Short Term"]
stl_for_home_impr = stl[stl["Purpose"] == "Home Improvements"]
stl_for_home_impr_number = len(stl_for_home_impr["Purpose"])

#How many unique loan purposes are there?
df["Purpose"].hist()
most_frequent_purposes = df['Purpose'].value_counts()[::].sort_values(ascending=False)
unique_purposes_number = most_frequent_purposes.nsmallest(5)

most_frequent_purposes_top3 = most_frequent_purposes.nlargest(3)


#correlations
corr = df.corr()
correlation1 = df["Annual Income"].corr(df["Number of Open Accounts"])
correlation2 = df["Number of Credit Problems"].corr(df["Bankruptcies"])


























