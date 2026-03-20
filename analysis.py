import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Dataset  (1).csv')

# Task 1: Rating Distribution
df['Rating Range'] = pd.cut(df['Aggregate rating'],
                             bins=[0, 1, 2, 3, 4, 5],
                             labels=['0-1', '1-2', '2-3', '3-4', '4-5'])

most_common = df['Rating Range'].value_counts().idxmax()
print("Rating Range Distribution:")
print(df['Rating Range'].value_counts().sort_index())
print(f"\nMost Common Rating Range: {most_common}")

# Task 2: Average Votes
avg_votes = df['Votes'].mean()
print(f"\nAverage Number of Votes: {avg_votes:.2f}")

# ---- SAVE CHART AS IMAGE ----
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Chart 1: Rating Range Bar Chart
range_counts = df['Rating Range'].value_counts().sort_index()
axes[0].bar(range_counts.index, range_counts.values, color=['#ff6b6b','#74b9ff','#74b9ff','#e17055','#74b9ff'])
axes[0].set_title('Most Common Rating Range')
axes[0].set_xlabel('Rating Range')
axes[0].set_ylabel('Number of Restaurants')

# Chart 2: Rating Distribution Histogram
axes[1].hist(df['Aggregate rating'], bins=20, color='#a29bfe', edgecolor='white')
axes[1].set_title('Aggregate Rating Distribution')
axes[1].set_xlabel('Rating')
axes[1].set_ylabel('Frequency')

plt.tight_layout()
plt.savefig('restaurant_chart.png')  # ← saves image in same folder
print("\nChart saved as restaurant_chart.png ✅")