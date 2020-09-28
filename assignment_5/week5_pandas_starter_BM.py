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
#%%
# Esimation5
data.flow
# print(data.datetime[(data.flow >= rnge[0]) & (data.flow <= rnge[1])])

# list_2010 = []
# list_2011 = []
# list_2012 = []
# list_2013 = []
# list_2014 = []
# list_2015 = []
# list_2016 = []
# list_2017 = []
# list_2016 = []
# list_2017 = []
# list_2020 = []

# data.flow[(data.year >= 2010) & (data.year <= 2020) & (data.month == i)].mean]
#%%
# 1, 3, 5, 7, 8, 10, 12
for d in range(2010, 2020):
        fig1 = plt.figure()
        fig1.patch.set_facecolor('xkcd:mint green')
        plt.title('%d'%(d))
        plt.ylabel('flow')
        for i in (1, 3, 5, 7, 8, 10, 12):
                # print(i)
                # print(data.flow[(data.year == 2010) & (data.month == i)].mean)
                # print("\n")
                # data.flow[(data.year == 2010) & (data.month == i)]
                x = list(range(1, 32))
                plt.plot(x, (data.flow[(data.year == d) & (data.month == i)]))
                plt.xlabel('days in %i'%(i))
                plt.legend(['1', '3', '5', '7', '8', '10', '12'])
                # plt.savefig('graphs/flow_202009')

                
# x = list(range(1, 32))
# print(x)


# print(flow_data.size)
# print(flow_data.shape)
# flow_202009 = flow_data[11571:11585, 3]
# print(flow_202009)

# x = [6.,7,8,9,10,11,12,13,14,15,16,17,18,19]
# fig9 = plt.figure()
# fig9.patch.set_facecolor('xkcd:mint green')
# plt.plot(x, flow_202009)
# plt.xlabel('days in September 2020')
# plt.ylabel('flow')
# plt.legend()
# plt.savefig('graphs/flow_202009')

# %%
# 4, 6, 9, 11
for d in range(2010, 2020):
        fig2 = plt.figure()
        fig2.patch.set_facecolor('xkcd:mint green')
        plt.title('%d'%(d))
        plt.ylabel('flow')
        for i in (4, 6, 9, 11):
                # print(i)
                # print(data.flow[(data.year == 2010) & (data.month == i)].mean)
                # print("\n")
                # data.flow[(data.year == 2010) & (data.month == i)]
                x = list(range(1, 31))
                # print(x)
                plt.plot(x, (data.flow[(data.year == d) & (data.month == i)]))
                plt.xlabel('days in the month')
                plt.legend(['4', '6', '9', '11'])
                # plt.savefig('graphs/flow_202009')
# %%
# 2020

fig3 = plt.figure()
fig3.patch.set_facecolor('xkcd:mint green')
plt.title('2020')
plt.ylabel('flow')
for i in (1, 3, 5, 7, 8, 10, 12):
        # print(i)
        # print(data.flow[(data.year == 2010) & (data.month == i)].mean)
        # print("\n")
        # data.flow[(data.year == 2010) & (data.month == i)]
        x = list(range(1, 32))
        # print(x)
        plt.plot(x, (data.flow[(data.year == 2020) & (data.month == i)]))
        plt.xlabel('days in the month')
        plt.legend(['1', '3', '5', '7', '8', '10', '12'])
        # plt.savefig('graphs/flow_202009')


fig4 = plt.figure()
fig4.patch.set_facecolor('xkcd:mint green')
plt.title('2020'
plt.ylabel('flow')
for i in (4, 6, 9, 11):
        # print(i)
        # print(data.flow[(data.year == 2010) & (data.month == i)].mean)
        # print("\n")
        # data.flow[(data.year == 2010) & (data.month == i)]
        x = list(range(1, 31))
        # print(x)
        plt.plot(x, (data.flow[(data.year == 2020) & (data.month == i)]))
        plt.xlabel('days in the month')
        plt.legend(['4', '6', '9', '11'])
        # plt.savefig('graphs/flow_202009')
# %%
