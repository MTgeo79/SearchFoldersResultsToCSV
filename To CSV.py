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



##def FindField(fc)
##    if len(arcpy.ListFields(fc,"NAME"))>0:
##        FldName = "NAME"
##    Elif len(arcpy.ListFields(fc,"LABEL"))>0:
##        FldName = "LABEL"
##    Elif len(arcpy.ListFields(fc,"NOTES"))>0:
##        FldName = "NOTES"
##    Elif len(arcpy.ListFields(fc,"SEED_MIX"))>0:
##        FldName = "SEED_MIX"
##    Elif len(arcpy.ListFields(fc,"Range"))>0:
##        FldName = "Range"
##    Elif len(arcpy.ListFields(fc,"PROJECT_NAME"))>0:
##        FldName = "PROJECT_NAME"
##    Elif len(arcpy.ListFields(fc,"ORGINAL_L"))>0:
##        FldName = "ORGINAL_L"
##    Elif len(arcpy.ListFields(fc,"WETLAND_TYPE"))>0:
##        FldName = "WETLAND_TYPE"
##    Elif len(arcpy.ListFields(fc,"Dist_Type"))>0:
##        FldName = "Dist_Type"
##    Elif len(arcpy.ListFields(fc,"PROJECT_NAME"))>0:
##        FldName = "PROJECT_NAME"
##    Elif len(arcpy.ListFields(fc,"Lessee"))>0:
##        FldName = "Lessee"
##    Elif len(arcpy.ListFields(fc,"label"))>0:
##        FldName = "label"
##    Elif len(arcpy.ListFields(fc,"MINENAME"))>0:
##        FldName = "MINENAME"
##    Elif len(arcpy.ListFields(fc,"Project_Name"))>0:
##        FldName = "Project_Name"
##    Elif len(arcpy.ListFields(fc,"Plot_Name"))>0:
##        FldName = "Plot_Name"
##    Elif len(arcpy.ListFields(fc,"PitName"))>0:
##        FldName = "PitName"
##    Else


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

        if len(arcpy.ListFields(fc,"NAME"))>0:
##            print(path)
            with arcpy.da.SearchCursor(fc, ['NAME']) as sc:
                for row in sc:
                    data = row[0]
                    createCSV(data, csvname)




#sql = "LABEL = 'POTENTIAL AZTEC GILA & BRACK'S CACTUS'"
