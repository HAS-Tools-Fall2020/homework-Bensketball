# here is where each of us can work on testing scripts
# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime
import os
import json  # conda install json
import urllib.request as req   # conda install urllib3
import urllib
import dataretrieval.nwis as nwis
from matplotlib import ticker

# %% Declare some functions

def week_prediction_all(flow, m, b, week_pred, end, prev_wks):
    """This function needs the stream flow data (flow), the intersection
    and slope values from AR model (m, b), and range of weeks you want to
    consider for weekly forecast (prev_wks and end). To indicate the week
    to forecast include the week number (week_pred = 1 or week_pred = 2)
    We are using the mean value of the data range you select - the standard
    deviation of the same data range """

    flow_range_value = flow['flow'][no_weeks-prev_wks:no_weeks-end].mean() - 0.3*flow[
                       'flow'][no_weeks - prev_wks:no_weeks-end].std()  # flow range mean - std
    prediction = (b + m * flow_range_value)*(1) # dryness of this year
    print('Week', week_pred, 'forecast using model is:', prediction)
    return prediction


def lin_reg_mod(test_weeks):
       """Linear Regression Model. 
       test weeks = streamflow laged 1 week (x values)
       test weeks = streamflow (y values) """
       reg_model = LinearRegression()
       x_val_model = test_weeks['flow_tm1'].values.reshape(-1, 1)  # Testing values
       y_val_model = test_weeks['flow'].values  # Testing values
       reg_model.fit(x_val_model, y_val_model)  # Fit linear model
       coeff_det = np.round(reg_model.score(x_val_model, y_val_model))  # r^2
       b = np.round(reg_model.intercept_, 2)  # Intercept
       m = np.round(reg_model.coef_, 2)  # Slope
       # Intercept and the slope (Final equation) y=mx+b
       print('Final equation is y = :', m[:1], 'x + ', b)
       return(b,m,reg_model,coeff_det)


# %% Streamflow section
# Set the file name and path to where you have stored the data
# adjust path as necessary

station_id = '09506000'
start_date = '1989-01-01'
end_date = '2020-10-31'

data_flow_day = nwis.get_record(sites=station_id, service='dv',
                          start=start_date, end=end_date,
                          parameterCd='00060')
data_flow_day.columns = ['flow', 'code', 'site_no']
# Rename columns
data_flow_day.index = data_flow_day.index.strftime('%Y-%m-%d')
# Make index a recognized datetime format instead of string
# data_flow_day.index = data_flow_day.index.strftime('%Y-%m-%d')
# %% Read the data into a pandas dataframe
# Expand dates to year month day
data_flow_day['datetime'] = pd.to_datetime(data_flow_day.index)
data_flow_day['year'] = pd.DatetimeIndex(data_flow_day['datetime']).year
data_flow_day['month'] = pd.DatetimeIndex(data_flow_day['datetime']).month
data_flow_day['day'] = pd.DatetimeIndex(data_flow_day['datetime']).day
data_flow_day['dayofweek'] = pd.DatetimeIndex(data_flow_day['datetime']).dayofweek

# %% AR model that you ended up building
# 1st step: Arrays to build model
wkly_flow_mean = data_flow_day.resample("W", on='datetime').mean()  # Flow to weekly
# %%
# This is the final graph function, to adjust for naming differences, the only
# change needed is to the parts before the for loop and defining data_mnth_i &
# flow_weekly_mnth_i in the for loop
data_mnth = data_flow_day[data_flow_day['month'] > 7]
flow_weekly_mnth = wkly_flow_mean[wkly_flow_mean['month'] > 7]
flow_quants_mnth = np.quantile(flow_weekly_mnth['flow'], q=[0, 0.5, 0.75, 0.9])
print('Method of flow quantiles for month ', mnth, ':', flow_quants_mnth)
print('For plots, Green is flow max above 75%, and Red is below 50%')
fig = plt.figure(figsize=(30, 10))
fig.subplots_adjust(hspace=0.6, wspace=0.4)
for i in range(1, 31):
    curr_yr = (i + 1990)
    flow_weekly_mnth_i = flow_weekly_mnth[flow_weekly_mnth['year'] ==
                                          curr_yr]
    data_mnth_i = data_mnth[data_mnth['year'] == curr_yr]
    ax = fig.add_subplot(3, 10, i)
    ax.set(title=("Streamflow in " + str(curr_yr)),
           ylabel="Weekly Avg Flow [cfs]", yscale='log')
    plt.xticks(rotation=45)
    if (np.max(flow_weekly_mnth_i['flow']) > flow_quants_mnth[2]):
        ax.plot(flow_weekly_mnth_i['flow'],
                '-g', label='Weekly Average')
        ax.plot(data_mnth_i['datetime'], data_mnth_i['flow'], color='grey',
                label='Daily Flow')
        ax.legend()
    elif (np.max(flow_weekly_mnth_i['flow']) < flow_quants_mnth[1]):
        ax.plot(flow_weekly_mnth_i['flow'],
                '-r', label='Weekly Average')
        ax.plot(data_mnth_i['datetime'], data_mnth_i['flow'], color='grey',
                label='Daily Flow')
        ax.legend()
    else:
        ax.plot(flow_weekly_mnth_i['flow'],
                '-b', label='Weekly Average')
        ax.plot(data_mnth_i['datetime'], data_mnth_i['flow'], color='grey', 
                label='Daily Flow')
        ax.legend()


# %%
