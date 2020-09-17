import pandas as pd
import os, glob

path = "C:\Users\Dennis Besseling\PycharmProjects\work_projects\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data"

all_data = glob.glob(os.path.join(path, "Sales_*.csv"))
data_merged = pd.concat(df_from_each_file, ignore_index=True)
data_merged = (pd.read_csv(f, sep=',') for f in all_files)
data_merged.to_csv('merged_data.csv')