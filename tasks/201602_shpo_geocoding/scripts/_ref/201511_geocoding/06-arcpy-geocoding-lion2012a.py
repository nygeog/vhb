import arcpy

from _settings import *

wind = "X:" #Windows drive
dd   = "Z:/Dropbox/" #Dropbox drive
pp = '/GIS/projects/cohd/'

wd = wind + pp + tf

wi = wd + 'data/input/'
wp = wd + 'data/processing/'
wo = wd + 'data/output/'
wt = wd + 'data/tables/'

inCSV = wp+"address/rnd2/address_with_uid_rnd2.csv"
ouLoc = wp+"address/rnd2"
ouDBF = "address_with_uid_rnd2.dbf"

geocodeTable = ouLoc + '/' + ouDBF
geocodeSHP   = wp+"address/rnd2/rnd2_lion2012a.shp"
ouCSV        = wp+"address/rnd2/address_with_uid_rnd2_lion_geocode_out.csv"

print 'bring csv to dbf'
arcpy.TableToTable_conversion(inCSV,ouLoc,ouDBF)

# print 'add field for combined house number and street'
# arcpy.AddField_management(geocodeTable,"fullstreet","TEXT","#","#","#","#","NULLABLE","NON_REQUIRED","#")
###CREATED THIS FIELD IN PANDAS
# print 'calc field for combined house number and street'
# arcpy.CalculateField_management(geocodeTable,"fullstreet","!hn! + ' ' +  !street!","PYTHON_9.3","#")

print 'geocode 80-10-80 w/ 2012a LION'
arcpy.GeocodeAddresses_geocoding(geocodeTable,dd+"/GIS/Data/Municipal/USA/New_York/New_York_City/Streets/nyc_lion_2012a/lion/lion.gdb/LION Locator - BoroCode 80-10-80","Street fullstreet VISIBLE NONE;Zone boro VISIBLE NONE",geocodeSHP,"STATIC")

print 'export to csv'
arcpy.ExportXYv_stats(wp+"address/rnd2/rnd2_lion2012a.shp","FID;Status;Score;Match_type;Side;X;Y;Match_addr;ARC_Street;ARC_Zone;uid;zip;streetaddr;county;address;addressRem;hn;street;boro;suite_type;suite_num;state;bin;xcoord;ycoord;rnd1;fullstreet","SEMI-COLON",wp+"address/rnd2/address_with_uid_rnd2_lion_geocode_out.csv","ADD_FIELD_NAMES")



