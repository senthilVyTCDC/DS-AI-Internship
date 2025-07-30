import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set()

dataset = pd.read_excel("Adidas Dataset.xlsx")
region_sales = dataset.groupby('Region')['Total Sales'].sum()

plt.figure(figsize=(10,6))
plt.bar(region_sales.index, region_sales.values, color='blue')
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.grid(axis='y')
plt.tight_layout()
plt.show()
