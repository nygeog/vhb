import pandas as pd
import numpy as np 

from streetaddress import StreetAddressFormatter
from streetaddress import StreetAddressParser

addr_parser = StreetAddressParser()

pd.options.display.max_columns = 5200
pd.options.display.max_rows    = 5200

from _settings import *

ouAddressIn   = wi+'address/address.csv'
ouAddressRnd1 = wp+'address/rnd1/gbatout_bin_xy.csv'
ouAddressRnd2 = wp+'address/rnd2/address_with_uid_rnd2.csv'

df     = pd.read_csv(ouAddressIn)
dfRnd1 = pd.read_csv(ouAddressRnd1)

df = df.merge(dfRnd1, on='uid', how='outer')

df = df[(df.rnd1 <> 1)]
print len(df.index)

#df = df[['p3muid','p3m_streetAddress','p3m_city','p3m_state','p3m_zip','hn','street','boro','suite_type','suite_num']]

def cleanStreet(streetString):
	x = str(streetString).upper()
	x = x.replace('STREE ','STREET ')
	x = x.replace("BWAY ",'BROADWAY ').replace("B'WAY ",'BROADWAY ') 
	x = x.replace(" BRONX",' ').replace(" NEW YORK",'').replace(" BROOKLYN",'')
	return x

df['fullstreet'] =  df.hn.map(str) + " " + df.street.map(cleanStreet) #"!hn! + ' ' +  !street!"

df.to_csv(ouAddressRnd2, index=False)

print df