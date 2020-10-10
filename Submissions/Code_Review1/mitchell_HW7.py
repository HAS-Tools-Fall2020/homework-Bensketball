# Baby's first autoregressive model
# How to build an AR model, plot it
# and use it for my perdiction

# By Benjamin Mitchell


# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime
import math


# %%
# Set the file name and path to where you have stored the data
# Make sure you are in the correct folder!!! ~BM
filename = 'streamflow_week7_temp.txt'
filepath = os.path.join('data', filename)
print(os.getcwd())
print(filepath)


# %%
# Turn on an off the line below to delete the pandas frame
# called 'Data' if you need to reset the data
# del(data)
# turn on the line above if 'data' needs to be reset
# turn of when 'data' does not exist

# Read the data into a pandas dataframe
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no', 'datetime', 'flow',
                            'code'], parse_dates=['datetime']
                    )

# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).day
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

# Aggregate flow values to weekly
flow_weekly = data.resample("W", on='datetime').mean()
# As an added bonus I am taking the log of the data
# becuase it fits the model better with all data included
flow_weekly.insert(2, 'log_flow', np.log(flow_weekly['flow']), True)
# print(flow_weekly)


# %%
# Building the autoregressive model
# You can learn more about the approach I'm following by walking 
# Through this tutorial
# https://realpython.com/linear-regression-in-python/

# Step 1: setup the arrays you will build your model on
# This is an autoregressive model so we will be building
# it based on the lagged timeseries
flow_weekly['log_flow_tm1'] = flow_weekly['log_flow'].shift(1)
flow_weekly['log_flow_tm2'] = flow_weekly['log_flow'].shift(2)

# Step 2: Pick what portion of the time series you want to use as training data
# here I'm grabbing the last 334 weeks
trainstart = 1300
trainend = 1600
print('trainstart', trainstart)
print('trainend', trainend)
# Note1 - dropping the first two weeks since they wont have lagged data
# to go with them
train = flow_weekly[trainstart:trainend][['log_flow',
                                          'log_flow_tm1', 'log_flow_tm2']]
test = flow_weekly[trainend:][['log_flow',
                               'log_flow_tm1', 'log_flow_tm2']]

# Step 3: Fit a linear regression model using sklearn
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

#altrenatievely you can calcualte this yourself like this: 
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
fig.savefig("graphs/Observed_Log(Flow)_All.png")


# 2. Time series of flow values with the x axis range limited
fig, ax = plt.subplots()
ax.plot(flow_weekly['log_flow'], label='full')
ax.plot(train['log_flow'], 'r:', label='training')
ax.set(title="Observed Log(Flow)", xlabel="Date", ylabel="Weekly Avg Log(Flow) [cfs]",
       yscale='log', xlim=[datetime.date(2000, 1, 26), datetime.date(2020,
                                                                     2, 1)])
ax.legend()
fig.savefig("graphs/Observed_Log(Flow)_Train.png")


# 3. Line  plot comparison of predicted and observed flows
fig, ax = plt.subplots()
ax.plot(train['log_flow'], color='grey', linewidth=2, label='observed')
ax.plot(train.index, q_pred_train, color='green', linestyle='--',
        label='simulated')
ax.set(title="Observed Log(Flow)", xlabel="Date", ylabel="Weekly Avg Flow [cfs]",
       yscale='log')
ax.legend()
fig.savefig("graphs/Observed_Log(Flow)_Sim.png")


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

# All graphs are saved in the folder called graphs.

# %%
# Finding the average of last weeks Flow, follwed by the predictions.
# y = mx + b
week_before = flow_weekly['log_flow'].tail(1)
print("Last weeks's flow was", math.exp(week_before),'!', '\n')
# Finding next weeks and next next weeks flows useing model and a fuction
def my_prediction(x):
        week_bef = week_before
        for i in range(1, x):
                print('week_%i:'%(i))
                log_pred = model.intercept_ + model.coef_ * week_bef
                pred = math.exp(log_pred)
                print(log_pred, '\n')
                print('prediction #%i:'%(i), pred, '\n')
                week_bef = log_pred

# The number chosen for the function named "my_prediction", was "3".
# This is becuase we want to predict next weeks flow and next next weeks flow.
my_prediction(3)
# %%
