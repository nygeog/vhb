import pandas as pd
from streetaddress import StreetAddressFormatter
from streetaddress import StreetAddressParser

addr_parser = StreetAddressParser()

from _settings import *

inXLS = wdi + 'address/USN_Geocode.xlsx'


df1 = pd.io.excel.read_excel(inXLS, 'Jackson_Heights_HD')
df2 = pd.io.excel.read_excel(inXLS, 'Broadway_Flushing_HD')


print df1.head(10)
print df2.head(10)

df1.to_csv(wi + 'address/jh.csv', index=False, encoding='utf-8')
df2.to_csv(wi + 'address/bf.csv', index=False, encoding='utf-8')

# keepCols_1 = ['patid','street_address','city','state','zip','dateint2']
# keepCols_2 = ['ID','Address','Apt','City','State','Zip_code','Visit_Date']
# keepCols_3 = ['ID','Address','Apt','City','State','Zip_code','baseline_date_completed']
# keepCols_4 = ['NOMEM_ID','Address','Apt','City','State','Zip_code','Date_Enrollment']

# print 'for coach date data - from .spss file'
# df1_date = pd.read_csv(wdi + 'address/_coach_dates/COACH recruitment date.csv')
# print df1_date.head(10)

# df1 = df1.merge(df1_date, on='patid', how='left')
# print df1.head(10)

# df1 = df1[keepCols_1]
# df2 = df2[keepCols_2]
# df3 = df3[keepCols_3]
# df4 = df4[keepCols_4]

renameCols1 = ['id','address']
renameCols2 = ['id','address']

df1.columns = renameCols1
df2.columns = renameCols2

df1['proj'] = 'jh'
df2['proj'] = 'bf'

df1.to_csv(wi + 'address/jf_cln.csv', index=False, encoding='utf-8')
df2.to_csv(wi + 'address/bf_cln.csv', index=False, encoding='utf-8')

print df1.head(10)
print df2.head(10)

df = pd.concat([df1,df2], axis=0)
df = df[['id','address','proj']] 

df['address_cln_1'] = df.address.str.split(',',1).str[0].str.upper()
df['address_cln_2'] = df.address_cln_1.str.split(' APT',1).str[0]

# df['zip_cln'] = df.zip.map(str).str[:5]

df = df.sort(['id'], ascending=[1])

print df.dtypes 
df.to_csv(wi + 'address/address_all_vars.csv', index=False, encoding='utf-8')

print len(df.index)

#df = df[['id','address_cln_2','proj']] #get rid of date col #####might need to keep orig to get BORO
df.to_csv(wi + 'address/address_only.csv', index=False, encoding='utf-8')

df_dup = df.set_index('id').index.get_duplicates()

for i in df_dup:
	print i


# df['addr_concat'] =  df.id.map(str) + '^' + df.address_cln_2.map(str) + '^' + df.city.map(str) + '^' + df.state.map(str)+ '^' + df.zip_cln.map(str) + '^' + df.proj.map(str)
df['addr_concat'] =  df.id.map(str) + '^' + df.address_cln_2.map(str) + '^' + df.proj.map(str)


# df = df[['addr_concat']]
# df['cnt'] = 1

# dfg = df.groupby(['addr_concat'],as_index=False).sum()

# print len(df.index)

df['uid'] = df.index + 90001
# # dfg['zip']  = dfg.addr_concat.str.split('^',5).str[4]  #NO FUCKING ZIP, just boro

# dfg['id'] = dfg.addr_concat.str.split('^',5).str[0]
# dfg['streetaddress'] = dfg.addr_concat.str.split('^',5).str[1] + ' ' + dfg.addr_concat.str.split('^',5).str[2] + ' ' 

# inZipTable = wdi+'zip/zip_code.csv'
# dfzip = pd.read_csv(inZipTable)
# dfzip['count'] = 1
# dfzip = dfzip.groupby(['zipcode','county'],as_index=False).sum()
# dfzip = dfzip[['zipcode','county']]
# dfzip['zip'] = dfzip['zipcode'].astype(str)
# dfzip = dfzip[['zip','county']]
# #Drop the following ZIP codes, as '11693', '10463', '11370' reside in two counties but drop county that makes no sense. May need to add to at some point. 
# dfzip = dfzip[~((dfzip.zip == '11370') & (dfzip.county == 'Bronx'))] 
# dfzip = dfzip[~((dfzip.zip == '10463') & (dfzip.county == 'New York'))] 
# dfzip = dfzip[~((dfzip.zip == '11693') & (dfzip.county == 'Kings'))] 
# print dfzip.head(5000)
# df = dfg.merge(dfzip, how='left', on='zip')

#df = dfg

print df.dtypes 

def boroCode(boroName):
    if   boroName.lower() == 'manhattan':
        return 1
    elif boroName.lower() == 'new york':
        return 1
    elif boroName.lower() == 'bronx':
        return 2
    elif boroName.lower() == 'brooklyn':
        return 3
    elif boroName.lower() == 'kings':
        return 3
    elif boroName.lower() == 'staten island':
        return 5
    elif boroName.lower() == 'richmond':
        return 5
    elif boroName.lower() == 'queens':
        return 4
    else:
        return 4
    
def addrStreetName(addy):
    addr = addr_parser.parse(addy)
    return addr['street_full']

def addrHouseNumber(addy):
    addr = addr_parser.parse(addy)
    return addr['house']

def addrSuiteNumber(addy):
    addr = addr_parser.parse(addy)
    return addr['suite_num']

def addrSuiteType(addy):
    addr = addr_parser.parse(addy)
    return addr['suite_type']

def cleanStreet(streetString):
    x = str(streetString).upper()
    x = x.split(' ',1)[1]
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
    x = x.replace('  ','')
    return x

df['streetaddress'] = df['address']

df['address'] = df.streetaddress.str.replace(',','').replace('.','')
df['addressRemoveSuite'] = df.address.str.split('#',1).str[0]
df['hn']    = df.address.map(str).apply(addrHouseNumber)
# #df['street'] = df.addressRemoveSuite.map(str).apply(addrStreetName)
df['street'] = df.address.map(cleanStreet)

#gotta get up to speed here, no ZIP, just pull boro from address string, first let's get the df




# def find_between(s, first, last):
#     try:
#         start = s.index( first ) + len( first )
#         end = s.index( last, start )
#         return s[start:end]
#     except ValueError:
#         return ""

#df['county'] = df.streetaddress.map(str).apply(find_between(i, ', ', ' NY'))
df['county'] = (df.streetaddress.str.split(' NY',1).str[0]).str.split(', ',1).str[1]


df['boro']   = df.county.map(str)#.apply(boroCode)

print df.head(20)


df['suite_type'] = df.address.map(str).apply(addrSuiteType)
df['suite_num']    = df.address.map(str).apply(addrSuiteNumber)
df['city'] = df['county']
df['state'] = 'NY'

df.to_csv(wi + 'address/address_only_rem_dups.csv', index=False, encoding='utf-8')

ouAddressIn = wi+'address/address.csv'
ouAddress   = wp+'address/rnd1/address.csv'

df.to_csv(ouAddressIn, index=False) #Rewriting (overwriting) this file so it has the UID

df = df[['uid','hn','street','boro','state']]#,'zip']]

df.to_csv(ouAddress, index=False)

df.head(100)
