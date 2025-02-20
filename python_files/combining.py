import pandas as pd

all_data = []

for year in range(2015, 2025):
    file_path = f'data/WHR_{year}.csv'
    df = pd.read_csv(file_path)
    df['year'] = year
    all_data.append(df)

combined_df = pd.concat(all_data, ignore_index=True)
combined_df.sort_values(['country', 'year'], inplace=True)
combined_df.to_csv('data.csv', index=False)