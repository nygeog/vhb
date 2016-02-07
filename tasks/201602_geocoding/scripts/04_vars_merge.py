import pandas as pd
from _settings import *

inAddress   = wp+'address/rnd0/address_geoclient.csv'

df = pd.read_csv(inAddress)

#print df.head(10)

print df.dtypes 

dfAllVars = wi+'address/address.csv'
dfA = pd.read_csv(dfAllVars)

#print dfAllVars.head(10)
print dfA.dtypes 

df = df.merge(dfA, how='left', on='uid')

ouAddress   = wo+'address_geoclient.csv'
df.to_csv(ouAddress, index=False)