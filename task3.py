import pandas as pd

# Load the dataset
df = pd.read_csv("Data_set 2 - Copy.csv")

# Define numerical columns
numerical_cols = [
    'age', 'Mutual_Funds', 'Equity_Market', 'Debentures',
    'Government_Bonds', 'Fixed_Deposits', 'PPF', 'Gold'
]

# Create dictionary of stats
stats = {}

for col in numerical_cols:
    stats[col] = {
        'Mean': df[col].mean(),
        'Median': df[col].median(),
        'Standard Deviation': df[col].std()
    }

# Convert dictionary to DataFrame
stats_df = pd.DataFrame(stats).T

# Print results rounded to 2 decimal places
print(stats_df.round(2))