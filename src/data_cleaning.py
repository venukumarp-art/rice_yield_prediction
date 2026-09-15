# importing the libraries ,load the dataset,fill the data by using fillna method
from config.settings import RAW_DATA_PATH
from config.settings import PROCESSED_DATA_PATH
import pandas as pd
def clean_data():
  df=pd.read_csv(RAW_DATA_PATH)
  df["land_size_acres"]=df["land_size_acres"].fillna(df["land_size_acres")].mean())
  df.to_csv(PROCESSED_DATA_PATH,index=False)
  return df
  
