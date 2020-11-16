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
from sklearn import metrics
import json 
import urllib.request as req
import urllib
# import eval_fuctions as ef
import dataretrieval.nwis as nwis


# %% Declare all our functions

# Building a function for our Linear Regression Model
def mono_reg_mod(test_weeks):
    """Linear Regression Model data being offset only once.
    test weeks = natural log streamflow laged by 1 week (x values)
    test weeks = natural log streamflow (y values)
    """
    reg_model = LinearRegression()
    x_val_model1 = test_weeks['log_flow_tm1'].values.reshape(-1, 1)  # Testing values
    y_val_model1 = test_weeks['log_flow'].values  # Testing values
    reg_model.fit(x_val_model1, y_val_model1)  # Fit linear model
    coeff_det1 = np.round(reg_model.score(x_val_model1, y_val_model1), 7)  # r^2
    b = np.round(reg_model.intercept_, 7)  # Intercept
    m = np.round(reg_model.coef_, 7)  # Slope
    print('coefficient of determination:', np.round(coeff_det1, 7))
    # Intercept and the slope (Final equation) y= mx + b
    print('Final equation is y1 = :', m[:1], 'x + ', b)
    return(b,m,reg_model,coeff_det1)

# Building a function for our Linear Regression Model
def poly_reg_mod(test_weeks):
    """Linear Regression Model with data being offset on two separate occasions.
    test weeks = natural log of streamflow laged by 1 & 2 weeks (x values)
    test weeks = natural log of streamflow (y values)
    """
    poly_model = LinearRegression()
    x_val_model2 = test_weeks[['log_flow_tm1', 'log_flow_tm2']]  # Testing values
    y_val_model2 = test_weeks['log_flow']  # Testing values
    poly_model.fit(x_val_model2, y_val_model2)  # Fit linear model
    coeff_det2 = np.round(poly_model.score(x_val_model2, y_val_model2), 7)  # r^2
    c = np.round(poly_model.intercept_, 7)  # Intercept
    a = np.round(poly_model.coef_, 7)  # Slope(s)
    print('coefficient of determination:', np.round(coeff_det2, 7))
    # Intercept and the slope (Final equation) y= a1*x1 + a2*x2 + c
    print('Final equation is y2 = :', a[:1], 'x1 + ', a[1:2], 'x2 + ', c)
    return(c,a,poly_model,coeff_det2)

# Building a function for flow prediction outside of the AR model
def real_prediction(indexnumber, last_week_flow, last2_week_flow=None):
    """This function is prepping the linear regression model to be
    multiplied by a correction factor to bring it down to a more
    reasonable value for the forecast of week 1 and week 2.
    """
    if indexnumber == 0 and last2_week_flow is None:
        rp = (model.intercept_ + model.coef_[indexnumber] * last_week_flow)
    if indexnumber == 1:
        rp = (model2.intercept_ + model2.coef_[0] * last_week_flow +
              model2.coef_[indexnumber] * last2_week_flow)
    if indexnumber != 0 and indexnumber != 1:
        print('The index number =', indexnumber, 'is not valid. Enter 0 or 1.')
    return rp

# Building a function to produce our two week flow predictions
# using linaral model1 with only one data offsets
def flow_predic_mono(b, m, num_of_weeks, week_b4, forecast_weeks):
    """This function produces predicted flow values using coefficients provided
    by an Liner Autoregressive Model with only one data offset.
    'b' is the y-intersept and 'm' is the slope.
    'num_of_weeks' is how many weeks you would like to loop the model for.
    'week_b4' is the natural log flow of a known flow and
    'forecast_weeks' is a list of dates that you are predicting for.
    """
    week_b4_i = week_b4
    pred_i = np.zeros((num_of_weeks, 1))
    for i in range(1, num_of_weeks + 1):
            log_flow_pred_i = b + m[:1] * week_b4_i
            flow_pred_i = math.exp(log_flow_pred_i)
            pred_i[i-1] = flow_pred_i
            week_b4_i = log_flow_pred_i
    flow_predictions_lin = pd.DataFrame(pred_i, index = forecast_weeks,
                                        columns=["Predicted_Flows_Lin:"])
    return flow_predictions_lin

# Building a function to produce our two week flow predictions
# using linaral model2 with multiple data offsets
def flow_predic_poly(c, a, num_of_weeks, week_b4, forecast_weeks):
    """This function produces predicted flow values using coefficients provided
    by an Liner Autoregressive Model with two different data offsets.
    'c' is the y-intersept and 'a' is a list of two slopes provided by the model.
    'num_of_weeks' is how many weeks you would like to loop the model for.
    'week_b4' is the natural log flow of a known flow and
    'forecast_weeks' is a list of dates that you are predicting for.
    """
    week_b4_i = week_b4
    pred_i = np.zeros((num_of_weeks, 1))
    for i in range(1, num_of_weeks + 1):
            log_flow_pred_i = c + a[1] * week_b4_i + a[0] * (week_b4_i)
            flow_pred_i = math.exp(log_flow_pred_i)
            pred_i[i-1] = flow_pred_i
            week_b4_i = log_flow_pred_i
    flow_predictions_poly = pd.DataFrame(pred_i, index = forecast_weeks,
                                         columns=["Predicted_Flows_Poly:"])
    return flow_predictions_poly

