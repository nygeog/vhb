import pandas as pd
import numpy as np 

from streetaddress import StreetAddressFormatter
from streetaddress import StreetAddressParser

addr_parser = StreetAddressParser()

pd.options.display.max_columns = 5200
pd.options.display.max_rows    = 5200

from _settings import *

inBoro = wp+'intersects/' + 'boro/uid_boro_int.csv'
inCB00 = wp+'intersects/' + 'census/uid_cb2000_int.csv'
inCB10 = wp+'intersects/' + 'census/uid_cb2010_int.csv'
inComD = wp+'intersects/' + 'community_districts/uid_cd_int.csv'

ouCSV  = wo+'geocoded/uid_admin.csv'

dfBoro = pd.read_csv(inBoro).rename(columns=lambda x: x.lower())
dfCB00 = pd.read_csv(inCB00).rename(columns=lambda x: x.lower())
dfCB10 = pd.read_csv(inCB10).rename(columns=lambda x: x.lower())
dfComD = pd.read_csv(inComD).rename(columns=lambda x: x.lower())

dfBoro = dfBoro[['uid','borocode','boroname']]
dfCB00 = dfCB00[['uid','geoid']]
dfCB10 = dfCB10[['uid','geoid']]
dfComD = dfComD[['uid','borocd']]

dfCB00.columns = ['uid', 'cb2000gid']
dfCB10.columns = ['uid', 'cb2010gid']

print dfBoro.head(5)
print dfCB00.head(5)
print dfCB10.head(5)
print dfComD.head(5)

mergeID = 'uid'

df = dfBoro.merge(dfComD, how='outer', on=mergeID).merge(dfCB00, how='outer', on=mergeID).merge(dfCB10, how='outer', on=mergeID)

df.to_csv(ouCSV, index=False)

df