import arcpy
import os


#commit

enviro = r"U:\My Documents\ArcGIS\ArcPyOutputFiles"

txtFile = open(enviro +"{}".format("StipPolys.txt"),"w")
txtFile.write("Polys field information" + "\n")
txtFile.write("-------------------------------------" + "\n")

arcpy.env.workspace = r"V:\tools\ArcSDE\Database Connections\5 NMSO ilmnmso3gi1 ilmnmsoclass1 (Type 1) Default.sde"

datasets = arcpy.ListDatasets("*FFO*", "Feature")
datasets = [''] + datasets if datasets is not None else []

for ds in datasets:
    for fc in arcpy.ListFeatureClasses("*FFO*", "Polygon", feature_dataset=ds):

        path = os.path.join( ds, fc)
        txtFile.write(path)

        field_list = arcpy.ListFields(fc)


        for field in field_list:
            line = "Name: {}, Type: {}, Length: {}\n".format(
                field.name, field.type, field.length)
            txtFile.write(line)

txtFile.close()

print("Script completed")