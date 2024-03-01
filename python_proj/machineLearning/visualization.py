import pandas as pd
import matplotlib.pyplot as plt

# Sample data input (replace this with your own dataset)
data = {
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Value': [25, 45, 30, 15, 50]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Data analysis
total_values = df['Value'].sum()
average_value = df['Value'].mean()

# Data visualization
plt.bar(df['Category'], df['Value'])
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Data Analysis and Visualization')
plt.show()

# Print analysis results
print(f'Total values: {total_values}')
print(f'Average value: {average_value}')
