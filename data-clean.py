import pandas as pd

df = pd.read_csv('greenhouse_gas_inventory_data_data.csv')

#print all the distinct categories
categoryArr = list(df['category'].unique())

f = open('country.csv' , 'a')

countryList = list(df['country_or_area'].unique())

for country in countryList:
    f.write(country)
    f.write("\n")

f.close()

shortCategoryList = ["CO2","GHG(Indirect CO2)","GHG","HFC","CH4","NF3","N2O","PFC","SF6","HFC+PFC"]

d = {}

l = []

for index,row in df.iterrows():
    country = row['country_or_area']
    year = row['year']
    values = row['value']
    category = row['category']
    d[country + ','+ str(year) + category] = values
    l.append(country + ',' + str(year))

l = set(l)
l = sorted(list(l))

f = open('output.csv' , 'a')

f.write('country,year')
for i in categoryArr:
    f.write(',' + shortCategoryList[categoryArr.index(i)])
f.write('\n')

for i in l:
    s = i
    for category in categoryArr:
        s = s + ',' + str(d.get(i + category , 'null'))
    f.write(s)
    f.write('\n')

f.close()