import pandas as pd
import glob
import os

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

# 

# for j in all_csvs:
# 	df = pd.read_csv(j)
# 	df_list.append(df)

# df = pd.concat(df_list)
print df
df.to_csv('TEST1.csv')