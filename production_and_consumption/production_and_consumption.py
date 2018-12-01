import csv
import pandas as pd

production_file_name = "modifiedMeatProduction.csv"
production_dataframe = pd.read_csv(production_file_name, delimiter=",")

consumption_file_name = "modifiedMeatConsumption.csv"
consumption_dataframe = pd.read_csv(consumption_file_name, delimiter=",")

matching_data = pd.merge(left=production_dataframe, right=consumption_dataframe, on=['Country','Year'])
matching_data.to_csv('joineddata.csv', sep =',')

