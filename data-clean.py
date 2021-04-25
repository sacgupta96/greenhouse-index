import pandas as pd

# this file is used to clean and format the data for the service to consume.

df = pd.read_csv('greenhouse_gas_inventory_data_data.csv')

#print all the distinct categories
categoryArr = list(df['category'].unique())

# changet the name of the coloumn of gases for better readablility
shortCategoryList = ["CO2","GHG(Indirect CO2)","GHG","HFC","CH4","NF3","N2O","PFC","SF6","HFC+PFC"]

d = {}

l = []

# Create a dist of country+year+category , list of country+year
for index,row in df.iterrows():
    country = row['country_or_area']
    year = row['year']
    values = row['value']
    category = row['category']
    d[country + ','+ str(year) + category] = values
    l.append(country + ',' + str(year))

l = set(l)
l = sorted(list(l))

# Open a csv in append form
f = open('output.csv' , 'a')

# Add the columnName to the CSV
f.write('country,year')
for i in categoryArr:
    f.write(',' + shortCategoryList[categoryArr.index(i)])
f.write('\n')

# Insert the values into CSV
for i in l:
    s = i
    for category in categoryArr:
        s = s + ',' + str(d.get(i + category , 'null'))
    f.write(s)
    f.write('\n')

f.close()