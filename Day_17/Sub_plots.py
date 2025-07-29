import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_excel("Adidas Dataset.xlsx")

# Define the groupby values before plotting
region_sales = dataset.groupby('Region')['Total Sales'].sum()
method_profit = dataset.groupby('Sales Method')['Operating Profit'].sum()

fig, axs = plt.subplots(1, 2, figsize=(14,5))

# Region vs Sales
axs[0].bar(region_sales.index, region_sales.values, color='cornflowerblue')
axs[0].set_title("Total Sales by Region")
axs[0].set_xlabel("Region")
axs[0].set_ylabel("Total Sales")

# Sales Method vs Operating Profit
axs[1].bar(method_profit.index, method_profit.values, color='lightgreen')
axs[1].set_title("Operating Profit by Sales Method")
axs[1].set_xlabel("Sales Method")
axs[1].set_ylabel("Operating Profit")

plt.tight_layout()
plt.show()