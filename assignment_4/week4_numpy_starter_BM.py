# Starter code for Homework 4

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week4.txt'
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

# Make a numpy array of this data
flow_data = data[['year', 'month','day', 'flow']].to_numpy()

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

# %%
# Starter Code
# Count the number of values with flow > 600 and month ==7
flow_count = np.sum((flow_data[:,3] > 600) & (flow_data[:,1]==7))

# Calculate the average flow for these same criteria 
flow_mean = np.mean(flow_data[(flow_data[:,3] > 600) & (flow_data[:,1]==7),3])

print("Flow meets this critera", flow_count, " times")
print('And has an average value of', flow_mean, "when this is true")

# Make a histogram of data
# Use the linspace  funciton to create a set  of evenly spaced bins
mybins = np.linspace(0, 1000, num=15)
# another example using the max flow to set the upper limit for the bins
#mybins = np.linspace(0, np.max(flow_data[:,3]), num=15) 
#Plotting the histogram
plt.hist(flow_data[:,3], bins = mybins)
plt.title('Streamflow')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')

# Get the quantiles of flow
# Two different approaches ---  you should get the same answer
# just using the flow column
flow_quants1 = np.quantile(flow_data[:,3], q=[0,0.1, 0.5, 0.9])
print('Method one flow quantiles:', flow_quants1)
# Or computing on a colum by column basis 
flow_quants2 = np.quantile(flow_data, q=[0,0.1, 0.5, 0.9], axis=0)
# and then just printing out the values for the flow column
print('Method two flow quantiles:', flow_quants2[:,3])
# %%
# Starting 'my code'
# print(data)
# print(flow_count)
print(flow_data)
print(flow_mean)
print(flow_data.size)
print(flow_data.shape)
# %%
#Testing
#take flows and compare similar years
# flow_year = flow_data[:,0]
# flow_month = flow_data[:,1]
# flow_flow = flow_data[:,3]
# print(flow_year)
# flow_data2 = np.flow_data(flow_data[:,0]flow_data[:,1],
# test1 = np.append(flow_data[:,0], flow_data[:,1])
# print(test1)

# del(test1)# %%

# for flow_data[:,1] == 9 in flow_data:
#     print(flow_data[:,2])

# for i in flow_data:
#         if flow_data.any[:,1] == 9:
#                 print(flow_data[:,3])

# year = 

# flow_data2 = flow_data[(flow_data[:,1]==9), 3]
# yr1 = flow_data2[1:30]

# print(flow_data2)

# flow_data.index(flow_data[:,1] == 9)

# print(flow_data[:,1] == 9 for flow_data[:,3])

# %%
# Monday Guess!
print(flow_data.size)
print(flow_data.shape)
flow_202009 = flow_data[11571:11585, 3]
# print(flow_202009)

x = [6.,7,8,9,10,11,12,13,14,15,16,17,18,19]
fig9 = plt.figure()
fig9.patch.set_facecolor('xkcd:mint green')
plt.plot(x, flow_202009)
plt.xlabel('days in September 2020')
plt.ylabel('flow')
plt.legend()
plt.savefig('graphs/flow_202009')
#%%
# Make a histogram of data for month 9
flow_data9 = flow_data[(flow_data[:,3] < 400) & (flow_data[:,1]==9), 3]
mean9 = np.mean(flow_data9)
print(mean9)
# Use the linspace  funciton to create a set  of evenly spaced bins
mybins = np.linspace(0, 1000, num=25)
# another example using the max flow to set the upper limit for the bins
#mybins = np.linspace(0, np.max(flow_data[:,3]), num=15) 
#Plotting the histogram
fig9 = plt.figure()
fig9.patch.set_facecolor('xkcd:mint green')
plt.hist(flow_data9[:], bins = mybins)
plt.title('Streamflow_9')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')
plt.savefig('graphs/g9')
# %%
# Make a histogram of data for month 10
flow_data10 = flow_data[(flow_data[:,3] < 400) & (flow_data[:,1]==10), 3]
mean10 = np.mean(flow_data10)
print(mean10)
# Use the linspace  funciton to create a set  of evenly spaced bins
mybins = np.linspace(0, 1000, num=25)
# another example using the max flow to set the upper limit for the bins
#mybins = np.linspace(0, np.max(flow_data[:,3]), num=15) 
#Plotting the histogram
fig10 = plt.figure()
fig10.patch.set_facecolor('xkcd:mint green')
plt.hist(flow_data10[:], bins = mybins)
plt.title('Streamflow_10')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')
plt.savefig('graphs/g10')
# %%
# %%
# Make a histogram of data for month 11
flow_data11 = flow_data[(flow_data[:,3] < 400) & (flow_data[:,1]==11), 3]
mean11 = np.mean(flow_data11)
print(mean11)
# Use the linspace  funciton to create a set  of evenly spaced bins
mybins = np.linspace(0, 1000, num=25)
# another example using the max flow to set the upper limit for the bins
#mybins = np.linspace(0, np.max(flow_data[:,3]), num=15) 
#Plotting the histogram
fig11 = plt.figure()
fig11.patch.set_facecolor('xkcd:mint green')
plt.hist(flow_data11[:], bins = mybins)
plt.title('Streamflow_11')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')
plt.savefig('graphs/g11')
# %%
# Make a histogram of data for month 12
flow_data12 = flow_data[(flow_data[:,3] < 400) & (flow_data[:,1]==12), 3]
mean12 = np.mean(flow_data12)
print(mean12)
# Use the linspace  funciton to create a set  of evenly spaced bins
mybins = np.linspace(0, 1000, num=25)
# another example using the max flow to set the upper limit for the bins
#mybins = np.linspace(0, np.max(flow_data[:,3]), num=15) 
#Plotting the histogram
fig12 = plt.figure()
fig12.patch.set_facecolor('xkcd:mint green')
plt.hist(flow_data12[:], bins = mybins)
plt.title('Streamflow_12')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')
plt.savefig('graphs/g12')
# %%
