import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker

dataset = pd.read_excel("Adidas Dataset.xlsx")
top_products = dataset.groupby('Product')['Total Sales'].sum().nlargest(5)

plt.figure(figsize=(8,5))
plt.bar(top_products.index, top_products.values, color='teal')
plt.title("Top 5 Products by Total Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=30)

plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{int(x):,}'))

plt.tight_layout()
plt.show()
