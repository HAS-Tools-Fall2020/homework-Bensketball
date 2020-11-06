# Baby's second autoregressive model
# How to build an AR model, plot it
# and use it for my prediction

# By Benjamin Mitchell


# %%
# Import the modules we will use
import os
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from sklearn.linear_model import LinearRegression
import json 
import urllib.request as req
import urllib
# import eval_fuctions as ef
import dataretrieval.nwis as nwis
# could not find packages?


# %%
# Find the data you want to use from the USGS Website
# Site number for Verde River Near Camp Verde
site = '09506000'
start = '1989-01-01'
end = '2020-10-31' # Halloween!
url = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=" + site + \
      "&referred_module=sw&period=&begin_date=" + start + "&end_date=" + end

# Read the data from dictionary into a pandas dataframe
flow_data = pd.read_table(url, skiprows=30,
                              names=['agency_cd', 'site_no',
                                     'datetime', 'flow', 'code'],
                              parse_dates=['datetime'])

print(url)
# print(type(flow_data))
# print(flow_data)
# flow_data.keys()


# %%
# Turn on an off the line below to delete the pandas frame
# called 'Data' if you need to reset the data
# del(flow_data)
# turn on the line above if 'data' needs to be reset
# turn of when 'data' does not exist

# Expand the dates to year month day
flow_data['year'] = pd.DatetimeIndex(flow_data['datetime']).year
flow_data['month'] = pd.DatetimeIndex(flow_data['datetime']).month
flow_data['day'] = pd.DatetimeIndex(flow_data['datetime']).day
flow_data['dayofweek'] = pd.DatetimeIndex(flow_data['datetime']).dayofweek

# Aggregate flow values to weekly
flow_weekly = flow_data.resample("W", on='datetime').mean()
# As an added bonus I am taking the log of the data
# because it fits the model better with all data included
flow_weekly.insert(2, 'log_flow', np.log(flow_weekly['flow']), True)
# print(flow_weekly)
# print(type(flow_weekly['log_flow']))


# %%
# Building the autoregressive model
# You can learn more about the approach I'm following by walking 
# Through this tutorial
# https://realpython.com/linear-regression-in-python/

# Step 1: setup the arrays you will build your model on
# This is an autoregressive model so we will be building
# it based on the lagged timeseries
shifts = [1, 2]
print('Shfiting the data by', shifts, 'weeks.')
flow_weekly['log_flow_tm1'] = flow_weekly['log_flow'].shift(shifts[0])
flow_weekly['log_flow_tm2'] = flow_weekly['log_flow'].shift(shifts[1])

# Step 2: Pick what portion of the time series you want to use as training data
# here I'm grabbing the weeks for my training period.
# LC nice  job defining these as variables -- one suggestion would be to move user defined variables to the top
trainstart = '2016-01-01'
trainend = '2019-12-31'
print('trainstart', trainstart)
print('trainend', trainend)

# Note1 - dropping the first two weeks since they wont have lagged data
# to go with them
train = flow_weekly[trainstart:trainend][['log_flow',
                                          'log_flow_tm1', 'log_flow_tm2']]
test = flow_weekly[trainend:][['log_flow',
                               'log_flow_tm1', 'log_flow_tm2']]

# Step 3: Fit a linear regression model using sklearn
# LC- From here to line 98 would make a nice function :) 
model = LinearRegression()
x = train['log_flow_tm1'].values.reshape(-1, 1)
# See the tutorial to understand the reshape step here
y = train['log_flow'].values
model.fit(x, y)

# Step 3.5: Look at the results - r^2 values
r_sq = model.score(x, y)
print('coefficient of determination:', np.round(r_sq, 7))

# Print the intercept and the slope
print('intercept:', np.round(model.intercept_, 7))
print('slope:', np.round(model.coef_, 7))

# Step 4: Make a prediction with your model 
# Predict the model response for a  given flow value
q_pred_train = model.predict(train['log_flow_tm1'].values.reshape(-1,1))
q_pred_test = model.predict(test['log_flow_tm1'].values.reshape(-1,1))

#alternatively you can calcualte this yourself like this: 
q_pred = model.intercept_ + model.coef_ * train['log_flow_tm1']


# %%
# Here are some examples of things you might want to plot to get you started:

# 1. Timeseries of observed flow values
# Note that date is the index for the dataframe so it will
# automatically treat this as our x axis unless we tell it otherwise
fig, ax = plt.subplots()
ax.plot(flow_weekly['log_flow'], label='full')
ax.plot(train['log_flow'], 'r:', label='training')
ax.set(title="Observed Log(Flow)", xlabel="Date",
       ylabel="Weekly Avg Log(Flow) [cfs]",
       yscale='log')
ax.legend()
# An example of saving your figure to a file
fig.set_size_inches(6, 4.5)
fig.savefig("graphs/Observed_Log-Flow_All.png")


