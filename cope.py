import pandas as pd

df = pd.read_csv('/Users/asheeshkumar/Documents/SEM 2-2/DV/World_Happiness_Score/WHR_2024_bar.csv')

# Rename columns to match 2023 dataset
df.rename(columns={
    'Country name': 'country',
    'Ladder score': 'happiness_score',
    'Explained by: Log GDP per capita': 'gdp_per_capita',
    'Explained by: Social support': 'social_support',
    'Explained by: Healthy life expectancy': 'healthy_life_expectancy',
    'Explained by: Freedom to make life choices': 'freedom_to_make_life_choices',
    'Explained by: Generosity': 'generosity',
    'Explained by: Perceptions of corruption': 'perceptions_of_corruption'
}, inplace=True)

# Remove extra columns
df.drop(columns=['upperwhisker', 'lowerwhisker', 'Dystopia + residual'], inplace=True)

# Reorder columns to make 'region' the 2nd column and shift 'happiness_score' to 3rd
columns = ['country', 'region', 'happiness_score', 'gdp_per_capita', 'social_support', 'healthy_life_expectancy', 'freedom_to_make_life_choices', 'generosity', 'perceptions_of_corruption']
whr_2024_bar = df[columns]

# Save the cleaned dataset
whr_2024_bar.to_csv('data/WHR_2024.csv', index=False)
print(whr_2024_bar.head())