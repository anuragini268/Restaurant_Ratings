import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Dataset  (1).csv')

# ---- TASK 1: Identify Restaurant Chains ----
# Chains = restaurants with same name appearing more than once
restaurant_counts = df['Restaurant Name'].value_counts()
chains = restaurant_counts[restaurant_counts > 1]

print(f"Total Restaurant Chains Found: {len(chains)}")
print("\nTop 10 Restaurant Chains (by number of outlets):")
print(chains.head(10))

# ---- TASK 2: Analyze Ratings & Popularity of Chains ----
# Filter only chain restaurants
chain_names = chains.index.tolist()
chain_df = df[df['Restaurant Name'].isin(chain_names)]

# Average rating per chain
chain_ratings = chain_df.groupby('Restaurant Name').agg(
    Outlets=('Restaurant Name', 'count'),
    Avg_Rating=('Aggregate rating', 'mean'),
    Total_Votes=('Votes', 'sum')
).sort_values('Outlets', ascending=False)

print("\nTop 10 Chains - Ratings & Popularity:")
print(chain_ratings.head(10))

# ---- SAVE CHARTS ----
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Restaurant Chains Analysis', fontsize=16, fontweight='bold')

# Chart 1: Top 10 chains by outlets
top10 = chain_ratings.head(10)
axes[0].barh(top10.index, top10['Outlets'], color='#74b9ff')
axes[0].set_title('Top 10 Chains by Number of Outlets')
axes[0].set_xlabel('Number of Outlets')
axes[0].invert_yaxis()

# Chart 2: Top 10 chains by average rating
top10_rated = chain_ratings[chain_ratings['Outlets'] >= 5].sort_values(
    'Avg_Rating', ascending=False).head(10)
axes[1].barh(top10_rated.index, top10_rated['Avg_Rating'], color='#55efc4')
axes[1].set_title('Top 10 Chains by Average Rating')
axes[1].set_xlabel('Average Rating')
axes[1].invert_yaxis()

plt.tight_layout()
plt.savefig('chains_analysis.png')
print("\nChart saved as chains_analysis.png ✅")