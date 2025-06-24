#task 9
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Data_set 2 - Copy.csv")

# Column containing investment return expectations
expectation_col = 'Expect'

# Count the frequency of each expectation
expectation_counts = df[expectation_col].value_counts()

# Print summary
print("Common Investment Expectations:\n")
print(expectation_counts)

# Plot bar chart
plt.figure(figsize=(6, 4))
expectation_counts.plot(kind='bar', color='orchid')
plt.title('Investment Return Expectations')
plt.xlabel('Expected Return Range')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()