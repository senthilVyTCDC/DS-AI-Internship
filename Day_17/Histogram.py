import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_excel("Adidas Dataset.xlsx")

plt.figure(figsize=(10,6))

counts, bins, bars = plt.hist(dataset['Units Sold'], bins=10, color='orange', edgecolor='black')

plt.title("Units Sold Distribution")
plt.xlabel("Units Sold")
plt.ylabel("Frequency")
plt.grid(axis='y')

for bar, count in zip(bars, counts):
    plt.text(bar.get_x() + bar.get_width() / 2, count + 1, int(count),
             ha='center', fontsize=9)

plt.tight_layout()
plt.show()
