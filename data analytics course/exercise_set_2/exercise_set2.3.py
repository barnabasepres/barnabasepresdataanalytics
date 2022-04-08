import numpy as np
import pandas as pd

df = df = pd.read_csv("data_salaries_india.csv")

heads = df.head(n=0)

# helper function for pandas to convert all salaries
# into yearly integer salaries
# I also change to eur, since it makes more sense to us
def yearly_wage_to_eur(row):
    # the last two characters determine if it's yearly, monthly, hourly
    period = row['Salary'][-2:]
    
    # remove all commas and combine all numbers
    number = int(''.join(filter(str.isdigit, row['Salary'])))
    
    # if it's hourly, the average work hours per year in India is
    # approximately 2117.01 (might change in future)
    if period == "hr":
        number = int(number * 2117.01)
    elif period == "mo":
        # months to year
        number = int(number * 12)
    
    
    # converting to eur
    number = round(number * 0.012, 1)
    
    # return the yearly salary in integer format
    return number

def cities_to_numbers(row):
    
    if row["Location"] == "Bangalore":
        city_number = 1
    elif row["Location"] == "Pune":
        city_number= 2
    elif row["Location"] == "Hyderabad":
        city_number = 3
    elif row["Location"] == "New Delhi":
        city_number = 4
    else:
        city_number = 5
    
    return city_number

df["Salary"] = df.apply(yearly_wage_to_eur, axis=1)

# most common job titles
job_title = df["Job Title"].value_counts()[::].sort_values(ascending=False).nlargest(3)

# most common companies
company_name = df["Company Name"].value_counts()[::].sort_values(ascending=False).nlargest(3)

# most common location
location = df["Location"].value_counts()[::].sort_values(ascending=False).nlargest(3)

data = df.value_counts()[::].sort_values(ascending=False)
data = data.describe()
data_hist = df.hist()

# based on the graph the data is balanced because the standard destribution is low

# based on my analysis I will remove the salaries higher than 200k due to being outliers
df = df[df['Salary'] < 200000]

# factorising the role column
label1, unique1 = pd.factorize(df['Role'], sort=False)

df['Factorised Roles'] = label1

correlations = df.corr(method="spearman")

# I will compare the location to the salary and see if there is any correlation
# first I create a function to convert each location to a number
city = df["Location"].value_counts()[::].sort_values(ascending=False)
df["City Number"] = df.apply(cities_to_numbers, axis=1)

city_salary_corr = df["Salary"].corr(df["City Number"])




















