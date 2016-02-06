import pandas as pd
from _settings import *
import urllib, json
import time

inCSV   = wp+'address/rnd0/address.csv'

df = pd.read_csv(inCSV)

df = df.fillna('missing')

df['concat'] = df.uid.map(str) + '^' + df['hn'] + '^' + df['street'] + '^' + df['boro'] + '^' + df['state']

print df.head(10)

dfList = df['concat'].tolist()

def nycGeoClient(uid,houseNumber,street,borough,appid,apikey):
	theRequest = "https://api.cityofnewyork.us/geoclient/v1/address.json?houseNumber="+houseNumber+"&street="+street+",&borough="+borough+"&app_id="+appid+"&app_key="+apikey
	print theRequest
	url = theRequest
	try:
		response = urllib.urlopen(url)
		data = json.loads(response.read())
		print data
		with open('geoclient_data/'+str(uid)+'.json', 'w') as outfile:
			json.dump(data, outfile)
			time.sleep(1)
	except:
		print 'for uid:', uid, 'shit was fucked up'

apikey = '9c9f84d37a3b00a56444db091c8812a6'
appid  = '41cc2f11'

for i in dfList:
	print i
	uid = i.split('^')[0]
	#print uid
	hn  = i.split('^')[1]
	st  = i.split('^')[2]
	bo  = i.split('^')[3]
	nycGeoClient(uid,hn,st,bo,appid,apikey)


# hn     = '44-78'
# st     = '23RD ST'
# bo     = 'Queens'


