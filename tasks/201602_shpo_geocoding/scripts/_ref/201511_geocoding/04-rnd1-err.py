import pandas as pd
import numpy as np 

from streetaddress import StreetAddressFormatter
from streetaddress import StreetAddressParser

addr_parser = StreetAddressParser()

pd.options.display.max_columns = 5200
pd.options.display.max_rows    = 5200

from _settings import *

inError = wp+'address/rnd1/GBATErr.csv'

df = pd.read_csv(inError)

print len(df.index)

df.head(5)

dfMissingHn = df[(df.hn == 0)]

print len(dfMissingHn.index)

dfMissingHn.head(5)

dfValidHn = df[(df.hn > 0)]

print len(dfValidHn.index)

dfValidHn.head(15)

ouAddressIn = wd+'data/input/address/address.csv' #_with_p3muid.csv'

addIn = pd.read_csv(ouAddressIn)

df = df[['uid','GRC','ReasonCode','BadRecordId']]

df = df.merge(addIn, how='left', on='uid')

print len(df.index)

print df.dtypes

df

df = df[(df.hn != 'missing')]

df

print dfMissingHn.head(200)

