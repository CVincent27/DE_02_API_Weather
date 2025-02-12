import csv
import pandas as pd
df = pd.read_csv("data_csv/geo_data.csv")
print(df['lat'][0])