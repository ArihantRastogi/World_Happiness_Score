import pandas as pd
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv('../data/final.csv')

# Get happiness scores for 2015 and 2024
df_2015 = df[df['year'] == 2015][['country', 'happiness_score']]
df_2024 = df[df['year'] == 2024][['country', 'happiness_score']]

# Merge the data to calculate changes
changes = pd.merge(df_2015, df_2024, on='country', suffixes=('_2015', '_2024'))
changes['change'] = changes['happiness_score_2024'] - changes['happiness_score_2015']

# Sort by absolute change to get most affected countries
most_affected = changes.nlargest(5, 'change')
least_affected = changes.nsmallest(5, 'change')

print("\nTop 5 Countries with Largest Positive Change:")
print(most_affected[['country', 'change']].to_string(index=False))

print("\nTop 5 Countries with Largest Negative Change:")
print(least_affected[['country', 'change']].to_string(index=False))

# Plot trends for these countries
countries_to_plot = pd.concat([most_affected['country'], least_affected['country']])

plt.figure(figsize=(12, 6))
for country in countries_to_plot:
    country_data = df[df['country'] == country]
    plt.plot(country_data['year'], country_data['happiness_score'], marker='o', label=country)

plt.title('Happiness Score Trends (2015-2024)')
plt.xlabel('Year')
plt.ylabel('Happiness Score')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()

# Print detailed yearly trends for these countries
print("\nYearly Happiness Scores for Most Affected Countries:")
for country in countries_to_plot:
    country_data = df[df['country'] == country]
    print(f"\n{country}:")
    print(country_data[['year', 'happiness_score']].to_string(index=False))
