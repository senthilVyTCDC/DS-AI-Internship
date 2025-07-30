import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_excel("Adidas Dataset.xlsx")

sns.boxplot(x='Sales Method', y='Units Sold', data=dataset)
plt.tight_layout()
plt.show()
