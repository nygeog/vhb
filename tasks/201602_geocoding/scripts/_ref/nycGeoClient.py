

z = 'https://api.cityofnewyork.us/geoclient/v1/address.json?houseNumber=44-78&street=23RD ST,&borough=Queens&app_id=41cc2f11&app_key=9c9f84d37a3b00a56444db091c8812a6'

apikey = '9c9f84d37a3b00a56444db091c8812a6'
appid  = '41cc2f11'

hn     = '44-78'
st     = '23RD ST'
bo     = 'Queens'

def nycGeoClient(houseNumber,street,borough,appid,apikey):
	theRequest = "https://api.cityofnewyork.us/geoclient/v1/address.json?houseNumber="+houseNumber+"&street="+street+",&borough="+borough+"&app_id="+appid+"&app_key="+apikey
	print theRequest

nycGeoClient(hn,st,bo,appid,apikey)

print z	