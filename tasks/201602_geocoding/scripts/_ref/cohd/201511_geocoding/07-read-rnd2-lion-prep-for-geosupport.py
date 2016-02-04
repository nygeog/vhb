import pandas as pd
import numpy as np 

from streetaddress import StreetAddressFormatter
from streetaddress import StreetAddressParser

addr_parser = StreetAddressParser()

pd.options.display.max_columns = 5200
pd.options.display.max_rows    = 5200

from _settings import *

def addrStreetName(addy):
    addr = addr_parser.parse(addy)
    return addr['street_full']

def addrHouseNumber(addy):
    addr = addr_parser.parse(addy)
    return addr['house']

def removeLeadNumber(addy):
	addr = str(addy)
	if addr.split(' ',1)[0].isdigit() == True:
		z = addr.replace(addr.split(' ',1)[0],'')
	else:
		z = addr
	return z

def cleanStreetNoSplit(streetString):
    x = str(streetString).upper()
    #x = x.split(' ',1)[1]
    x = x.replace('.', ' ')
    x = x.replace('STREE ','STREET ').replace(' AVENU ',' AVENUE ')
    x = x.replace("BWAY ",'BROADWAY ').replace("B'WAY ",'BROADWAY ') 
    x = x.replace(" BRONX",' ').replace(" NEW YORK",'').replace(" BROOKLYN",' ')
    x = x.replace(' NY', ' ').replace(" MANHATTAN", ' ').replace(' QUEENS',' ')
    x = x.replace(' ST  ALBANS',' ').replace(' CAMBRIA HEIGHTS',' ').replace(' FAR ROCKAWAY',' ')
    x = x.replace(' LAURELTON',' ').replace(' QUEENS VILLAGE',' ').replace(' JAMAICA',' ').replace(' HOLLIS',' ')
    x = x.replace(' WOODSIDE',' ').replace(' FLUSHING',' ').replace(' ELMHURST',' ').replace(' SUNNYSIDE',' ')
    x = x.replace(' KEW GARDENS',' ').replace(' ASTORIA',' ').replace(' EAST ELMHURST',' ')
    x = x.replace(' COLLEGE POINT',' ').replace(' FOREST HILLS',' ').replace(' LONG ISLAND CITY',' ')
    x = x.replace(' WOODHAVEN',' ').replace(' FRESH MEADOWS',' ').replace(' SPRINGFIELD GARDENS',' ')
    x = x.replace(' ROSEDALE',' ').replace(' BRIARWOOD',' ').replace(' ROCHDALE VILLAGE',' ')
    x = x.replace('BROADWAY 1','BROADWAY').replace('BROADWAY 2','BROADWAY')#.replace(' ROCHDALE VILLAGE',' ')
    return x

inCSV = wp+'address/rnd2/address_with_uid_rnd2_lion_geocode_out.csv'
ouCSV = wp+'address/rnd2/to_geosupport/rnd2_to_geosupport.csv'

df = pd.read_csv(inCSV, sep=';').rename(columns=lambda x: x.lower())

print len(df.index)

df = df[(df.status == 'M')]

print len(df.index)

df['hn_r2']     = df['hn'] #.match_addr.apply(addrHouseNumber)
df['street_r2'] = df.match_addr.apply(addrStreetName).apply(removeLeadNumber).apply(cleanStreetNoSplit)
df['boro_r2']   = df.match_addr.str.split(',',1).str[1]
df['boro_r2']   = df.boro_r2.str.replace(' ','')   #replace leading ' '   

df = df[['uid','hn_r2','street_r2','boro_r2']]

df.to_csv(ouCSV, index=False)

print df.head(100)