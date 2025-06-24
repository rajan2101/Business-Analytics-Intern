#task 4
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Data_set 2 - Copy.csv")

# Count the frequency of each investment avenue
preferred_avenue_counts = df['Avenue'].value_counts()

# Display the most preferred investment avenue
most_preferred_avenue = preferred_avenue_counts.idxmax()
most_preferred_count = preferred_avenue_counts.max()

print("Most Preferred Investment Avenue:", most_preferred_avenue)
print("Number of Participants:", most_preferred_count)
print("\nAll Avenue Preferences:\n")
print(preferred_avenue_counts)

# Plot the bar chart
plt.figure(figsize=(6, 4))
preferred_avenue_counts.plot(kind='bar', color='lightcoral')
plt.title('Most Preferred Investment Avenues')
plt.xlabel('Investment Avenue')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
