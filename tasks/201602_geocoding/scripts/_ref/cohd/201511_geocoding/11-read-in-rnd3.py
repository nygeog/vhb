import pandas as pd
import numpy as np 

from streetaddress import StreetAddressFormatter
from streetaddress import StreetAddressParser

addr_parser = StreetAddressParser()

pd.options.display.max_columns = 5200
pd.options.display.max_rows    = 5200

from _settings import *

xlsFile       = wp+'address/rnd3/address_with_uid_rnd3_working.xls'
inBin         = wdi+'building_footprints/building_points.csv'
our3Address   = wp+'address/rnd3/gbatout_bin_xy.csv'
our4Address   = wp+'address/rnd4/address_with_uid_rnd4.csv'

df = pd.io.excel.read_excel(xlsFile, 'address_with_uid_rnd3.csv')

bldg = pd.read_csv(inBin, sep=';').rename(columns=lambda x: x.lower())
bldg = bldg[['xcoord','ycoord','bin']]
bldg = bldg[(bldg.bin <> 1000000) & (bldg.bin <> 4000000) & (bldg.bin <> 2000000) & (bldg.bin <> 3000000)]
#these are generic, non-specific bin's. 201309 building files has 72,928 of them. The
#201412 buidling file has 30,311 with these bin codes

dfErr = df

df = df[['uid','bin_clean']]
df.columns = ['uid', 'bin']
print len(df.index)

df = df.merge(bldg, how='left', on='bin')

df['rnd3'] = 3

df['xcoord'] = df['xcoord'].astype(float)
df['ycoord'] = df['ycoord'].astype(float)

df = df[df.xcoord > 0]
df = df[df.ycoord > 0]

print str(len(df.index)) + ' have valid bin-s and xy-s'

df.to_csv(our3Address, index=False)

print df.head(100) 