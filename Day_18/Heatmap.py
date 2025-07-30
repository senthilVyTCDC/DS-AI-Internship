import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_excel("Adidas Dataset.xlsx")

sns.heatmap(dataset.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.tight_layout()
plt.show()
