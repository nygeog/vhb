import pandas as pd
import numpy as np 

from streetaddress import StreetAddressFormatter
from streetaddress import StreetAddressParser

addr_parser = StreetAddressParser()

pd.options.display.max_columns = 5200
pd.options.display.max_rows    = 5200

from _settings import *

from shapely.geometry import Point, mapping
from fiona import collection

inCSV  = wo+'geocoded/uid_subjectid_bin_xy.csv'
shpOut = wo+'geocoded/uid.shp'

y = 'y'
x = 'x'

schema = { 'geometry': 'Point', 'properties': { 'uid': 'str' }, }

df = pd.read_csv(inCSV) 
df['x'] = df['xcoord']
df['y'] = df['ycoord']
df = df[['uid','x','y']]

data = df
with collection(shpOut, "w", "ESRI Shapefile", schema) as output:
    for index, row in data.iterrows():
        point = Point(row[x], row[y])
        output.write({
            'properties': {'uid': row['uid'],'uid': row['uid'],'uid': row['uid']},
            'geometry': mapping(point)
        })

#DEFINE PROJECTION IS THE NEXT STEP. BY COPYING PRJ FILES FOR EPSG 4326 with the filename.prj
#http://www.topografix.com/GPX/1/1/
# EPSG 2263
import shutil

prjFile = wdi + 'prj/2263.prj'
prjOut  = wo+'geocoded/uid.prj'

shutil.copy2(prjFile, prjOut)