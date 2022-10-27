import dask.dataframe as dd 
import csv
import os 

def split_dbfiles(db_file_name): 
    psdr2_source_path = "../1_catalogs/panSTARRS/db_data/"+db_file_name+".db.csv" 


    chunk_size = 500000

    os.mkdir(db_file_name) 
    def write_chunk(part, lines):
        with open(db_file_name+'/'+ str(part) +'.csv', 'w') as f_out:
            f_out.write(header)
            f_out.writelines(lines)

    with open(psdr2_source_path) as f:
        count = 0
        header = f.readline()
        lines = []
        for line in f:
            count += 1
            lines.append(line)
            if count % chunk_size == 0:
                write_chunk(count // chunk_size, lines)
                lines = []
        # write remainder
        if len(lines) > 0:
            write_chunk((count // chunk_size) + 1, lines)


split_dbfiles("SOV_05.00")