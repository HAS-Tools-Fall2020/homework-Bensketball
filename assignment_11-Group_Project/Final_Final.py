# %% Start

import os
import math
import numpy as np
import pandas as pd
import dataretrieval.nwis as nwis
import matplotlib.pyplot as plt
import datetime
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import json 
import urllib.request as req
import urllib
import eval_functions
import contextily as ctx
from shapely.geometry import Point
import geopandas as gpd
import fiona
import matplotlib as mpl

# %% Define trainning period
station_id = '09506000'  # Streamflow station
trainstart = '2016-01-01'  # Start date to train AR model
trainend = '2019-12-31'  # end date to train AR model
lag = 2  # No. of weeks to consider for lag 

# %% Streamflow section
# Get streamflow from website using getstrm_wbs function
end_date = '2020-11-07'  # yyyy-mm-dd (changes each week)

flow_data = getstrm_wbs(station_id,end_date)  # get strmflow data from website
flow_data_pd = add_yymmdd(flow_data)  # add year,month,day

flow_weekly = flow_data_pd.resample("W", on='datetime').mean()  # Add flow values to weekly
flow_weekly.insert(2, 'log_flow', np.log(flow_weekly['flow']), True)  # Natural log (fits the model better)

# %% Step 1: setup the arrays (to build the model)
# Autoregressive model (based on the lagged timeserie)

shifts = list(range(1, lag+1))
flow_weekly['log_flow_tm1'] = flow_weekly['log_flow'].shift(shifts[0])  # Lag 1week
flow_weekly['log_flow_tm2'] = flow_weekly['log_flow'].shift(shifts[1])  # Lag 2weeks

# %% Step 2: Pick time series portion to train model
print('Start training week: ', trainstart)
print('End training week: ', trainend)

# Dropping first two weeks (won't have lagged data) to go with them
train = flow_weekly[trainstart:trainend][['log_flow',
                                          'log_flow_tm1', 'log_flow_tm2']]
test = flow_weekly[trainend:][['log_flow',
                               'log_flow_tm1', 'log_flow_tm2']]

# %% Step 3 Fit AR model (linear regression model using sklearn, 1 var)
b, m, reg_model1, coeff_det1 = mono_reg_mod(train)

# %% Getting our two week predictions!
# Geting last weeks flow
week_before_flow = flow_weekly['log_flow'].tail(1)
print("Last weeks's flow was", math.exp(week_before_flow),'cfs!', '\n')

# Defining prediction weeks for our 2 week predic.
# These are the weeks we will be predicting for our 2 week predictions.
forecast_week_1_2 = ['2020-11-09','2020-11-16']
print(flow_predic_mono(b, m, 2, week_before_flow, forecast_week_1_2), '\n')

# %% 16 week forecast taking previous 12 weeks mean before week to forecast
no_weeks = flow_weekly["log_flow"].size  # Number of weeks up to date
begining_week_ly = 25  # start week year 2020
ending_week_ly = 12  # end week year 2020
dates_weeks_range = flow_weekly['log_flow'][no_weeks-begining_week_ly:
                                           no_weeks-ending_week_ly] 

wk_prd = np.zeros(16)
for i in range(1,17):
       wk_prd = week_prediction_all(flow=flow_weekly, m=m, b=b,
                                    prev_wks=begining_week_ly, end=ending_week_ly, week_pred=i)
       begining_week_ly = begining_week_ly+1
       ending_week_ly = ending_week_ly +1

# %% Plot streamflow

# This is the final graph function, to adjust for naming differences, the only
# change needed is to the parts before the for loop and defining data_mnth_i &
# flow_weekly_mnth_i in the for loop
data_mnth = flow_data_pd[flow_data_pd['month'] > 7]
flow_weekly_mnth = flow_weekly[flow_weekly['month'] > 7]
flow_quants_mnth = np.quantile(flow_weekly_mnth['flow'], q=[0, 0.5, 0.75, 0.9])
print('Method of flow quantiles for month ', data_mnth, ':', flow_quants_mnth)
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

# %% Get variables to map


# Map Gauges II USGS stream gauge dataset:
# https://water.usgs.gov/GIS/metadata/usgswrd/XML/gagesII_Sept2011.xml#stdorder
filepath = os.path.join('../../data')
state= 'AZ' #  state
gages_AZ = down_map_var(filepath,0,state)

# Watershed boundaries for the lower colorado
# https://viewer.nationalmap.gov/basic/?basemap=b1&category=nhd&title=NHD%20View
filepath_bd = '../../data/map/Shape'
HUC6 = down_map_var(filepath_bd,1,state)

# Forest
filepath_fr = '../../data/map'
forest = down_map_var(filepath_fr,2,state)
forests_az = ['Kaibab National Forest', 'Prescott National Forest',
              'Coconino National Forest', 'Tonto National Forest',
              'Apache-Sitgreaves National Forests', 'Coronado National Forest']
forest_az=forest[forest['FORESTNAME'].isin(forests_az)]

# Rivers and stream

filepath_rv = '../../data/map/USA_Rivers_and_Streams-shp'
rivers_AZ = down_map_var(filepath_rv,3,state)
rivers_AZ.columns
rivers_AZ.Name.unique()
river_verde = rivers_AZ[rivers_AZ['Name'] == 'Verde River']

# %% Add some points
# Stream gauge:  34.44833333, -111.7891667
point_list = np.array([[-111.7891667, 34.44833333]])
#make these into spatial features
point_geom = [Point(xy) for xy in point_list]
point_geom

#mape a dataframe of these points
point_df = gpd.GeoDataFrame(point_geom, columns=['geometry'],
                            crs=HUC6.crs)

# %%
# Adding a basemap, correcting crs to align on basemap
# This aligns the basemap with the other layers
points_project = point_df.to_crs(epsg=3857)
gages_AZ = gages_AZ.to_crs(epsg=3857)
HUC6_project = HUC6.to_crs(epsg=3857)
forest_az = forest_az.to_crs(epsg=3857)
river_verde = river_verde.to_crs(epsg=3857)
fig, ax = plt.subplots(figsize=(10, 10))
xlim = ([-1.261e7, -1.221e7])
ylim = ([3.91e6, 4.31e6])
ax.set_xlim(xlim)
ax.set_ylim(ylim)
gages_AZ.plot(column='DRAIN_SQKM', categorical=False,
              legend=True, markersize=35, label='AZ gages', marker='^', color='gold',
              ax=ax, zorder=3)
points_project.plot(ax=ax, color='crimson',markersize=500, marker='*', label='class-gage', zorder=5 )
HUC6_project.boundary.plot(ax=ax, color=None, label='Watershed boundaries',
                           edgecolor='black', linewidth=1.5, zorder=1)
forest_az.boundary.plot(ax=ax, label='National Forest Bounds', alpha= 0.5,
                             facecolor='darkgreen', edgecolor='forestgreen',
                             linewidth=1, zorder=2)
river_verde.plot(ax=ax, linewidth=3, color='goldenrod', zorder=4, label='Verde river')
ctx.add_basemap(ax=ax, url=ctx.providers.OpenTopoMap,)
ax.set_title('Verde River Watershed', fontsize=20)
ax.legend(loc='upper right', fontsize=13)



plt.show()

# %%