import pandas as pd

COUNTRY_OR_AREA = 'country_or_area'
YEAR = 'year'
VALUE = 'value'
CATEGORY = 'category'
OUTPUTCSV = 'output.csv'
DATASET = 'greenhouse_gas_inventory_data_data.csv'
# this file is used to clean and format the data for the service to consume.

df = pd.read_csv(DATASET)

countryList = list(df[COUNTRY_OR_AREA].unique())

f = open('country.csv' , 'w')

for i in countryList:
    f.write(i + '\n')
f.close()

#print all the distinct categories
categoryArr = list(df[CATEGORY].unique())

# changet the name of the coloumn of gases for better readablility
shortCategoryList = ["CO2","GHG(Indirect CO2)","GHG","HFC","CH4","NF3","N2O","PFC","SF6","HFC+PFC"]

datasetDict = {}

countryYearList = []

# Create a dist of country+year+category , list of country+year
for index,row in df.iterrows():
    country = row[COUNTRY_OR_AREA]
    year = row[YEAR]
    values = row[VALUE]
    category = row[CATEGORY]
    datasetDict[country + ','+ str(year) + category] = values
    countryYearList.append(country + ',' + str(year))

countryYearList = set(countryYearList)
countryYearList = sorted(list(countryYearList))

# Open a csv in write mode
f = open(OUTPUTCSV , 'w')

# Add the columnName to the CSV
f.write('country,year')
for i in categoryArr:
    f.write(',' + shortCategoryList[categoryArr.index(i)])
f.write('\n')

# Insert the values into CSV
for i in countryYearList:
    valueRow = i
    for category in categoryArr:
        valueRow = valueRow + ',' + str(datasetDict.get(i + category , 'null'))
    f.write(valueRow)
    f.write('\n')

f.close()