# Building a function to produce our two week flow predictions
def week_prediction_all(flow, m, b, week_pred, end, prev_wks):
    """This function needs the stream flow data (flow), the intersection
    and slope values from AR model (m, b), and range of weeks you want to
    consider for weekly forecast (prev_wks and end). To indicate the week
    to forecast include the week number (week_pred = 1 or week_pred = 2)
    We are using the mean value of the data range you select - the standard
    deviation of the same data range
    """
    flow_range_value = flow['flow'][no_weeks-prev_wks:no_weeks-end].mean() - 0.3*flow[
                       'flow'][no_weeks - prev_wks:no_weeks-end].std()  # flow range mean - std
    prediction = (b + m * flow_range_value)*(1) # dryness of this year
    print('Week', week_pred, 'forecast using model is:', prediction)
    return prediction


# %%
# Find the data you want to use from the USGS Website
# Site number for Verde River Near Camp Verde
site = '09506000'
start = '1989-01-01'
end = '2020-11-14' # Saturday before perdiction
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
# As an added bonus I am taking the natural log of the data
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
flow_weekly['log_flow_tm1'] = flow_weekly['log_flow'].shift(shifts[0]) # Flow lag 1week
flow_weekly['log_flow_tm2'] = flow_weekly['log_flow'].shift(shifts[1]) # Flow lag 2weeks


#%%
# Step 2: Pick what portion of the time series you want to use as training data
# here I'm grabbing the weeks for our training period.
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

# print(train)
# print(test)
# %%
# Step 3a: Fit a linear regression model using sklearn, 1 variable
# model1 = LinearRegression()
# x1 = train['log_flow_tm1'].values.reshape(-1, 1)
# y1 = train['log_flow'].values
# model1.fit(x1, y1)
# r_sq1 = model1.score(x1, y1)
# print('coefficient of determination:', np.round(r_sq1, 7))
# print('slope:', np.round(model1.coef_, 7))
# print('intercept:', np.round(model1.intercept_, 7))


# %%
# Step 3b: Fit a linear regression model using sklearn, 2 variables
# model2 = LinearRegression()
# x2 = train[['log_flow_tm1', 'log_flow_tm2']]
# y2 = train['log_flow']
# model2.fit(x2, y2)
# r_sq2 = model2.score(x2, y2)
# print('coefficient of determination:', np.round(r_sq2, 7))
# print('slope:', np.round(model2.coef_, 7))
# print('intercept:', np.round(model2.intercept_, 7))


# %%
# Step 3a: Fit a linear regression model using sklearn, 1 variable
b, m, reg_model1, coeff_det1 = mono_reg_mod(train)
# Step 3b: Fit a linear regression model using sklearn, 2 variables
c, a, reg_model2, coeff_det2 = poly_reg_mod(train)


# %%
# Getting our two week predictions!
# Geting last weeks flow
week_before_flow = flow_weekly['log_flow'].tail(1)
print("Last weeks's flow was", math.exp(week_before_flow),'cfs!', '\n')

# Defining prediction weeks for our 2 & 16 week predictions.
# These are the weeks we will be predicting for our 2 & 16 week predictions.
forecast_week_1_2 = ['2020-11-16','2020-11-23']
forecast_week_1_thru_16 = ['2020-08-22','2020-08-30','2020-09-06','2020-09-13',
                           '2020-09-20','2020-09-27','2020-10-04','2020-10-11',
                           '2020-10-18','2020-10-25','2020-11-01','2020-11-08',
                           '2020-11-15','2020-11-22','2020-11-29','2020-12-06']

# Finding next weeks and next next weeks flows using both models outputs
# The number chosen for the function named "flow_predic_mono" and "flow_predic_poly",
#  was "2". This is because we want to predict next weeks flow and next next weeks flow.
print(flow_predic_mono(b, m, 2, week_before_flow, forecast_week_1_2), '\n')
print(flow_predic_poly(c, a, 2, week_before_flow, forecast_week_1_2))


# %%
# Testing models for 16 week predictions
# Getting the first weekly average flow of the semester!
week_start_flow = flow_weekly.loc['2020-08-16'][['log_flow']]
print("First flow of the semester was", math.exp(week_start_flow),'cfs!', '\n')

# Running the functions for 16 weeks out
print(flow_predic_mono(b, m, 16, week_start_flow, forecast_week_1_thru_16), '\n')
print(flow_predic_poly(c, a, 16, week_start_flow, forecast_week_1_thru_16))


# Corr_fact1 = week_before_flow / AR1_output
# Corr_fact2 = week_before_flow / AR2_output
# %%

# my_prediction_1 = real_prediction(0, last_week_flow, None)*0.80
# my_prediction_2 = real_prediction(1, last_week_flow, last2_week_flow)*.84
# print("week 1 prediction outside AR=", my_prediction_1.round(1))
# print("week 2 prediction outside AR=", my_prediction_2.round(1))

# %%
