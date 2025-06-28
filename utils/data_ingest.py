import pandas as pd
import numpy as np
from typing import Tuple
class DataIngest:
    def __init__(self, file_path) -> None:
        self.file_path = file_path


    def load_data(self) -> pd.DataFrame :
        data = pd.read_csv(self.file_path)
        return data
    
    def get_X_y(self) -> Tuple[pd.Series, pd.Series, pd.DataFrame]:      
        data = self.load_data()
        X = data["TV"]
        y = data["Sales"]
        df = pd.concat([X,y], axis=1)
        return X, y, df
    
    