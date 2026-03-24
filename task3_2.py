import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Dataset  (1).csv')

# ---- TASK 1: Highest & Lowest Votes ----
highest_votes = df.nlargest(10, 'Votes')[
    ['Restaurant Name', 'City', 
     'Aggregate rating', 'Votes']]

lowest_votes = df.nsmallest(10, 'Votes')[
    ['Restaurant Name', 'City', 
     'Aggregate rating', 'Votes']]

print("Top 10 Restaurants with HIGHEST Votes:")
print(highest_votes.to_string(index=False))

print("\nTop 10 Restaurants with LOWEST Votes:")
print(lowest_votes.to_string(index=False))

# ---- TASK 2: Correlation between Votes & Rating ----
correlation = df['Votes'].corr(df['Aggregate rating'])
print(f"\nCorrelation between Votes and Rating: {correlation:.4f}")

if correlation > 0.5:
    print("Strong Positive Correlation ✅")
elif correlation > 0:
    print("Weak Positive Correlation ↗️")
else:
    print("Negative Correlation ↘️")

# Stats
print(f"\nAverage Votes: {df['Votes'].mean():.2f}")
print(f"Max Votes: {df['Votes'].max()}")
print(f"Min Votes: {df['Votes'].min()}")

# ---- SAVE CHARTS ----
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Votes Analysis', 
             fontsize=16, fontweight='bold')

# Chart 1: Top 10 Highest Voted Restaurants
axes[0].barh(highest_votes['Restaurant Name'], 
             highest_votes['Votes'], 
             color='#74b9ff')
axes[0].set_title('Top 10 Restaurants\nby Highest Votes')
axes[0].set_xlabel('Number of Votes')
axes[0].invert_yaxis()

# Chart 2: Scatter plot - Votes vs Rating
axes[1].scatter(df['Votes'], 
                df['Aggregate rating'],
                alpha=0.3, 
                color='#a29bfe',
                s=10)
axes[1].set_title(f'Votes vs Rating\n(Correlation: {correlation:.4f})')
axes[1].set_xlabel('Number of Votes')
axes[1].set_ylabel('Aggregate Rating')

# Add trend line
z = np.polyfit(df['Votes'], 
               df['Aggregate rating'], 1)
p = np.poly1d(z)
axes[1].plot(sorted(df['Votes']), 
             p(sorted(df['Votes'])), 
             "r--", linewidth=2, 
             label='Trend Line')
axes[1].legend()

plt.tight_layout()
plt.savefig('votes_analysis.png')
print("\nChart saved as votes_analysis.png ✅")