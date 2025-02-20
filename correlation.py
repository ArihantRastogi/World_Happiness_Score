import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('data/finalest.csv')

# List of factors to correlate with happiness score
factors = ['social_support', 'healthy_life_expectancy', 
          'freedom_to_make_life_choices', 'generosity', 'perceptions_of_corruption',
          'tax', 'temperature', 'divorce_percentage', 'gdp_nominal']

# Create a figure with multiple subplots
plt.figure(figsize=(20, 15))

# Create correlation plots for each factor
for i, factor in enumerate(factors, 1):
    plt.subplot(4, 3, i)
    
    # Remove rows with missing values for current factor
    valid_data = df[[factor, 'happiness_score']].dropna()
    
    # Create scatter plot
    sns.scatterplot(data=valid_data, x=factor, y='happiness_score')
    
    # Add trend line
    sns.regplot(data=valid_data, x=factor, y='happiness_score', 
                scatter=False, color='red', line_kws={'linestyle': '--'})
    
    # Calculate correlation coefficient
    corr = valid_data[factor].corr(valid_data['happiness_score'])
    
    plt.title(f'{factor.replace("_", " ").title()}\nCorrelation: {corr:.2f}')
    plt.xlabel(factor.replace("_", " ").title())
    plt.ylabel('Happiness Score')

# Adjust layout
plt.tight_layout()
plt.savefig('correlation_plots.png', dpi=300, bbox_inches='tight')
plt.close()

# Create correlation matrix
correlation_matrix = df[['happiness_score'] + factors].corr()['happiness_score'].sort_values(ascending=False)
print("\nCorrelation with Happiness Score:")
print(correlation_matrix)
