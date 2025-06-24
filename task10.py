#task 10
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Data_set 2 - Copy.csv")

# Map 'Duration' to numeric values (midpoints)
duration_mapping = {
    "Less than 1 year": 0.5,
    "1-3 years": 2,
    "3-5 years": 4,
    "More than 5 years": 6
}
df['Duration_Years'] = df['Duration'].map(duration_mapping)

# Map 'Expect' to numeric values
expect_mapping = {
    "10%-20%": 15,
    "20%-30%": 25,
    "Above 30%": 35
}
df['Expected_Return'] = df['Expect'].map(expect_mapping)

# Select relevant numeric columns
corr_df = df[['age', 'Duration_Years', 'Expected_Return']]

# Calculate correlation matrix
correlation_matrix = corr_df.corr()

# Print correlation values
print("Correlation Matrix:\n")
print(correlation_matrix)

# Visualize with heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Between Investment Factors')
plt.tight_layout()
plt.show()
