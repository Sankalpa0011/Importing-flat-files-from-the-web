# Import packages
import matplotlib.pyplot as plt
import pandas as pd
from urllib.request import urlretrieve

# Assign url of file: url
url = "https://assets.datacamp.com/production/course_1606/datasets/winequality-red.csv"

# Read file into a DataFrame: df
urlretrieve(url, "winequality-red.csv")
df = pd.read_csv("winequality-red.csv", sep=':')

# Print the head of the DataFrame
print(df.head())

# Plot first column of df
df.iloc[:, 0].hist()
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('count')
plt.show()