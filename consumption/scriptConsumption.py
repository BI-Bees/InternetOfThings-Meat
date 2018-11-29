import csv
import pandas as pd

file_name = "originalMeatConsumption.csv"
dataframe = pd.read_csv(file_name, delimiter=",")
lessdata = dataframe[['Country', 'TIME', 'Measure', 'Value']]
country = ''

# Creating lists
country_list = lessdata.Country.unique().tolist()
year_list = lessdata.TIME.unique().tolist()
measure_list = lessdata.Measure.tolist()

# print(measure_list)


def find_sum(country, year):
    #if measure == 'Kilograms/capita':
    country_mask = lessdata['Country'] == country
    year_mask = lessdata['TIME'] == year
    return lessdata[(country_mask) & (year_mask)].Value.sum()


def create_csv():
    with open('modifiedMeatConsumption.csv', 'w', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['Country', 'Year', 'Consumption'])
        for measure_row in measure_list:
            if measure_row == 'Kilograms/capita':
                for country_row in country_list:
                    for year_row in year_list:
                        csv_writer.writerow([country_row, year_row, find_sum(country_row, year_row)])


            #print(measure_row)
            #for country_row in country_list:
                
                    #print(measure_row)
                    
                    


create_csv()

# consumptioncsvurl = "https://stats.oecd.org/sdmx-json/data/DP_LIVE/.MEATCONSUMP.../OECD?contentType=csv&amp;detail=code&amp;separator=comma&amp;csv-lang=en"
# #codeline1 = 'wget -cn consmptioncsvurl'
# #filename = wget.download(consumptioncsvurl)
# filename = 'DP_LIVE_22112018110209786.csv'

# # 1st Qeustion regarding all meat consumption per country
# mCCountry = {}

# # we count the countries we get in order to compare production and consumption
# countriescount = 0

# # Linear progression


# #report


# #read
# dataframe = pd.read_csv(filename, delimiter=',')

# #process
# lessdata = dataframe[['Country', 'TIME', 'Measure','Value']]
# lessdata.columns = ['Country', 'Year', 'Measure' , 'Value']
# print(lessdata)
# # country_mask = lessdata['Country'] == country
# # year_mask = lessdata['Year'] == year
# # lessdata[(country_mask) & (year_mask)]

# #get all countries that our "consumption" dataset has in order to compare to the production one
# #reason: less countries in this dataset
# country_list = lessdata.Country.unique().tolist()
# # print(country_list)

# # list of countries
# # ['Australia', 'Canada', 'Japan', 'Korea', 'Mexico', 'New Zealand', 'Turkey', 'United States', 'Algeria', 'Argentina', 'Bangladesh', 'Brazil',
# # 'Chile', "China (People's Republic of)", 'Colombia', 'Egypt', 'Ethiopia', 'Ghana', 'Haiti', 'India', 'Indonesia', 'Iran', 'Israel', 'Kazakhstan',
# #  'Malaysia', 'Mozambique', 'Nigeria', 'Pakistan', 'Paraguay', 'Peru', 'Philippines', 'Russia', 'Saudi Arabia', 'South Africa', 'Sudan', 'Tanzania',
# #  'Thailand', 'Ukraine', 'Uruguay', 'Viet Nam', 'Zambia', 'World', 'Sub-Saharan Africa', 'OECD - Total', 'BRICS', 'European Union (28 countries)', 'Norway', 'Switzerland']

# #Code for a single year
# # with open(filename) as data:
# #     reader = csv.reader(data)
# #     header_row = next(reader)

# #     for row in reader:
# #         country = row[1]
# #         year = row[11]
# #         measure = row[7]
# #         value = float(row[12])

# #         meatConsumption = 0.0
# #         if(year == "2000" and measure == "Kilograms/capita"):
# #             meatConsumption += value

# #         if country not in mCCountry.keys():
# #             mCCountry[country] = meatConsumption
# #             countriescount += 1
# #         else:
# #             mCCountry[country] += meatConsumption

# #     mCCountry_sorted = sorted(mCCountry, key=mCCountry.get, reverse = True)

# #     print(mCCountry_sorted)
# #     print(mCCountry)
# #     print(countriescount)
# # countries: 48
