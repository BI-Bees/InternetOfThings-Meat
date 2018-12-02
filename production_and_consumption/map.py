import csv
import pandas as pd
import pygal

countries_file_name = "countries.csv"
countries_file_name = pd.read_csv(countries_file_name, delimiter=",")

production_file_name = "modifiedMeatProduction.csv"
production_file_name = pd.read_csv(production_file_name, delimiter=",")


def map_page():
    df = production_file_name
    df_country = countries_file_name()
    map = create_data_map(df, df_country)
    return render_template("map.html", data=map.render_data_uri())


def create_data_map(df, df_country):
    worldmap_chart = pygal.maps.world.World()
    worldmap_chart.title = 'Produced 3D-Printers per Country'

    df_map = df.Country.unique()
    for countries in df_map:
        worldmap_chart.add(countries + ' ' + str(df.Country.value_counts()[countries]), {
            countries.lower(): df.Country.value_counts()[countries]
        })
    
    return worldmap_chart
