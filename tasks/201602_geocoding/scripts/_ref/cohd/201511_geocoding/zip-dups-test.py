import pandas as pd

from _settings import *

inZipTable = wdi+'zip/zip_code.csv'
dfzip = pd.read_csv(inZipTable)

dfzip['count'] = 1

dfzip = dfzip.groupby(['zipcode','county'],as_index=False).sum()

dfzip = dfzip[['zipcode','county']]

dfzip['zip'] = dfzip['zipcode'].astype(str)

dfzip = dfzip[['zip','county']]

print dfzip.head(500)

#Drop the following ZIP codes, as '11693', '10463', '11370' reside in two counties but drop county that makes no sense.
dfzip = dfzip[~((dfzip.zip == '11370') & (dfzip.county == 'Bronx'))] 
dfzip = dfzip[~((dfzip.zip == '10463') & (dfzip.county == 'New York'))] 
dfzip = dfzip[~((dfzip.zip == '11693') & (dfzip.county == 'Kings'))] 

dfzip.to_csv('zip_test.csv', index=False)

dfList = dfzip['zip'].tolist()

theDups = set([x for x in dfList if dfList.count(x) > 1])

print theDups