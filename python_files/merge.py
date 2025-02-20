import pandas as pd

# Read the CSV files
happiness_df = pd.read_csv('finalest.csv')
gdp_df = pd.read_csv('gdp_ppp.csv')

# Clean up gdp_nominal to numeric
gdp_df['gdp_nominal'] = pd.to_numeric(gdp_df['gdp_nominal'], errors='coerce')

# Merge the dataframes with GDP data
merged_df = happiness_df.merge(
    gdp_df[['Country', 'gdp_nominal']],
    left_on='country',
    right_on='Country',
    how='left'
)

# Drop the redundant country column
merged_df = merged_df.drop('Country', axis=1)

# Save the merged dataset
merged_df.to_csv('finalest.csv', index=False)

print("Merge complete. Check finalest.csv for the merged data.")
