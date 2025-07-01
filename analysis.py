import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file
df = pd.read_csv('your_file.csv')  # Replace with your file name

# Explore the data
print(df.head())
print(df.info())
print(df.describe())

# Clean the data
print("Missing values:\n", df.isnull().sum())
df = df.dropna()  # or use fillna()

# Analyze a column
print("Value counts:\n", df['column_name'].value_counts())  # Replace column_name

# Correlation heatmap
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()
