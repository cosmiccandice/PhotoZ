import pandas as pd


sdss  = pd.read_csv("../1_catalogs/sdss_table.csv")
print(sdss[0:20]) 

psdr2 =pd.read_csv("../1_catalogs/panSTARRS/db_data/SOV_05.00.db.csv") 
print (psdr2[0:20])