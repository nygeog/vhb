import pandas as pd
import numpy as np 

from streetaddress import StreetAddressFormatter
from streetaddress import StreetAddressParser

addr_parser = StreetAddressParser()

pd.options.display.max_columns = 5200
pd.options.display.max_rows    = 5200

from _settings import *

inAddress   = wp +'address/rnd1/GBATOut.csv'
ouAddress   = wp +'address/rnd1/gbatout_bin_xy.csv'
inBin       = wdi+'building_footprints/building_points.csv'

df = pd.read_csv(inAddress)
df['bin'] = df['WA2_AddrRange1BIN']

df = df[['address.csv_uid','bin']]
df.columns = ['uid', 'bin']
print len(df.index)

bldg = pd.read_csv(inBin, sep=';').rename(columns=lambda x: x.lower())
bldg = bldg[['xcoord','ycoord','bin']]
bldg = bldg[(bldg.bin <> 1000000) & (bldg.bin <> 4000000) & (bldg.bin <> 2000000) & (bldg.bin <> 3000000)]
#these are generic, non-specific bin's. 201309 building files has 72,928 of them. The
#201412 buidling file has 30,311 with these bin codes

df = df.merge(bldg, how='left', on='bin')

df['rnd1'] = 1

df['xcoord'] = df['xcoord'].astype(float)
df['ycoord'] = df['ycoord'].astype(float)

df = df[df.xcoord > 0]
df = df[df.ycoord > 0]

print str(len(df.index)) + ' have valid bin-s and xy-s'

df.to_csv(ouAddress, index=False)

df#.head(5)