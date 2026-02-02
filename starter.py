import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("Life Expectancy Data.csv")
print(df.head())
print(df.isnull().sum())
sns.heatmap()