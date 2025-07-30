import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_excel("Adidas Dataset.xlsx")

sns.scatterplot(x='Units Sold', y='Operating Profit', hue='Sales Method', data=dataset)
plt.tight_layout()
plt.show()
