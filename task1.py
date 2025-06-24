#task 1
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Data_set 2 - Copy.csv')
print(df['gender'].value_counts())

gender_counts = df['gender'].value_counts()
