# %% here is where each of us can work on testing scripts
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
import matplotlib.pyplot as plt
import matplotlib as mpl

# %% Streamflow section
# Get streamflow from website using getstrm_wbs function
station_id = '09506000'
#end_date = '2020-10-31'
end_date = '2020-11-07'  #yyyy-mm-dd

flow_data = getstrm_wbs(station_id,end_date)
flow_data_pd = add_yymmdd(flow_data)  # add year,month,day

# Aggregate flow values to weekly
flow_weekly = flow_data_pd.resample("W", on='datetime').mean()
# As an added bonus I am taking the natural log of the data
# because it fits the model better with all data included
flow_weekly.insert(2, 'log_flow', np.log(flow_weekly['flow']), True)

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
forecast_week_1_2 = ['2020-11-09','2020-11-16']
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
print(flow_predic_mono(b, m, 16, week_before_flow, forecast_week_1_thru_16), '\n')
print(flow_predic_poly(c, a, 16, week_before_flow, forecast_week_1_thru_16))


# Corr_fact1 = week_before_flow / AR1_output
# Corr_fact2 = week_before_flow / AR2_output
# %%

# my_prediction_1 = real_prediction(0, last_week_flow, None)*0.80
# my_prediction_2 = real_prediction(1, last_week_flow, last2_week_flow)*.84
# print("week 1 prediction outside AR=", my_prediction_1.round(1))
# print("week 2 prediction outside AR=", my_prediction_2.round(1))


# %% Function Lourdes
no_weeks = flow_weekly["log_flow"].size  # Number of weeks up to date
begining_week_ly = 25  # start week year 2020
ending_week_ly = 12  # end week year 2020
dates_weeks_range = flow_weekly['log_flow'][no_weeks-begining_week_ly:
                                           no_weeks-ending_week_ly]
# %% 
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

# %% Map Gauges II USGS stream gauge dataset:
# Download here:
# https://water.usgs.gov/GIS/metadata/usgswrd/XML/gagesII_Sept2011.xml#stdorder
# Reading it using geopandas
# file = os.path.join('../data', 'gagesII_9322_sept30_2011.shp')
file = os.path.join('../../data/', 'gagesII_9322_sept30_2011.shp')
gages = gpd.read_file(file)
gages_AZ=gages[gages['STATE']=='AZ']

# adding more datasets
# https://www.usgs.gov/core-science-systems/ngp/national-hydrography/access-national-hydrography-products
# https://viewer.nationalmap.gov/basic/?basemap=b1&category=nhd&title=NHD%20View

# Example reading in a geodataframe
# Watershed boundaries for the lower colorado
#filepath = '../data/Shape'
filepath = '../../data/map/Shape'
filename = 'WBDHU6.shp'
file = os.path.join(filepath,
                    filename)
HUC6 = gpd.read_file(file, layer="WBDHU6")
huc = gpd.read_file(file)
# %%
# plot the new layer we got:
#fig, ax = plt.subplots(figsize=(5, 5))
#HUC6.plot(ax=ax)
#ax.set_title("HUC Boundaries")
#plt.show()


# %%
# Add some points
# Central Avra Valley Storage and Recovery Project:  32.22877495, -110.97688412
# Stream gauge:  34.44833333, -111.7891667
point_list = np.array([[-111.240551, 32.231749],
                       [-111.7891667, 34.44833333]])
#make these into spatial features
point_geom = [Point(xy) for xy in point_list]
point_geom
# %%
#mape a dataframe of these points
point_df = gpd.GeoDataFrame(point_geom, columns=['geometry'],
                            crs=HUC6.crs)
# %%
#filepath = '../data/S_USA.AdministrativeForest'
filepath = '../../data/map/'
filename = 'S_USA.AdministrativeForest.shp'
file = os.path.join(filepath,
                    filename)
forest = gpd.read_file(file)
# print(forest.head())

forests_az = ['Kaibab National Forest', 'Prescott National Forest',
              'Coconino National Forest', 'Tonto National Forest',
              'Apache-Sitgreaves National Forests', 'Coronado National Forest']
forest_az=forest[forest['FORESTNAME'].isin(forests_az)]



# %%
#filepath = '../data/USA_Rivers_and_Streams-shp'
filepath = '../../data/map/USA_Rivers_and_Streams-shp'
filename = '9ae73184-d43c-4ab8-940a-c8687f61952f2020328-1-r9gw71.0odx9.shp'
file = os.path.join(filepath,
                    filename)
rivers_USA = gpd.read_file(file)
rivers_USA.columns
rivers_USA.State.unique()
rivers_AZ = rivers_USA[rivers_USA['State'] == 'AZ']

rivers_AZ.columns
rivers_AZ.Name.unique()
river_verde = rivers_AZ[rivers_AZ['Name'] == 'Verde River']

# %%
# Now trying to put it all together - adding our two points to the stream gagees
point_df.plot(ax=ax, color='r', marker='*')



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
