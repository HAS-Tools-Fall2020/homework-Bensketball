# Start code for assignment 3
# this code sets up the lists you will need for your homework
# and provides some examples of operations that will be helpful to you

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week3.txt'
filepath = os.path.join('data', filename)
print(os.getcwd())
print(filepath)

# %%
# DON'T change this part -- this creates the lists you 
# should use for the rest of the assignment
# no need to worry about how this is being done now we will cover
# this in later sections. 

#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

#make lists of the data
flow = data.flow.values.tolist()
date = data.datetime.values.tolist()
year = data.year.values.tolist()
month = data.month.values.tolist()
day = data.day.values.tolist()

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

# %%
# Here is some starter code to illustrate some things you might like to do
# Modify this however you would like to do your homework. 
# From here on out you should use only the lists created in the last block:
# flow, date, yaer, month and day

# Calculating some basic properites
# print(min(flow))
# print(max(flow))
# print(np.mean(flow))
# print(np.std(flow))

# Making and empty list that I will use to store
# index values I'm interested in
# ilist = []

# Loop over the length of the flow list
# and adding the index value to the ilist
# if it meets some criteria that I specify
# for i in range(len(flow)):
#         if flow [i] > 600 and month[i] == 7:
#                 ilist.append(i)

# see how many times the criteria was met by checking the length
# of the index list that was generated
# print(len(ilist))

# Alternatively I could have  written the for loop I used 
# above to  create ilist like this
# ilist2 = [i for i in range(len(flow)) if flow[i] > 600 and month[i]==7]
# print(len(ilist2))

# Grabbing out the data that met the criteria
# This  subset of data is just the elements identified 
# in the ilist
# subset = [flow[j] for j in ilist]
# %%
# flow = data.flow.values.tolist()
# date = data.datetime.values.tolist()
# year = data.year.values.tolist()
# month = data.month.values.tolist()
# day = data.day.values.tolist()

# print(date)
# print(day)
# %%
# begin1 = '2017-09-06'
# end1 = '2017-09-12'
# begin2 = '2018-09-06'
# end2 = '2018-09-12'
# begin3 = '2019-09-06'
# end3 = '2019-09-12'
# begin4 = '2020-09-06'
# end4 = '2020-09-12'

days = [6, 7, 8, 9, 10, 11, 12]
yrs = [2017, 2018, 2019, 2020]
#  print(days[1])


yr2017 = []
flow2017 = []
for i in range(len(days)):
        d = days[i]
        p = '2017-09-%02d' %d
        yr2017.append(p)
# print(yr2017)

for i in range(len(yr2017)):
        val = date.index(yr2017[i])
        f = flow[val]
        flow2017.append(f)
        print (yr2017[i], end = " ")
        print(f)
print(flow2017)
print(min(flow2017))
print(max(flow2017))
print(np.mean(flow2017))
print(np.std(flow2017))
print("\n")


yr2018 = []
flow2018 = []
for i in range(len(days)):
        d = days[i]
        p = '2018-09-%02d' %d
        yr2018.append(p)
# print(yr2018)

for i in range(len(yr2018)):
        val = date.index(yr2018[i])
        f = flow[val]
        flow2018.append(f)
        print (yr2018[i], end = " ")
        print(flow[val])
print(flow2018)
print(min(flow2018))
print(max(flow2018))
print(np.mean(flow2018))
print(np.std(flow2018))
print("\n")


yr2019 = []
flow2019 = []
for i in range(len(days)):
        d = days[i]
        p = '2019-09-%02d' %d
        yr2019.append(p)
# print(yr2019)

for i in range(len(yr2019)):
        val = date.index(yr2019[i])
        f = flow[val]
        flow2019.append(f)
        print (yr2019[i], end = " ")
        print(flow[val])
print(flow2019)
print(min(flow2019))
print(max(flow2019))
print(np.mean(flow2019))
print(np.std(flow2019))
print("\n")


yr2020 = []
flow2020 = []
for i in range(len(days)):
        d = days[i]
        p = '2020-09-%02d' %d
        yr2020.append(p)
# print(yr2020)

for i in range(len(yr2020)):
        val = date.index(yr2020[i])
        f = flow[val]
        flow2020.append(f)
        print (yr2020[i], end = " ")
        print(flow[val])
print(flow2020)
print(min(flow2020))
print(max(flow2020))
print(np.mean(flow2020))
print(np.std(flow2020))


# print('begin1:')
# print(date.index(begin1))
# print('end1:')
# print(date.index(end1))
# date.index('2020-09-10')
# print(date.index('2020-09-10'))

# for i in range(len(date)): 
#     print (i, end = " ")
#     print (date[i])
# %%