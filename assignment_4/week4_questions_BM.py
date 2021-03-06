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
# Question #2

print(flow_data.dtype)
print(flow_data.size)
print(flow_data.shape)

# %%
# Question #3

flow_data9 = flow_data[(flow_data[:,1]==9), 3]
# print(flow_data9 > 50.7)
flow_data_t = np.count_nonzero(flow_data9 > 50.7)
print(flow_data_t)
print(flow_data9.shape)
print(type(flow_data_t))
print(type(flow_data9.shape[0]))
print((flow_data_t)/(flow_data9.shape[0]))

# %%
# Question #4

flow_data92000 = flow_data[(flow_data[:,1]==9) & (flow_data[:,0]<=2000), 3]
print(flow_data92000 > 50.7)
flow_data_t2 = np.count_nonzero(flow_data92000 > 50.7)
print(flow_data_t2)
print(flow_data92000.shape)
print(type(flow_data_t2))
print(type(flow_data92000.shape[0]))
print((flow_data_t2)/(flow_data92000.shape[0]))

flow_data92010 = flow_data[(flow_data[:,1]==9) & (flow_data[:,0]>=2010), 3]
print(flow_data92010 > 50.7)
flow_data_t3 = np.count_nonzero(flow_data92010 > 50.7)
print(flow_data_t3)
print(flow_data92010.shape)
print(type(flow_data_t3))
print(type(flow_data92010.shape[0]))
print((flow_data_t3)/(flow_data92010.shape[0]))

# %%
#Question #5?

flow_data9_1st = flow_data[(flow_data[:,3] < 200) & (flow_data[:,1]==9) & (flow_data[:,0]!=2020) & (flow_data[:,2]<=15), 3]
x_1st = flow_data[(flow_data[:,3] < 200) & (flow_data[:,1]==9) & (flow_data[:,0]!=2020) & (flow_data[:,2]<=15),2]
print(flow_data9_1st)
print(x_1st)

fig9_1st = plt.figure()
fig9_1st.patch.set_facecolor('xkcd:mint green')
plt.plot(x_1st, flow_data9_1st)
plt.xlabel('days in September')
plt.ylabel('flow(s)')
plt.legend()
plt.savefig('graphs/flow_data9_1st')


flow_data9_2nd = flow_data[(flow_data[:,3] < 200) & (flow_data[:,1]==9) & (flow_data[:,0]!=2020) & (flow_data[:,2]>=15), 3]
x_2nd = flow_data[(flow_data[:,3] < 200) & (flow_data[:,1]==9) & (flow_data[:,0]!=2020) & (flow_data[:,2]>=15),2]
print(flow_data9_2nd)
print(x_2nd)

fig9_1st = plt.figure()
fig9_1st.patch.set_facecolor('xkcd:mint green')
plt.plot(x_2nd, flow_data9_2nd)
plt.xlabel('days in September')
plt.ylabel('flow(s)')
plt.legend()
plt.savefig('graphs/flow_data9_2nd')
# %%
#Question 5!

flow_data9_1st = flow_data[(flow_data[:,3] < 200) & (flow_data[:,1]==9) & (flow_data[:,0]==2020) & (flow_data[:,2]<=15), 3]
x_1st = flow_data[(flow_data[:,3] < 200) & (flow_data[:,1]==9) & (flow_data[:,0]==2020) & (flow_data[:,2]<=15),2]
print(flow_data9_1st)
print(x_1st)

fig9_1st = plt.figure()
fig9_1st.patch.set_facecolor('xkcd:mint green')
plt.plot(x_1st, flow_data9_1st)
plt.xlabel('days in September 2020')
plt.ylabel('flow(s)')
plt.legend()
plt.savefig('graphs/flow_data92020_1st')


flow_data9_2nd = flow_data[(flow_data[:,3] < 200) & (flow_data[:,1]==9) & (flow_data[:,0]==2020) & (flow_data[:,2]>=15), 3]
x_2nd = flow_data[(flow_data[:,3] < 200) & (flow_data[:,1]==9) & (flow_data[:,0]==2020) & (flow_data[:,2]>=15),2]
print(flow_data9_2nd)
print(x_2nd)

fig9_1st = plt.figure()
fig9_1st.patch.set_facecolor('xkcd:mint green')
plt.plot(x_2nd, flow_data9_2nd)
plt.xlabel('days in September 2020')
plt.ylabel('flow(s)')
plt.legend()
plt.savefig('graphs/flow_data92020_2nd')
# %%
