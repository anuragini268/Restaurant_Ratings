import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

df = pd.read_csv('Dataset  (1).csv')

# Check columns
print(df.columns.tolist())

# ---- TASK 1: Analyze Text Reviews ----
# Use 'Rating text' column for keywords
print("\nRating Text Values:")
print(df['Rating text'].value_counts())

# Positive keywords (Good, Very Good, Excellent)
positive = df[df['Rating text'].isin(
    ['Excellent', 'Very Good', 'Good'])]

# Negative keywords (Poor, Average)
negative = df[df['Rating text'].isin(
    ['Poor', 'Average'])]

print(f"\nPositive Reviews: {len(positive)}")
print(f"Negative Reviews: {len(negative)}")

# Most common positive cuisines
print("\nTop 5 Cuisines in Positive Reviews:")
print(positive['Cuisines'].value_counts().head(5))

print("\nTop 5 Cuisines in Negative Reviews:")
print(negative['Cuisines'].value_counts().head(5))

# ---- TASK 2: Review Length & Rating ----
# Use 'Rating text' as review
df['Review Length'] = df['Rating text'].apply(
    lambda x: len(str(x)))

avg_length = df['Review Length'].mean()
print(f"\nAverage Review Length: {avg_length:.2f} characters")

# Relationship between review length and rating
length_rating = df.groupby('Rating text').agg(
    Avg_Rating=('Aggregate rating', 'mean'),
    Avg_Length=('Review Length', 'mean'),
    Count=('Rating text', 'count')
).sort_values('Avg_Rating', ascending=False)

print("\nReview Length vs Rating:")
print(length_rating)

# ---- SAVE CHARTS ----
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Restaurant Reviews Analysis', 
             fontsize=16, fontweight='bold')

# Chart 1: Rating Text Distribution
rating_counts = df['Rating text'].value_counts()
colors = ['#55efc4','#74b9ff','#a29bfe',
          '#fd79a8','#ffeaa7','#e17055']
axes[0].bar(rating_counts.index, 
            rating_counts.values, 
            color=colors)
axes[0].set_title('Distribution of Rating Text\n(Positive vs Negative)')
axes[0].set_xlabel('Rating Category')
axes[0].set_ylabel('Number of Restaurants')
axes[0].tick_params(axis='x', rotation=45)
for i, v in enumerate(rating_counts.values):
    axes[0].text(i, v + 20, str(v), 
                ha='center', fontweight='bold')

# Chart 2: Review Length vs Rating
axes[1].bar(length_rating.index, 
            length_rating['Avg_Rating'], 
            color='#74b9ff')
axes[1].set_title('Average Rating by\nReview Category')
axes[1].set_xlabel('Rating Category')
axes[1].set_ylabel('Average Rating')
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('reviews_analysis.png')
print("\nChart saved as reviews_analysis.png ✅")