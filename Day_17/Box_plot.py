import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_excel("Adidas Dataset.xlsx")

plt.figure(figsize=(8,5))
dataset.boxplot(column='Units Sold', by='Sales Method')
plt.title("Units Sold by Sales Method")
plt.suptitle("")
plt.xlabel("Sales Method")
plt.ylabel("Operating Margin")
plt.tight_layout()
plt.show()
