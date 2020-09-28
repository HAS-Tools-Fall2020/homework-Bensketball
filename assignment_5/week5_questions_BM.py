# Example solution for HW 4

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week5.txt'
filepath = os.path.join('data', filename)
print(os.getcwd())
print(filepath)

# filepath = '../Assignments/Solutions/data/streamflow_week1.txt'

# %%
#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# %%
# Sorry no more helpers past here this week, you are on your own now :)
# Hints - you will need the functions: describe, info, groupby, sort, head and tail.
# %%
# Question #1c

# type(data)
data.dtypes
# %%
# Question #2

data
# print(data)
# print(data[['datetime']])
flow = data["flow"]
# print(flow)
print('min:', '\n', flow.min())
print('mean:', '\n', flow.mean())
print('max:', '\n', flow.max())
print('std:', '\n', flow.std())
print('quantile:', '\n', flow.quantile())
# print(mean_data)

data['flow'].describe()

# %%
# Question #3

# print(data)
# mon_flow = data[["month","flow"]]
# print(mon_flow)
# data["datetime":[2]]
# print('min:', '\n', data.min())
# data_test = data[(datetime[:,1]==9), 3]
# data["datetime"]
i=0
# print(range(len(data)))
# print(data.flow[data.month == (12)].describe())
for i in range(1, 13):
        # print(data['flow'])
        print(i)
        print(data.flow[data.month == (i)].describe())

# %%
# Question 4

print(data.flow.nlargest(5))
print(data.flow.nlargest(5))
# print(data.month[data.flow.nsmallest(5)])
# print(data.datetime[data['flow'].nsmallest(5)])

# data
# %%
# Question 5

for i in range(1, 13):
        print(i)
        print(data.flow[data.month == (i)].nlargest(1))
for i in range(1, 13):
        print(i)
        print(data.flow[data.month == (i)].nsmallest(1))
# %%
