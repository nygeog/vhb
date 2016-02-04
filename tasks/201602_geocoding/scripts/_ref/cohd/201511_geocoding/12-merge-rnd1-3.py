import pandas as pd
import numpy as np 

from streetaddress import StreetAddressFormatter
from streetaddress import StreetAddressParser

addr_parser = StreetAddressParser()

pd.options.display.max_columns = 5200
pd.options.display.max_rows    = 5200

from _settings import *

ouAddressIn = wi+'address/address.csv'

#inAddress   = pr + 'data/input/address/20150422/danny_addresses.csv'
inAddress = ouAddressIn

r1Address   = wp+'address/rnd1/gbatout_bin_xy.csv'
r2Address   = wp+'address/rnd2/gbatout_bin_xy.csv'
r3Address   = wp+'address/rnd3/gbatout_bin_xy.csv'

df   = pd.read_csv(ouAddressIn)
df   = pd.read_csv(inAddress)
dfR1 = pd.read_csv(r1Address)
dfR2 = pd.read_csv(r2Address)
dfR3 = pd.read_csv(r3Address)

df_list = []
df_list.append(dfR1)
df_list.append(dfR2)
df_list.append(dfR3)

dfR123 = pd.concat(df_list)

df = df.rename(columns=lambda x: x.lower())
#df['p3muid'] = 30001 + df.index
df = df[['uid']]#,'pid']]

df = df.merge(dfR123, on='uid', how='outer')

df = df[(df.rnd1 == 1) | (df.rnd2 == 2)  | (df.rnd3 == 3)] 

print str(len(df.index)) + ' have valid bin-s and xy-s'

df['wave'] = 1

df.to_csv(wd+'data/output/geocoded/uid_subjectid_bin_xy.csv', index=False)

print df.head(100)

dfI = pd.read_csv(inAddress)

print str(len(dfI.index)) + ' in input dataset'

dfI = dfI.merge(dfR123, on='uid', how='outer')

dfI = dfI[(dfI.rnd1 <> 1) & (dfI.rnd2 <> 2) & (dfI.rnd3 <> 3)] 

print str(len(dfI.index)) + ' not geocoded in 3 rounds'

dfI['p3m_missing'] = pd.isnull(dfI['street'])

dfMissing = dfI[(dfI.p3m_missing == True)]
print str(len(dfMissing.index)) + ' are missing p3m_streetAddress'

dfI = dfI[(dfI.p3m_missing == False)]
print str(len(dfI.index)) + ' have p3m_streetAddress but have not been geocoded'


ouUnGeocoded = wd+'data/output/ungeocoded/ungeocoded.csv'

#dfUnGeo = dfI[['p3muid']]

dfI.to_csv(ouUnGeocoded, index=False)

print dfI.head(100)