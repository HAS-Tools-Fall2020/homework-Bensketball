# %%
# Step 1 - Download the data from the USGS website
# https: // waterdata.usgs.gov/nwis/dv?referred_module = sw & site_no = 09506000
# For now you should save this file to the directory you put this script in

# %%
# Step 2 - Import the modules we will use
import pandas as pd
import matplotlib.pyplot as plt
import os

# %% 
# Step 3 - Read in the file in as dataframe
# You will need to change the filename to match what you downloaded
filename = 'streamflow_week2.txt'
filepath = os.path.join('data', filename)

data=pd.read_table(filepath, sep = '\t', skiprows=30, 
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )
data = data.set_index('datetime')


# %%
# Step 4 - Look at the data
data.shape  # See how many rows and columns the data has
data.head(6) # look at the first x rows of the data
data.tail(6) # look at the last  x rows  of the data

#data.iloc[350:360] # grab any subset of rows to look at
#data.flow[350:380]  # Grab a subset of just the flow data dat look at
print(data.loc['2019-08-31'])  #find a specific date1
print(data.loc['2018-08-31'])  #find a specific date1
print(data.loc['2017-08-31'])  #find a specific date1
print("\n")
print(data.loc['2019-09-07'])  #find a specific date2
print(data.loc['2018-09-07'])  #find a specific date2
print(data.loc['2017-09-07'])  #find a specific date2
print("\n")
print(data.loc['2019-09-14'])  #find a specific date3
print(data.loc['2018-09-14'])  #find a specific date3
print(data.loc['2017-09-14'])  #find a specific date3
print("\n")
print(data.loc['2019-09-21'])  #find a specific date4
print(data.loc['2018-09-21'])  #find a specific date4
print(data.loc['2017-09-21'])  #find a specific date4
print("\n")
print(data.loc['2019-09-28'])  #find a specific date5
print(data.loc['2018-09-28'])  #find a specific date5
print(data.loc['2017-09-28'])  #find a specific date5
print("\n")
print(data.loc['2019-10-05'])  #find a specific date6
print(data.loc['2018-10-05'])  #find a specific date6
print(data.loc['2017-10-05'])  #find a specific date6
print("\n")
print(data.loc['2019-10-12'])  #find a specific date7
print(data.loc['2018-10-12'])  #find a specific date7
print(data.loc['2017-10-12'])  #find a specific date7
print("\n")
print(data.loc['2019-10-19'])  #find a specific date8
print(data.loc['2018-10-19'])  #find a specific date8
print(data.loc['2017-10-19'])  #find a specific date8
print("\n")
print(data.loc['2019-10-26'])  #find a specific date9
print(data.loc['2018-10-26'])  #find a specific date9
print(data.loc['2017-10-26'])  #find a specific date9
print("\n")
print(data.loc['2019-11-02'])  #find a specific date10
print(data.loc['2018-11-02'])  #find a specific date10
print(data.loc['2017-11-02'])  #find a specific date10
print("\n")
print(data.loc['2019-11-09'])  #find a specific date11
print(data.loc['2018-11-09'])  #find a specific date11
print(data.loc['2017-11-09'])  #find a specific date11
print("\n")
print(data.loc['2019-11-16'])  #find a specific date12
print(data.loc['2018-11-16'])  #find a specific date12
print(data.loc['2017-11-16'])  #find a specific date12
print("\n")
print(data.loc['2019-11-23'])  #find a specific date13
print(data.loc['2018-11-23'])  #find a specific date13
print(data.loc['2017-11-23'])  #find a specific date13
print("\n")
print(data.loc['2019-11-30'])  #find a specific date14
print(data.loc['2018-11-30'])  #find a specific date14
print(data.loc['2017-11-30'])  #find a specific date14
print("\n")
print(data.loc['2019-12-07'])  #find a specific date15
print(data.loc['2018-12-07'])  #find a specific date15
print(data.loc['2017-12-07'])  #find a specific date15
print("\n")
print(data.loc['2019-12-14'])  #find a specific date16
print(data.loc['2018-12-14'])  #find a specific date16
print(data.loc['2017-12-14'])  #find a specific date16
# %%
# Step 5 - Make a plot of the data
# Change the numbers on the followin lines to plot a different portion of the data
ax=data.iloc[400:500]['flow'].plot(linewidth=0.5)
ax.set_ylabel('Daily Flow [cfs]')
ax.set_xlabel('Date')


# %%
