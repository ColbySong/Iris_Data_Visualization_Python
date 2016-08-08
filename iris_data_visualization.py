import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", color_codes=True)

iris = pd.read_csv("Iris.csv")

# Count the sample size each specie
species_count = iris["Species"].value_counts()
print species_count

# Pandas package scatter plot
iris.plot(kind="scatter", x="SepalLengthCm", y="SepalWidthCm")

# Seaborn package scatter plot that labels each species data with different colour
# used for idenitfying bivariate relationships
sns.FacetGrid(iris, hue="Species", size=5).map(plt.scatter, "SepalLengthCm", "SepalWidthCm").add_legend()

# Seaborn package Box plot
# useful for exploring univariate relationships
sns.boxplot(x="Species", y="PetalLengthCm", data=iris)

# Seaborn Kdeplot - plots density of feature measurements
# useful for exploring univariate relationships
sns.FacetGrid(iris, hue="Species", size=6).map(sns.kdeplot, "PetalLengthCm").add_legend()

# Pandas Radviz - puts each feature on 2D plane, based on spring tension minimization algorithm
# useful for multivariate visualization
from pandas.tools.plotting import radviz
radviz(iris.drop("Id", axis=1), "Species")

# Seaborn pairplot - plots all pairs of features
# useful for exploring bivariate relationships
sns.pairplot(iris.drop("Id", axis=1), hue="Species")














