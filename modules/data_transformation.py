import os
from dataclasses import dataclass
from pathlib import Path

from google.cloud import storage
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import xarray as xr
import matplotlib.pyplot as pyplot

@dataclass
class DataIngestionConfig:
    # Sync to GCP Bucket
    swh_data: str = ""
    market_data: str = ""
    heatmap_data: str = ""
    weather_data: str = ""

# Processing for Dataset from GCP 
class DataIngestion():
    def __init__(self):
        self._data_config = DataIngestionConfig()


class DataTransformation:
    def __init__(self, file_path: Path):
        self._file_path = file_path
        self._data_info = []

    def __str__(self) -> str:
        return "\n".join(
            "".format(
                **info
            )
            for info in self._data_info
        )

    def _data_preprocessing_csv(self):
        INFO = {}
        df = pd.read_csv("WILL READ THE CSV FILE. REPLACE IT")
        INFO["Total_Data"] = len(df)
        INFO["NaN_Data"] = df.isna().sum()
        INFO["%_NaN_Data"] = (int(INFO["NaN_Data"]) / int(INFO["Total_Data"])) * 100

        self._data_info.append(INFO)

    
    def _data_preprocessing_nc(self):
        INFO = {}

        df = xr.open_dataset("FILE_NAME.nc")


    def _data_preprocessing_xlsx(self):
        INFO = {}; PATH = []
        df = pd.read_excel("FILE_NAME.xlsx")

    def _data_splitting(self):

        X_train = ""
        y_train = ""
        X_val = ""
        y_val = ""
        train = ""
        val = ""
        test = ""
        j = ""

        return X_train, y_train, X_val, y_val, train, val, test ,j





