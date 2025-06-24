#task 8
import pandas as pd

# Load the dataset
df = pd.read_csv("Data_set 2 - Copy.csv")

# Define a mapping from categorical ranges to numerical values (approximate midpoints)
duration_mapping = {
    "Less than 1 year": 0.5,
    "1-3 years": 2,
    "3-5 years": 4,
    "More than 5 years": 6
}

# Replace categorical values with numerical approximations
df['Duration_Years'] = df['Duration'].map(duration_mapping)

# Calculate the average investment duration
average_duration = df['Duration_Years'].mean()

print(f"Average Investment Duration: {average_duration:.2f} years")
