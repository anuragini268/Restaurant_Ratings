import pandas as pd
import folium
from folium.plugins import MarkerCluster

df = pd.read_csv('Dataset  (1).csv')

# Remove rows with missing coordinates
df = df.dropna(subset=['Latitude', 'Longitude'])
df = df[df['Latitude'] != 0]

# ---- TASK 1: Plot restaurants on map ----
map = folium.Map(location=[df['Latitude'].mean(), 
                            df['Longitude'].mean()], 
                            zoom_start=2)

# Add cluster markers
marker_cluster = MarkerCluster().add_to(map)

for _, row in df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"{row['Restaurant Name']}\nRating: {row['Aggregate rating']}",
        tooltip=row['Restaurant Name']
    ).add_to(marker_cluster)

# Save map
map.save('restaurant_map.html')
print("Map saved as restaurant_map.html ✅")

# ---- TASK 2: Identify Clusters/Patterns ----
print("\nTop 10 Cities with Most Restaurants:")
print(df['City'].value_counts().head(10))

print("\nTop 10 Countries with Most Restaurants:")
print(df['Country Code'].value_counts().head(10))

print(f"\nTotal Restaurants Plotted: {len(df)}")