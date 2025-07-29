import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker

dataset = pd.read_excel("Adidas Dataset.xlsx")

daily_sales = dataset.groupby('Invoice Date')['Total Sales'].sum()

plt.figure(figsize=(10,5))
plt.plot(daily_sales.index, daily_sales.values, linestyle='-', color='green')
plt.title("Daily Total Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.grid(True)

plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{int(x):,}'))

plt.tight_layout()
plt.show()
