#task 7
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Data_set 2 - Copy.csv")

# Column containing information source
info_source_col = 'Source'

# Count each source's frequency
source_counts = df[info_source_col].value_counts()

# Print results
print("Common Information Sources:\n")
print(source_counts)

# Create bar plot
plt.figure(figsize=(6, 4))
source_counts.plot(kind='bar', color='orange')
plt.title('Common Investment Information Sources')
plt.xlabel('Source')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()