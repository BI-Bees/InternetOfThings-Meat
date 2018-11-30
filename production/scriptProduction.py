import csv
import pandas as pd

file_name = "originalMeatProduction.csv"
dataframe = pd.read_csv(file_name, delimiter=",")
lessdata = dataframe[['Country', 'Year', 'Value']]

# Creating lists
country_list = lessdata.Country.unique().tolist()
year_list = lessdata.Year.unique().tolist()


def find_sum(country, year):
    country_mask = lessdata['Country'] == country
    year_mask = lessdata['Year'] == year
    return lessdata[(country_mask) & (year_mask)].Value.sum()


def create_csv():
    with open('modifiedMeatProduction.csv', 'w', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['Country', 'Year', 'Production'])
        for country_row in country_list:
            for year_row in year_list:
                csv_writer.writerow(
                    [country_row, year_row, find_sum(country_row, year_row)])
