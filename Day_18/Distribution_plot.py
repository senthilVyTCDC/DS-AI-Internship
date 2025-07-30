import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_excel("Adidas Dataset.xlsx")

sns.histplot(dataset['Units Sold'], kde=True)
plt.tight_layout()
plt.show()
