import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_excel("Adidas Dataset.xlsx")

sns.countplot(x='Sales Method', data = dataset)
plt.tight_layout()
plt.show()
