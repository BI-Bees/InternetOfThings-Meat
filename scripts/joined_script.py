import csv
import pandas as pd

consumption_file_name = "../dataset/modified_consumption.csv"
consumption = pd.read_csv(consumption_file_name, delimiter=",")

production_file_name = "../dataset/modified_production.csv"
production = pd.read_csv(production_file_name, delimiter=",")

countries_file_name = "../dataset/countries.csv"
countries = pd.read_csv(countries_file_name, delimiter=",")

#matching_data = pd.merge(left=production, right=consumption, on=['Country','Year'])
#matching_data.to_csv('../dataset/joined.csv', sep =',')

joined_file_name = "../dataset/joined.csv"
joined = pd.read_csv(joined_file_name, delimiter=",")

matching_data2 = pd.merge(left=joined, right=countries, on=['Country'])
matching_data2.to_csv('../dataset/joined_w_countries.csv', sep =',')
