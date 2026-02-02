import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("Life Expectancy Data.csv")
print(df.head())
print(df.isnull().sum())
df= df.drop(columns = ["Status"]) #Dropping the status column
df = df.drop(columns = ["Country"])
def function_heatmap(data):
    correlation_matrix = data.corr()
    life_expectancy_corr = correlation_matrix[['Life expectancy ']]
    correlations_without_year = life_expectancy_corr.drop(['Year', 'Life expectancy '])
    result = sns.heatmap(correlations_without_year)
    return result

function_heatmap(df)
plt.tight_layout()
plt.show()