######@@@ Author: Venu Kumar P@@@@@@@@@@@####
from src.data_cleaning import clean_data
from src.train_data import train_model
from src.prediction import predict_rice_packets
def main():
  df=clean_data()
  train_model(df)
  predict_rice_packets()
if __name__=="__main__":
   main()
  
  


