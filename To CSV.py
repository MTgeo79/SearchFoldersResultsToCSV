#-------------------------------------------------------------------------------
# Name:        ToCSV
# Purpose:
#
# Author:      mthornton
#
# Created:     13/08/2019
# Copyright:   (c) mthornton 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def FindField(fc):
    field_list = [
        "NAME", "LABEL", "NOTES", "SEED_MIX", "Range", "PROJECT_NAME", "ORIGINAL_L",
        "WETLAND_TYPE", "Dist_Type", "Lessee", "MINENAME", "Plot_Name", "PitName", "ObjectID"
    ]
    fields = [fld.name.upper() for fld in arcpy.ListFields(fc)] #returns all filenames for current fc
    return next(f for f in field_list if f.upper() in fields)



def createCSV(data, csvname, mode ='ab'):
    with open(csvname, mode) as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(data)


import arcpy
import csv
import os


csvname = r"U:\My Documents\ArcGIS\ArcPyOutputFiles\TestFile4.csv"
headers = 'Name', 'Path'
createCSV(headers, csvname, 'wb')

arcpy.env.workspace = r"V:\tools\ArcSDE\Database Connections\5 NMSO ilmnmso3gi1 ilmnmsoclass1 (Type 1) Default.sde"

datasets = arcpy.ListDatasets("*FFO*", "Feature")
datasets = [''] + datasets if datasets is not None else []

for ds in datasets:
    for fc in arcpy.ListFeatureClasses("*FFO*", "Polygon", feature_dataset=ds):

        path = os.path.join( ds, fc)
        createCSV(path, csvname)
        
        FldName = FindField(fc)
            
        with arcpy.da.SearchCursor(fc, [FldName, SHAPE@XY]) as sc:
            for row in sc:
                name = row[0]
                locationX = row[1][0]
                locationY = row[1][1]
                data = name, locationX, locationY
                createCSV(data, csvname)





#sql = "LABEL = 'POTENTIAL AZTEC GILA & BRACK'S CACTUS'"
