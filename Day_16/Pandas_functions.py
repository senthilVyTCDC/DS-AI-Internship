import pandas as pd

dataset = pd.read_excel('Adidas Dataset.xlsx')
print("Head: ",dataset.head())
print("\nShape: ",dataset.shape)
print("\ndtypes: ",dataset.dtypes)
print("\nDescribe: ",dataset.describe())
print("\nColumns: ",dataset.columns)
print("\nMultiple Columns: ",dataset[['Retailer ID','Operating Profit']])
print("\nLimited Data: ",dataset['Units Sold'][:15])
print("\nSelection Data: ",dataset[dataset['State'] == 'Texas'].head(5))

dataset['Total Amount'] = dataset['Price per Unit'] * dataset['Units Sold']
print("\nNew Column: ",dataset['Total Amount'])

print("\niloc[0]: ",dataset.iloc[0])
print("\niloc[1:5]: ",dataset.iloc[1:5])

print("\nNull Values: ",dataset.isna().any())
dataset = dataset[dataset["Units Sold"].notna()]
print("\nNot Null values: ",dataset)

MeandatasetNotNan = dataset["Units Sold"].fillna(dataset["Units Sold"].mean())
print("\nMean for Null: ",MeandatasetNotNan)

codes, uniques = pd.factorize(dataset['City'])
for i, city in enumerate(uniques):
    i+1
print("\nValue Label Encoder: ",dataset.head(5))

dataset.rename(columns = {'Operating Profit':'Profit'}, inplace = True)
print("\nRenaming Column: ",dataset.columns)
dataset.drop('Invoice Date', axis=1, inplace=True)
print("\nDropping Column: ",dataset.columns)

print("\nCount: ",dataset['Sales Method'].value_counts())
print("\nSorted Data: ",dataset.sort_values(by='Units Sold'))

dataset.to_csv("newDataset.csv")

