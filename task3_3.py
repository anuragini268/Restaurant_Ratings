import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Dataset  (1).csv')

# Check columns
print("Price Range Values:")
print(df['Price range'].value_counts().sort_index())

print("\nOnline Delivery Values:")
print(df['Has Online delivery'].value_counts())

print("\nTable Booking Values:")
print(df['Has Table booking'].value_counts())

# ---- TASK 1: Price Range vs Online Delivery ----
delivery_by_price = df.groupby('Price range')[
    'Has Online delivery'].apply(
    lambda x: (x == 'Yes').sum() / len(x) * 100
).round(2)

print("\n% Restaurants with Online Delivery by Price Range:")
print(delivery_by_price)

# ---- TASK 2: Price Range vs Table Booking ----
booking_by_price = df.groupby('Price range')[
    'Has Table booking'].apply(
    lambda x: (x == 'Yes').sum() / len(x) * 100
).round(2)

print("\n% Restaurants with Table Booking by Price Range:")
print(booking_by_price)

# ---- TASK 3: Higher priced = more services? ----
print("\nConclusion:")
if delivery_by_price.is_monotonic_increasing:
    print("✅ Higher priced restaurants MORE likely to offer Online Delivery")
else:
    print("❌ No clear pattern for Online Delivery vs Price")

if booking_by_price.is_monotonic_increasing:
    print("✅ Higher priced restaurants MORE likely to offer Table Booking")
else:
    print("❌ No clear pattern for Table Booking vs Price")

# ---- SAVE CHARTS ----
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Price Range vs Services Analysis',
             fontsize=16, fontweight='bold')

price_labels = ['Budget\n(1)', 'Medium\n(2)', 
                'High\n(3)', 'Premium\n(4)']
x = np.arange(len(price_labels))
width = 0.35

# Chart 1: Online Delivery by Price Range
bars1 = axes[0].bar(x, delivery_by_price.values,
                    color='#74b9ff', 
                    edgecolor='white')
axes[0].set_title('Online Delivery %\nby Price Range')
axes[0].set_xlabel('Price Range')
axes[0].set_ylabel('% of Restaurants')
axes[0].set_xticks(x)
axes[0].set_xticklabels(price_labels)
for bar, val in zip(bars1, delivery_by_price.values):
    axes[0].text(bar.get_x() + bar.get_width()/2,
                bar.get_height() + 0.5,
                f'{val:.1f}%',
                ha='center', fontweight='bold')

# Chart 2: Table Booking by Price Range
bars2 = axes[1].bar(x, booking_by_price.values,
                    color='#55efc4',
                    edgecolor='white')
axes[1].set_title('Table Booking %\nby Price Range')
axes[1].set_xlabel('Price Range')
axes[1].set_ylabel('% of Restaurants')
axes[1].set_xticks(x)
axes[1].set_xticklabels(price_labels)
for bar, val in zip(bars2, booking_by_price.values):
    axes[1].text(bar.get_x() + bar.get_width()/2,
                bar.get_height() + 0.5,
                f'{val:.1f}%',
                ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('price_services_analysis.png')
print("\nChart saved as price_services_analysis.png ✅")