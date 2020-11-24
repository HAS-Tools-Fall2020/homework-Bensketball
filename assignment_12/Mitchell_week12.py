# This script assumes you have already downloaded several netcdf files
# see the assignment instructions for how to do this
# %%
import os
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xarray as xr
import rioxarray
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import seaborn as sns
import geopandas as gpd
import fiona
import shapely
from netCDF4 import Dataset


# %%
# Ben's NetCDF Code Start!
# https://rda.ucar.edu/datasets/ds084.1/index.html#!cgi-bin/datasets/getSubset?dsnum=084.1&listAction=customize&_da=y
data_path = os.path.join('./data',
                         'X72.222.172.39.327.20.28.52.nc')

my_dataset = xr.open_dataset(data_path)
print(my_dataset)
print(type(my_dataset))


# %%
# We can inspect the metadata of the file like this:
my_metadata = my_dataset.attrs
print(my_metadata)

# And we can grab out any part of it like this:
my_metadata['dataset_title']


# %%
# Now lets take a slice: Grabbing data for just one point
lat = my_dataset["prate"]["lat"].values[0]
lon = my_dataset["prate"]["lon"].values[0]
print("Long, Lat values:", lon, lat)
my_point = my_dataset["prate"].sel(lat=lat,lon=lon)
my_point.shape


# %%
# use x-array to plot timeseries
my_point.plot.line()
precip_val = my_point.values


# %%
# Make a nicer timeseries plot
f, ax = plt.subplots(figsize=(12, 6))
my_point.plot.line(hue='lat',
                    marker="o",
                    ax=ax,
                    color="grey",
                    markerfacecolor="purple",
                    markeredgecolor="purple")
ax.set(title="Time Series For a Single Lat / Lon Location")


# %%
# Creating my dataframe
precip_data = my_point.to_dataframe()
precip_data['datetime'] = my_dataset["prate"]["time"].values
precip_data['month'] = pd.DatetimeIndex(precip_data['datetime']).month
precip_data['year'] = pd.DatetimeIndex(precip_data['datetime']).year
precip_data['month_year'] = pd.to_datetime(precip_data['datetime']).dt.strftime('%Y-%m')
precip_data['yearday'] = pd.to_datetime(precip_data['datetime']).dt.strftime('%j')

# yearday to integer
precip_data['yearday'] = pd.to_numeric(precip_data['yearday'])

# Setting my Index
precip_by_year = precip_data.set_index('yearday')

# %%
# Next Attempt
# precip_by_year = pd.DataFrame(index= (np.arange(0, 366, 1)))

yr_2000 = precip_by_year.loc[precip_by_year['year'] == 2000]
yr_2001 = precip_by_year.loc[precip_by_year['year'] == 2001]
yr_2002 = precip_by_year.loc[precip_by_year['year'] == 2002]
yr_2003 = precip_by_year.loc[precip_by_year['year'] == 2003]
yr_2004 = precip_by_year.loc[precip_by_year['year'] == 2004]
yr_2005 = precip_by_year.loc[precip_by_year['year'] == 2005]
yr_2006 = precip_by_year.loc[precip_by_year['year'] == 2006]
yr_2007 = precip_by_year.loc[precip_by_year['year'] == 2007]
yr_2008 = precip_by_year.loc[precip_by_year['year'] == 2008]
yr_2009 = precip_by_year.loc[precip_by_year['year'] == 2009]
yr_2010 = precip_by_year.loc[precip_by_year['year'] == 2010]
yr_2011 = precip_by_year.loc[precip_by_year['year'] == 2011]
yr_2012 = precip_by_year.loc[precip_by_year['year'] == 2012]
yr_2013 = precip_by_year.loc[precip_by_year['year'] == 2013]
yr_2014 = precip_by_year.loc[precip_by_year['year'] == 2014]
yr_2015 = precip_by_year.loc[precip_by_year['year'] == 2015]
yr_2016 = precip_by_year.loc[precip_by_year['year'] == 2016]
yr_2017 = precip_by_year.loc[precip_by_year['year'] == 2017]
yr_2018 = precip_by_year.loc[precip_by_year['year'] == 2018]
yr_2019 = precip_by_year.loc[precip_by_year['year'] == 2019]
yr_2020 = precip_by_year.loc[precip_by_year['year'] == 2020]


# %%
# Plotting
# precip_by_year.plot.line(y = 'prate')

# x = np.arange(0, 366, 1)

fig, ax = plt.subplots()
ax.plot(yr_2000['prate'],  label='2000')
ax.plot(yr_2001['prate'],  label='2001')
ax.plot(yr_2002['prate'],  label='2002')
ax.plot(yr_2003['prate'],  label='2003')
ax.plot(yr_2004['prate'],  label='2004')
ax.plot(yr_2005['prate'],  label='2005')
ax.plot(yr_2006['prate'],  label='2006')
ax.plot(yr_2007['prate'],  label='2007')
ax.plot(yr_2008['prate'],  label='2008')
ax.plot(yr_2009['prate'],  label='2009')
ax.plot(yr_2010['prate'],  label='2010')
ax.plot(yr_2011['prate'],  label='2011')
ax.plot(yr_2012['prate'],  label='2012')
ax.plot(yr_2013['prate'],  label='2013')
ax.plot(yr_2014['prate'],  label='2014')
ax.plot(yr_2009['prate'],  label='2015')
ax.plot(yr_2010['prate'],  label='2016')
ax.plot(yr_2011['prate'],  label='2017')
ax.plot(yr_2012['prate'],  label='2018')
ax.plot(yr_2013['prate'],  label='2019')
ax.plot(yr_2020['prate'],  label='2020')
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.title('Precipitation By Year', fontsize=15)
plt.xlabel('Julian Day', fontsize=15)
plt.ylabel('Average Precipitation', fontsize=15)
ax.legend(ncol=4, fontsize=15)
fig.patch.set_facecolor('xkcd:white')
plt.tight_layout()
fig.set_size_inches(27, 10)

fig.savefig('Precipitation By Year.png')


# %%
