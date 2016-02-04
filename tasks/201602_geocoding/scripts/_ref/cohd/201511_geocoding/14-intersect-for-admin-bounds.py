import arcpy

from _settings import *

wind = "W:" #Windows drive
#dd   = "Z:/Dropbox/" #Dropbox drive
pp = '/GIS/projects/cohd/'

wd = wind + pp + tf

wdi = wind + pp + 'data/input/'

wi = wd + 'data/input/'
wp = wd + 'data/processing/'
wo = wd + 'data/output/'
wt = wd + 'data/tables/'

print 'intersect with boro'
arcpy.Intersect_analysis(wd+"data/output/geocoded/uid.shp #;"+wdi+"boro_boundary/nybb.shp #",wp+"intersects/boro/uid_boro_int.shp","ALL","#","INPUT")
print 'intersect with community districts'
arcpy.Intersect_analysis(wd+"data/output/geocoded/uid.shp #;"+wdi+"community_districts/nycd.shp #",wp+"intersects/community_districts/uid_cd_int.shp","ALL","#","INPUT")
print 'intersect with census block 2000'
arcpy.Intersect_analysis(wd+"data/output/geocoded/uid.shp #;"+wdi+"census/nycb2000.shp #",wp+"intersects/census/uid_cb2000_int.shp","ALL","#","INPUT")
print 'intersect with census block 2010'
arcpy.Intersect_analysis(wd+"data/output/geocoded/uid.shp #;"+wdi+"census/nycb2010.shp #",wp+"intersects/census/uid_cb2010_int.shp","ALL","#","INPUT")

print 'export all to csv'
arcpy.ExportXYv_stats(wp+"intersects/boro/uid_boro_int.shp","uid;FID_nybb;BoroCode;BoroName;Shape_Leng;Shape_Area","COMMA",wp+"intersects/boro/uid_boro_int.csv","ADD_FIELD_NAMES")
arcpy.ExportXYv_stats(wp+"intersects/census/uid_cb2000_int.shp","uid;FID_nycb20;BCTCB2000;CB2000;BoroCode;BoroName;CT2000;Shape_Leng;Shape_Area;geoid","COMMA",wp+"intersects/census/uid_cb2000_int.csv","ADD_FIELD_NAMES")
arcpy.ExportXYv_stats(wp+"intersects/census/uid_cb2010_int.shp","uid;FID_nycb20;CB2010;BoroCode;BoroName;CT2010;BCTCB2010;Shape_Leng;Shape_Area;geoid","COMMA",wp+"intersects/census/uid_cb2010_int.csv","ADD_FIELD_NAMES")
arcpy.ExportXYv_stats(wp+"intersects/community_districts/uid_cd_int.shp","uid;FID_nycd;BoroCD;Shape_Leng;Shape_Area","COMMA",wp+"intersects/community_districts/uid_cd_int.csv","ADD_FIELD_NAMES")