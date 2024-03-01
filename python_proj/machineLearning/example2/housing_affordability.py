import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample housing affordability data (replace with your actual data)
data = {
    'Region': ['Region A', 'Region B', 'Region C', 'Region D', 'Region E'],
    'MedianIncome': [60000, 75000, 55000, 80000, 70000],
    'MedianHousePrice': [300000, 400000, 250000, 500000, 450000]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Calculate affordability ratio (House Price / Income)
df['AffordabilityRatio'] = df['MedianHousePrice'] / df['MedianIncome']

# Sort the DataFrame by affordability ratio
df = df.sort_values(by='AffordabilityRatio', ascending=True)

# Create a bar plot to visualize affordability ratios
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Region', y='AffordabilityRatio', palette='viridis')
plt.title('Housing Affordability by Region')
plt.xlabel('Region')
plt.ylabel('Affordability Ratio')
plt.xticks(rotation=45)
plt.tight_layout()

# Display the plot
plt.show()
