# Seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

ds = sbn.load_dataset("tips")
# print(ds)
# plt.subplot(1, 2, 1)
ds.boxplot(by='day', column=['total_bill'], grid=False)

titanic = sbn.load_dataset("titanic")
age = titanic['age'].dropna()
# plt.subplot(1, 2, 1)
sbn.displot(age, bins=30, kde=False)

plt.show()