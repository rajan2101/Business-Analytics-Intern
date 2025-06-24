#task 6
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Data_set 2 - Copy.csv")

# Column name containing savings objectives
savings_col = 'What are your savings objectives?'

# Count each objective's frequency
savings_objectives_counts = df[savings_col].value_counts()

# Print results
print("Savings Objectives:\n")
print(savings_objectives_counts)

# Bar plot for visual representation
plt.figure(figsize=(6, 4))
savings_objectives_counts.plot(kind='bar', color='skyblue')
plt.title('Savings Objectives Distribution')
plt.xlabel('Savings Objective')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
