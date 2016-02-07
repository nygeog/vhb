import pandas as pd
import glob
import os
from _settings import *

fnamesList = glob.glob("geoclient_data/*.json")

df_list = []

for j in fnamesList:
	print j
	df = pd.read_json(j)
	df = df.T
	df['uid'] = j.replace('geoclient_data/','').replace('.json','')
	df = df.set_index('uid')
	df_list.append(df)

df = pd.concat(df_list)

print df

ouAddress   = wp+'address/rnd0/address_geoclient.csv'

df.to_csv(ouAddress, index=True)