import pandas as pd
import kaggle
import zipfile

from kaggle.api.kaggle_api_extended import KaggleApi

# get data
api = KaggleApi()
api.authenticate()
api.dataset_download_files('x1akshay/olympics-2024', path='.', unzip=True)

# read .csv
olympics = pd.read_csv("Olympics 2024.csv")

# olympics.info()

print(olympics.columns)
print()

new_columns_dict = {
    'Competitions':'Competition_Name',
    'NOC':'Country_Name',
    'Gold':'Gold_Medals',
    'Silver':'Silver_Medals',
    'Bronze':'Bronze_Medals',
    'Total':'Total_Medals'
}

olympics.rename(new_columns_dict, axis=1, inplace=True)

olympics.info()
print()

print(olympics.head())

olympics.to_excel('olympics_2024_final.xlsx', sheet_name='Data')