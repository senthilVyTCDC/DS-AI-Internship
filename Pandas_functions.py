import pandas as pd
dataset = pd.read_excel('Adidas US Sales Datasets.xlsx')
print(dataset.head())
print(dataset.shape)
print(dataset.dtypes)
print(dataset.describe())
print(dataset.columns)
print(dataset['Retailer ID','Operating Profit'])
print(dataset['Units Sold'][:15])
print(dataset[dataset['State'] == 'Texas'])
#print(dataset['Total Amount'] = dataset['Price per Units'] * dataset['Units Sold'])

print(dataset.iloc[0]) #integer location-acquire complete info about certain index
print(dataset.iloc[1:5]) #acquire complete info about range of index
print(dataset.iloc[1,2]) #acquire specific cell data

#dataset.to_csv("newDataset.csv")
#dataset.to_excel("newDataset.xlsx")
#dataset.to_csv("newDataset.csv",index=False, sep="\t")

dataset.isna().any()
dataset = dataset[dataset["Type 2"].notna()]

#MeandatasetNotNan = dataset["Speed"].fillna(dataset["Speed"].mean())

#dataset['City'] = dataset['City'].map({1: "one", 2: "two",3: "three", 4: "four",5: "five", 6: "six"}).astype(str)
#print(dataset.head(5))
