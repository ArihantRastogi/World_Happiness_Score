import pandas as pd

# Read the CSV files
happiness_df = pd.read_csv('finalest.csv')
life_exp_df = pd.read_csv('life_expectancy.csv')

# Merge the dataframes and update life expectancy
merged_df = happiness_df.merge(
    life_exp_df[['Country', 'Life Expectancy']],
    left_on='country',
    right_on='Country',
    how='left'
)

# Directly replace healthy_life_expectancy with Life Expectancy
merged_df['healthy_life_expectancy'] = merged_df['Life Expectancy']

# Drop unnecessary columns
merged_df = merged_df.drop(['Country', 'Life Expectancy'], axis=1)

# Save the updated dataset
merged_df.to_csv('finalest.csv', index=False)

print("Life expectancy values updated. Check finalest.csv for the merged data.")
