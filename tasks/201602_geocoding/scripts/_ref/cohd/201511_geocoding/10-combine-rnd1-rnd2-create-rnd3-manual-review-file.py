import pandas as pd
import numpy as np 

from streetaddress import StreetAddressFormatter
from streetaddress import StreetAddressParser

addr_parser = StreetAddressParser()

pd.options.display.max_columns = 5200
pd.options.display.max_rows    = 5200

from _settings import *

ouAddressIn = wi+'address/address.csv'
r1Address   = wp+'address/rnd1/gbatout_bin_xy.csv'
r2Address   = wp+'address/rnd2/gbatout_bin_xy.csv'
our3Address = wp+'address/rnd3/address_with_uid_rnd3.csv'

df   = pd.read_csv(ouAddressIn)
dfR1 = pd.read_csv(r1Address)
dfR2 = pd.read_csv(r2Address)

df_list = []
df_list.append(dfR1)
df_list.append(dfR2)

dfR12 = pd.concat(df_list)

df = df.merge(dfR12, on='uid', how='outer')

df = df[(df.rnd1 <> 1)]
df = df[(df.rnd2 <> 2)]
print len(df.index), ' to review!'

#df = df[['p3muid','streetAddress','city','state','zip','hn','street','boro','suite_type','suite_num']]

df.to_csv(our3Address, index=False)

print df.head(100) 

#MANUALLY REVIEW BINS AND ADDRESSES FOR ROUND 3
#
#ADD THESE FIELDS to EXCEL SHEET 
#
#not_nyc	no_hn	po_box	bin_clean	valid_addr	notes
#
# renamce as <filename>_working.xls and save
