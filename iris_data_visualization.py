import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", color_codes=True)
import os as os

iris = pd.read_csv("Iris.csv")
# first_5_rows = iris.head()
# print irisHead
species_count = iris["Species"].value_counts()
print species_count
iris.plot(kind="scatter", x="SepalLengthCm", y="SepalWidthCm")
sns.FacetGrid(iris, hue="Species", size=5).map(plt.scatter, "SepalLengthCm", "SepalWidthCm").add_legend()












