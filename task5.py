#task 5
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Data_set 2 - Copy.csv")

# List of columns with reasons
reason_columns = ['Reason_Equity', 'Reason_Mutual', 'Reason_Bonds', 'Reason_FD']

# Combine all reason columns into a single Series
all_reasons = pd.Series(dtype=str)
for col in reason_columns:
    all_reasons = pd.concat([all_reasons, df[col]])

# Count the frequency of each reason
reason_counts = all_reasons.value_counts()

# Print the top 10 reasons
print("Top Reasons for Investment:\n")
print(reason_counts.head(10))

# Plot a bar chart of the top 10 reasons
plt.figure(figsize=(8, 5))
reason_counts.head(10).plot(kind='bar', color='mediumseagreen')
plt.title('Top 10 Reasons for Investment')
plt.xlabel('Reason')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()