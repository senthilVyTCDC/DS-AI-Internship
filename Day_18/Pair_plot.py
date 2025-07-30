import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_excel("Adidas Dataset.xlsx")

sns.pairplot(dataset[['Units Sold', 'Total Sales', 'Operating Profit', 'Price per Unit']], diag_kind='kde')
plt.tight_layout()
plt.show()
