import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd

dataset = pd.read_excel("Adidas Dataset.xlsx")
region_sales = dataset.groupby('Region')['Total Sales'].sum()

plt.figure(figsize=(10,6))
plt.bar(region_sales.index, region_sales.values, color='blue')
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")

plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{int(x):,}'))

plt.grid(axis='y')
plt.tight_layout()
plt.show()
