import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from typing import Union

class DataProcessing:
    def __init__(self, df):
        self.df = df
    
    def identify_outliers(self, data: pd.DataFrame):
        """
        function to identify outliers in data using box plot visualization.
        Parameters:
        data (pd.DataFrame): The data to be visualized

        Returns:
        None
        """
        fig, ax = plt.subplots()
        print(fig, ax)
        print(data)

        ax.boxplot(data, label=["tv spending", "sales"])
        ax.set_title("box plot data")
        ax.set_ylabel("value")
        plt.show()
        plt.savefig('./temp/boxplot.png')
    
    def identify_outliers_zscore(self, data: pd.Series, threshold: float = 3) -> pd.Series:

        z_score = (data - data.mean() ) / data.std() 
        outliers =data[np.abs(z_score) > threshold]
        return outliers

        