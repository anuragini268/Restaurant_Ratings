import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Dataset  (1).csv')

# ---- TASK 1: Most Common Cuisine Combinations ----
cuisine_counts = df['Cuisines'].value_counts()

print("Top 10 Most Common Cuisine Combinations:")
print(cuisine_counts.head(10))

most_common_cuisine = cuisine_counts.idxmax()
print(f"\nMost Common Cuisine Combination: {most_common_cuisine}")

# ---- TASK 2: Cuisine Combinations with Higher Ratings ----
cuisine_ratings = df.groupby('Cuisines')['Aggregate rating'].mean()
cuisine_ratings = cuisine_ratings.sort_values(ascending=False)

print("\nTop 10 Cuisine Combinations by Average Rating:")
print(cuisine_ratings.head(10))

# ---- SAVE CHARTS ----
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Chart 1: Top 10 Most Common Cuisines
top_cuisines = cuisine_counts.head(10)
axes[0].barh(top_cuisines.index, top_cuisines.values, color='#74b9ff')
axes[0].set_title('Top 10 Most Common\nCuisine Combinations')
axes[0].set_xlabel('Number of Restaurants')
axes[0].invert_yaxis()

# Chart 2: Top 10 Highest Rated Cuisines
top_rated = cuisine_ratings.head(10)
axes[1].barh(top_rated.index, top_rated.values, color='#55efc4')
axes[1].set_title('Top 10 Highest Rated\nCuisine Combinations')
axes[1].set_xlabel('Average Rating')
axes[1].invert_yaxis()

plt.tight_layout()
plt.savefig('cuisine_analysis.png')
print("\nChart saved as cuisine_analysis.png ✅")