# 2. Time series of flow values with the x axis range limited
fig, ax = plt.subplots()
ax.plot(flow_weekly['log_flow'], label='full')
ax.plot(train['log_flow'], 'r:', label='training')
ax.set(title="Observed Log(Flow)", xlabel="Date", ylabel="Weekly Avg Log(Flow) [cfs]",
       yscale='log', xlim=[datetime.date(2000, 1, 26), datetime.date(2020,
                                                                     2, 1)])
ax.legend()
fig.savefig("graphs/Observed_Log-Flow_Train.png")


# 3. Line  plot comparison of predicted and observed flows
fig, ax = plt.subplots()
ax.plot(train['log_flow'], color='grey', linewidth=2, label='observed')
ax.plot(train.index, q_pred_train, color='green', linestyle='--',
        label='simulated')
ax.set(title="Observed Log(Flow)", xlabel="Date", ylabel="Weekly Avg Flow [cfs]",
       yscale='log')
ax.tick_params(axis='x', labelrotation=70)
ax.legend()
fig.savefig("graphs/Observed_Log-Flow_Sim.png")


# 4. Scatter plot of t vs t-1 flow with log log axes
fig, ax = plt.subplots()
ax.scatter(train['log_flow_tm1'], train['log_flow'], marker='p',
           color='blueviolet', label='obs')
ax.set(xlabel='Log(Flow) t-1', ylabel='Log(Flow) t', yscale='log', xscale='log')
ax.plot(np.sort(train['log_flow_tm1']), np.sort(q_pred_train), label='AR model')
ax.legend()
fig.savefig("graphs/AR_Log.png")


# 5. Scatter plot of t vs t-1 flow with normal axes
fig, ax = plt.subplots()
ax.scatter(train['log_flow_tm1'], train['log_flow'], marker='p',
           color='blueviolet', label='observations')
ax.set(xlabel='Log(Flow) t-1', ylabel='Log(Flow) t')
ax.plot(np.sort(train['log_flow_tm1']), np.sort(q_pred_train), label='AR model')
ax.legend()
fig.savefig("graphs/AR.png")

plt.show()

# All graphs are saved in the folder called 'graphs'.


# %%
# Finding the average of last weeks Flow, followed by the predictions.
# y = mx + b

# LC - Great function! You should define it at the top of your script though
# also it could use doc strings. 
# This is my fucntion:
# The inputs are the weeks to want to predict out,
# a known weekly average flow you want to start your predictions with,
# and a list of dates these prediction are for.
def my_predictions(weeks, week_b4, forecast_weeks):
       week_b4_i = week_b4
       my_pred_i = np.zeros((weeks, 1))
       for i in range(1, weeks+1):
              log_flow_pred_i = model.intercept_ + model.coef_ * week_b4_i
              flow_pred_i = math.exp(log_flow_pred_i)
              my_pred_i[i-1] = flow_pred_i
              week_b4_i = log_flow_pred_i
       my_prediction = pd.DataFrame(my_pred_i, index = forecast_weeks,
                              columns=["Predicted_Flows:"])
       print(my_prediction, '\n')

# Geting last weeks flow.
week_before_flow = flow_weekly['log_flow'].tail(1)
print("Last weeks's flow was", math.exp(week_before_flow),'cfs!', '\n')

# Defining prediction weeks for my 2 week predictions.
forecast_week_1_2 = ['2020-10-25','2020-11-01']

# Finding next weeks and next next weeks flows using model outputs
# and my function:
# The number chosen for the function named "my_prediction", was "3".
# This is because we want to predict next weeks flow and next next weeks flow.
my_predictions(2, week_before_flow, forecast_week_1_2)

# This is where I get make my 16-week predictions using the function:
# 'my_prediction'
# lc - Great job!

# These are the weeks we will be predicting for my 16 week prediction.
forecast_week_1_thru_16 = ['2020-08-22','2020-08-30','2020-09-06','2020-09-13',
                           '2020-09-20','2020-09-27','2020-10-04','2020-10-11',
                           '2020-10-18','2020-10-25','2020-11-01','2020-11-08',
                           '2020-11-15','2020-11-22','2020-11-29','2020-12-06']

# Getting the first weekly average flow of the semester!
week_start_flow = flow_weekly.loc['2020-08-16'][['log_flow']]
print("First flow of the semester was", math.exp(week_start_flow),'cfs!', '\n')

# Running the program for 16 weeks out.
my_predictions(16, week_start_flow, forecast_week_1_thru_16)


# %%
# Daymet Example:
# You can get Daymet data for a single pixle form this site:
# https: // daymet.ornl.gov/single-pixel/ 
# You can also experiment with their API Here: 
# https: // daymet.ornl.gov/single-pixel/api

# Example reading it as a json file
url = "https://daymet.ornl.gov/single-pixel/api/data?lat=34.9455&lon=-113.2549"  \
       "&vars=prcp&start=" + start + "&end=" + end + "&format=json"
response = req.urlopen(url)
# print(response, '\n')
print(url, '\n')
print(trainstart, trainend, '\n')

# Look at the kesy and use this to grab out the data
responseDict = json.loads(response.read())
responseDict['data'].keys()
year = responseDict['data']['year']
yearday = responseDict['data']['yday']
precip = responseDict['data']['prcp (mm/day)']

