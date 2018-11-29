import csv
import wget
import pandas as pd

dataframe = pd.read_csv("MeatSupply.csv", delimiter = ",")
lessdata = dataframe[['Country', 'Year', 'Value']]
country = ''

# Creating lists
country_list = lessdata.Country.unique().tolist()
year_list = lessdata.Year.unique().tolist()

#print(country_year)




def findSum(country, year):
    country_mask = lessdata['Country'] == country
    year_mask = lessdata['Year'] == year
    return lessdata[(country_mask) & (year_mask)].Value.sum()

for country_row in country_list:
    for year_row in year_list:
        print(country_row, year_row, findSum(country_row, year_row))
        
#print(findSum('Denmark', 2000))

# def findCountries():
#     country_list
#     country_mask = lessdata['Country'].tolist()
#     country = country_mask[0]
#     for item in country_mask:
#         if (country != item):
#             country = item
            #country_list = country_list + item
    #return country_list

# findCountries()


# countryname = lessdata[lessdata['Country']]
# print(countryname)


#print(lessdata.Value.sum())



# 1st Qeustion regarding all meat consumption per country
# mCCountry = {}
# count = 0

# #Code for a single year
# with open('MeatSupply.csv') as data:
#     reader = csv.reader(data)
#     header_row = next(reader)
    
#     for row in reader:
#         country = row[3]
#         year = row[8]
#         meatConsumption = 0
#         if(year == '1991'):
#             meatConsumption += float(row[11])

#         if country not in mCCountry.keys():
#             mCCountry[country] = meatConsumption
#             count = count + 1

#         else:
#             mCCountry[country] += meatConsumption

#     mCCountry_sorted = sorted(mCCountry, key=mCCountry.get, reverse = True)

#     print(mCCountry)