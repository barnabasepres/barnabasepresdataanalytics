import numpy as np
import pandas as pd

df = df = pd.read_csv("purchases.csv")

heads = df.head(n=0)

#total price sum of the Purchase Order Number 018H2015
price_sum_rows = df[df["Purchase Order Number"] == "018H2015"]
total_price_sum = round(price_sum_rows["Total Price"].sum(), 2)


#  name and description of the purchased item with the 
# Purchase Order Number 3176273
name_description_row = df[df["Purchase Order Number"] == "3176273"]
name_description = name_description_row["Item Name"] + ", " + name_description_row["Item Description"]


# purchase data number from 2013
purchases_2013 = len(df[df['Purchase Date'].str.slice(start=6) == "2013"])


# 5 most common departments
departments = df["Department Name"].value_counts()[::].sort_values(ascending=False).nlargest(5)

# sort data by department name
df = df.sort_values(by="Department Name")





