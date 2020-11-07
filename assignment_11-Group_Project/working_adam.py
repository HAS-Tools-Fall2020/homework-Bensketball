
# %%
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
import geopandas as gpd
import fiona
from shapely.geometry import Point
import contextily as ctx


# %%
#  Gauges II USGS stream gauge dataset:
# Download here:
# https://water.usgs.gov/GIS/metadata/usgswrd/XML/gagesII_Sept2011.xml#stdorder
# Reading it using geopandas
file = os.path.join('../data', 'gagesII_9322_sept30_2011.shp')
gages = gpd.read_file(file)
gages_AZ=gages[gages['STATE']=='AZ']
# %%
# adding more datasets
# https://www.usgs.gov/core-science-systems/ngp/national-hydrography/access-national-hydrography-products
# https://viewer.nationalmap.gov/basic/?basemap=b1&category=nhd&title=NHD%20View

# Example reading in a geodataframe
# Watershed boundaries for the lower colorado
filepath = '../data/Shape'
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
filepath = '../data/S_USA.AdministrativeForest'
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
filepath = '../data/USA_Rivers_and_Streams-shp'
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
