# Class Exercises - 10/29/2020

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#needed to make web requests
import requests

#store the data we get as a dataframe
import pandas as pd

#convert the response as a strcuctured json
import json

#mathematical operations on lists
import numpy as np

#parse the datetimes we get from NOAA
from datetime import datetime

# %% 
# Downloading data directly from NOAA's API.
# https://towardsdatascience.com/getting-weather-data-in-3-easy-steps-8dc10cc5c859
# NOAA NCDC's Climate Data Online (CDO) has a size data limit.
# So, let do a loop to download the data by year.
# Store lists
dates_prcp = []
prcp = []
# Insert your token here
headers = {'token': 'VSkxlHQnVGEZkuZWzGwEOuVmOXnMWNug'}
 
# This is the base url that will be the start our final url
base_url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/data"
 
# Parameters:
datasetid = "GHCND"
stationid = "GHCND:USC00025635"
datatypeid = "PRCP"
startyear = 1989
endyear = 2020
 
for year in range(startyear, endyear + 1):
    year = str(year)
 
    # writing the complete URL
    url = base_url + '?' + 'datasetid=' + datasetid + '&stationid=' + \
        stationid + '&datatypeid=' + datatypeid + '&units=metric' + \
        '&startdate=' + year + '-01-01&enddate=' + year + '-12-31&limit=1000'
    print("downloading", year)
 
    # make the api call
    apicall = requests.get(url, headers=headers)
 
    # load the api response
    response = apicall.json()
 
    for i in range(len(response['results'])):
        dates_prcp_get = response['results'][i]['date']
        prcp_get = response['results'][i]['value']
        dates_prcp.append(dates_prcp_get)
        prcp.append(prcp_get)
print("download completed")
 
# %%
# Now we can combine this into a pandas dataframe
data_NOAA = pd.DataFrame({'Precipitation': prcp, 'datetime': dates_prcp},
                         index=pd.to_datetime(dates_prcp))
 
# Expand the dates to year, month, day, and days of the week.
data_NOAA['year'] = pd.DatetimeIndex(data_NOAA['datetime']).year
 
# %%
# Aggregate prcp values to weekly: from sunday to saturday
rain_weekly = data_NOAA.resample("W-SAT").mean()
# %%
