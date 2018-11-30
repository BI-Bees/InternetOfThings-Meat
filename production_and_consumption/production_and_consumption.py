import csv
import pandas as pd

production_file_name = "modifiedMeatProduction.csv"
production_dataframe = pd.read_csv(production_file_name, delimiter=",")

consumption_file_name = "modifiedMeatConsumption.csv"
consumption_dataframe = pd.read_csv(consumption_file_name, delimiter=",")
consumption_country_list = consumption_dataframe.Country.unique().tolist()
consumption_year_list = consumption_dataframe.Year.unique().tolist()

# Matching on countries & year
production_dataframe = production_dataframe[production_dataframe['Country'].isin(consumption_country_list)]
production_dataframe = production_dataframe[production_dataframe['Year'].isin(consumption_year_list)]

#production_country_list = production_dataframe.Country.unique().tolist()
#production_year_list = production_dataframe.Year.unique().tolist()

#consumption_dataframe = consumption_dataframe[consumption_dataframe['Country'].isin(production_country_list)]
#consumption_dataframe = consumption_dataframe[consumption_dataframe['Year'].isin(production_year_list)]

print(production_dataframe)

def create_csv():
    with open('production_and_consumption.csv', 'w', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['Country', 'Year', 'Production', 'Consumption'])