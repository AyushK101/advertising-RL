import pandas as pd
import matplotlib.pyplot as plt
from utils import DataIngest
from utils import DataProcessing
from utils import SimpleLinearRegression

if __name__ == "__main__":
    data_ingest = DataIngest("./data/Advertising.csv");

    X, y, df = data_ingest.get_X_y()
    df.to_csv("./data/simple_df.csv",index=False)

    # print(X, y, df)
     
     
    data_process = DataProcessing(df)
    data_process.identify_outliers(df)

    data_process.identify_outliers_zscore(df["TV"])

    lr_model = SimpleLinearRegression(X,y)
    lr_model.summary()

