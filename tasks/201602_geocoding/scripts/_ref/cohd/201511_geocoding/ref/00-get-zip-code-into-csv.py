import csv
from dbfpy import dbf
import os
import sys
import glob
import pandas as pd

filename = '/Volumes/Echo/GIS/projects/resistome/data/input/zip/ZIP_CODE_040114/ZIP_CODE_040114.dbf'

if filename.endswith('.dbf'):
    print "Converting %s to csv" % filename
    csv_fn = filename[:-4]+ ".csv"
    with open(csv_fn,'wb') as csvfile:
        in_db = dbf.Dbf(filename)
        out_csv = csv.writer(csvfile)
        names = []
        for field in in_db.header.fields:
            names.append(field.name)
        out_csv.writerow(names)
        for rec in in_db:
            out_csv.writerow(rec.fieldData)
        in_db.close()
        print "Done..."
else:
  print "Filename does not end with .dbf"

csv = '/Volumes/Echo/GIS/projects/resistome/data/input/zip/ZIP_CODE_040114/ZIP_CODE_040114.csv'

filename = csv

df = pd.read_csv(filename)
df = df.rename(columns=lambda x: x.lower())

df.to_csv('/Volumes/Echo/GIS/projects/resistome/data/input/zip/zip_code.csv',index=False)

df.head(10)