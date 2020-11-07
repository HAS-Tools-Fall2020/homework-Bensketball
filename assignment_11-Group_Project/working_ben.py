# here is where each of us can work on testing scripts
# Not Complete!

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


# %%
# Building a function for flow prediction outside of the AR model
def real_prediction(indexnumber, last_week_flow, last2_week_flow=None):
    ''''
    This function is prepping the linear regression model to be
    multiplied by a correction factor to bring it down to a more
    reasonable value for the forecast of week 1 and week 2.
    '''
    if indexnumber == 0 and last2_week_flow is None:
        rp = (model.intercept_ + model.coef_[indexnumber] * last_week_flow)
    if indexnumber == 1:
        rp = (model2.intercept_ + model2.coef_[0] * last_week_flow +
              model2.coef_[indexnumber] * last2_week_flow)
    if indexnumber != 0 and indexnumber != 1:
        print('The index number =', indexnumber, 'is not valid. Enter 0 or 1.')
    return rp


# %%
# Find the data you want to use from the USGS Website
# Site number for Verde River Near Camp Verde
site = '09506000'
start = '1989-01-01'
end = '2020-11-06'
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
# Expand the dates to year month day
flow_data['year'] = pd.DatetimeIndex(flow_data['datetime']).year
flow_data['month'] = pd.DatetimeIndex(flow_data['datetime']).month
flow_data['day'] = pd.DatetimeIndex(flow_data['datetime']).day
flow_data['dayofweek'] = pd.DatetimeIndex(flow_data['datetime']).dayofweek


# %%
# Aggregate flow values to weekly
flow_weekly = flow_data.resample("W", on='datetime').mean()
# As an added bonus I am taking the log of the data
# because it fits the model better with all data included
flow_weekly.insert(2, 'log_flow', np.log(flow_weekly['flow']), True)
# print(flow_weekly)
# print(type(flow_weekly['log_flow']))


# %%
# Step 1: setup the arrays you will build your model on
# This is an autoregressive model so we will be building
# it based on the lagged timeseries
shifts = [1, 2]
print('Shfiting the data by', shifts, 'weeks.')
flow_weekly['log_flow_tm1'] = flow_weekly['log_flow'].shift(shifts[0])
flow_weekly['log_flow_tm2'] = flow_weekly['log_flow'].shift(shifts[1])


#%%
# Step 2: Pick what portion of the time series you want to use as training data
# here I'm grabbing the weeks for my training period.
# LC nice  job defining these as variables -- one suggestion would be to move user defined variables to the top
trainstart = '2016-01-01'
trainend = '2020-12-31'
print('trainstart', trainstart)
print('trainend', trainend)

# Note1 - dropping the first two weeks since they wont have lagged data
# to go with them
train = flow_weekly[trainstart:trainend][['log_flow',
                                          'log_flow_tm1', 'log_flow_tm2']]
test = flow_weekly[trainend:][['log_flow',
                               'log_flow_tm1', 'log_flow_tm2']]

# print(train)
# %%
# Step 3a: Fit a linear regression model using sklearn, 1 variable
model1 = LinearRegression()
x1 = train['log_flow_tm1'].values.reshape(-1, 1)
y1 = train['log_flow'].values
model1.fit(x1, y1)
r_sq1 = model1.score(x1, y1)
print('coefficient of determination:', np.round(r_sq1, 7))
print('intercept:', np.round(model1.intercept_, 7))
print('slope:', np.round(model1.coef_, 7))


# %%
# Step 3b: Fit a linear regression model using sklearn, 2 variables
model2 = LinearRegression()
x2 = train[['log_flow_tm1', 'log_flow_tm2']]
y2 = train['log_flow']
model2.fit(x2, y2)
r_sq2 = model2.score(x2, y2)
print('coefficient of determination:', np.round(r_sq2, 7))
print('intercept:', np.round(model2.intercept_, 7))
print('slope:', np.round(model2.coef_, 7))


# %%
# Finding the Flows
week_before_flow = flow_weekly['log_flow'].tail(1)

# Corr_fact1 = week_before_flow / AR1_output
# Corr_fact2 = week_before_flow / AR2_output
# %%

# my_prediction_1 = real_prediction(0, last_week_flow, None)*0.80
# my_prediction_2 = real_prediction(1, last_week_flow, last2_week_flow)*.84
# print("week 1 prediction outside AR=", my_prediction_1.round(1))
# print("week 2 prediction outside AR=", my_prediction_2.round(1))
