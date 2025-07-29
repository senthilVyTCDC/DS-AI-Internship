import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_excel("Adidas Dataset.xlsx")

plt.figure(figsize=(8,5))
plt.scatter(dataset['Units Sold'], dataset['Operating Profit'], color='purple', s=50, alpha=0.6, edgecolor='black')
plt.title("Units Sold vs Operating Profit")
plt.xlabel("Operating Profit")
plt.ylabel("Units Sold")
plt.grid(True)
plt.tight_layout()
plt.show()