# make a dataframe from the data
precip_data = pd.DataFrame({'year': year,
                            'yearday': yearday, "precip": precip})


# %%
# 
precip_data["year"] = precip_data["year"].astype(str)
precip_data["yearday"] = precip_data["yearday"].astype(str)
precip_data["year"] = precip_data["year"].str.slice(0, -2)
precip_data["yearday"] = precip_data["yearday"].str.slice(0, -2)
precip_data["date"] = precip_data["year"].str.cat(precip_data["yearday"], sep = ' ')
precip_data['datetime'] = pd.to_datetime(precip_data.date, format='%Y %j')

# Create day of the week coulmn and resample for weeks
precip_data['dayofweek'] = pd.DatetimeIndex(precip_data['datetime']).dayofweek
weekly_precip_avg = precip_data.resample("W", on='datetime').mean()
weekly_precip_sum = precip_data.resample("W", on='datetime').sum()

# print(weekly_precip_avg)
# print(weekly_precip_sum)


# %%
# Creating precipitation data for above training period from the flow data
prd_avg = weekly_precip_avg[trainstart:trainend][['precip']]
prd_sum = weekly_precip_sum[trainstart:trainend][['precip']]

# print(prd_avg)
# print(prd_sum)

# Bar Graph for precipitation data(s)
fig, ax = plt.subplots()
ax.bar(prd_avg.index, prd_avg['precip'], color='red', width = 3, label='precip_avg')
ax.bar(prd_sum.index, prd_sum['precip'], color='blue', width = 3, label='precip_sum')
ax.set(title="Precipitation", xlabel="Date", ylabel="Weekly Precipitaion")
ax.tick_params(axis='x', labelrotation=70)
ax.legend()

fig.savefig("graphs/Observed_Flow_and_Precip_Bar.png")

#%%
# # Creating better flow data for above training period
train['flow'] = train.log_flow.apply(np.exp)
# print(type(q_pred_train))
# print(train)

# Line plot comparison of predicted and observed flows with yscale = 'log'
fig, axs = plt.subplots(2)
axs[0].plot(train['flow'], color='grey', linewidth=2, label='observed')
axs[0].plot(train.index, np.exp(q_pred_train), color='green', linestyle='--',
            label='simulated')
axs[0].set(title="Observed Flow", xlabel="Date",
           ylabel="Weekly Avg Flow [cfs]", yscale='log')
axs[0].tick_params(axis='x', labelrotation=70)
axs[0].legend()

# Line plot comparison of weekly average precipitation
# and weekly cumulative precipitation

axs[1].plot(prd_avg.index, prd_avg['precip'], color='red', linewidth=2,
            label='precip_avg')
axs[1].plot(prd_sum.index, prd_sum['precip'], color='blue', linewidth=2,
            label='precip_sum')
axs[1].set(title="Observed Precipitaion", xlabel="Date",
           ylabel="Weekly Precipitaion")
axs[1].tick_params(axis='x', labelrotation=70)
axs[1].legend()

fig.savefig("graphs/Observed_Log_Flow_and_Precip.png")

# %%
# Line plot comparison of predicted and observed flows with yscale = 'normal'
fig, axs = plt.subplots(2)
axs[0].plot(train['flow'], color='grey', linewidth=2, label='observed')
axs[0].plot(train.index, np.exp(q_pred_train), color='green', linestyle='--',
            label='simulated')
axs[0].set(title="Observed Flow", xlabel="Date",
           ylabel="Weekly Avg Flow [cfs]")
axs[0].tick_params(axis='x', labelrotation=70)
axs[0].legend()

# Line plot comparison of weekly average precipitation
# and weekly cumulative precipitation

axs[1].plot(prd_avg.index, prd_avg['precip'], color='red', linewidth=2,
            label='precip_avg')
axs[1].plot(prd_sum.index, prd_sum['precip'], color='blue', linewidth=2,
            label='precip_sum')
axs[1].set(title="Observed Precipitaion", xlabel="Date",
           ylabel="Weekly Precipitaion")
axs[1].tick_params(axis='x', labelrotation=70)
axs[1].legend()

fig.savefig("graphs/Observed_Flow_and_Precip.png")

# %%
# Line plot comparison of flow and precipitation
# Work in progress...
# an second y-axes would make more sense
fig, ax = plt.subplots()
fig.set_size_inches(20, 8)
ax.plot(train['flow'], color='grey', linewidth=2, label='observed')
ax.plot(train.index, np.exp(q_pred_train), color='green', linestyle='--',
        label='simulated')
ax.plot(prd_avg.index, prd_avg['precip'], color='red', linewidth=2,
        label='precip_avg')
ax.plot(prd_sum.index, prd_sum['precip'], color='blue', linewidth=2,
        label='precip_sum')
ax.set(title="Observed Weekly Flow & Precipitaion", xlabel="Date",
       ylabel="Weekly Avg Flow [cfs]")
ax.tick_params(axis='x', labelrotation=70)
ax.legend()

fig.savefig("graphs/Observed_Flow_and_Precip_combined.png")

# %%
