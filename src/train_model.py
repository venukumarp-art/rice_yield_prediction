import joblib
from sklearn.linear_model import LinearRegression
from config.settings import MODEL_PATH
def train_model(df):
  X=df[["land_size_acres"]].values
  y=df["rice_packets"].values
  model=LinearRegression()
  model.fit(X,y)
  joblib.dump(model,MODEL_PATH)# save the model to a pickle file
  
  
  
