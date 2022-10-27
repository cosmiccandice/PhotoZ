from astroquery.sdss import SDSS
import sqlite3 as db
import csv


sdss_query = """
SELECT
z,zerr,zwarning,class,subclass,survey,type,objid,specobjid, ra, dec
FROM SpecPhoto 
WHERE 
 (class = 'QSO') OR (class= 'GALAXY')
""" 

#save data
data = SDSS.query_sql(sdss_query)


#create csv
table_name = 'sdss_table.csv'

with open(table_name, 'w', newline='') as f_handle:
    writer = csv.writer(f_handle)
    # Add the header/column names
    header = ['z','zerr','zwarning','class','subclass','survey,','type','objid','specobjid','ra','dec']
    writer.writerow(header)
    # Iterate over `data`  and  write to the csv file
    for row in data:
        writer.writerow(row)