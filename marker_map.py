import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import csv

latitudeArray = []
longitudeArray = []

with open("bicycle.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        x, y = float(row[0]), float(row[1])
        latitudeArray.append(x) #storing all the latitudes and longitudes in separate arrays, but the index is the same for each pair
        longitudeArray.append(y)
        
m = Basemap(llcrnrlon=min(longitudeArray)-10, #Set map's displayed max/min based on your set's max/min
    llcrnrlat=min(latitudeArray)-10,
    urcrnrlon=max(longitudeArray)+10,
    urcrnrlat=max(latitudeArray)+10,
    lat_ts=20, #"latitude of true scale" lat_ts=0 is stereographic projection
    resolution='h', #resolution can be set to 'c','l','i','h', or 'f' - for crude, low, intermediate, high, or full
    projection='merc',
    lon_0=longitudeArray[0],
    lat_0=latitudeArray[0])

x1, y1 = m(longitudeArray, latitudeArray) #map the lat, long arrays to x, y coordinate pairs
m.drawmapboundary(fill_color="white")
m.drawcoastlines()
m.drawcountries()
m.scatter(x1, y1, s=25, c='r', marker="o") #Plot your markers and pick their size, color, and shape
plt.title("Steen's Bicycling Coordinates")
plt.show()