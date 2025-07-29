import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_excel("Adidas Dataset.xlsx")

method_sales = dataset.groupby('Sales Method')['Total Sales'].sum()

plt.figure(figsize=(6,6))
plt.pie(method_sales, labels=method_sales.index, autopct='%1.1f%%', startangle=140)
plt.title("Sales by Sales Method")
plt.axis('equal')
plt.tight_layout()
plt.show()
