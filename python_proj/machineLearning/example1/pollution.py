import matplotlib.pyplot as plt
import pandas as pd

# Sample data (replace with your actual data)
data = {
    'Date': ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01'],
    'PollutionLevel': [150, 120, 180, 90, 200]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Basic statistics
mean_pollution = df['PollutionLevel'].mean()
max_pollution = df['PollutionLevel'].max()
min_pollution = df['PollutionLevel'].min()

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['PollutionLevel'], marker='o')
plt.axhline(y=mean_pollution, color='r', linestyle='--', label='Mean Pollution')
plt.axhline(y=max_pollution, color='g', linestyle='--', label='Max Pollution')
plt.axhline(y=min_pollution, color='b', linestyle='--', label='Min Pollution')
plt.title('Air Pollution Levels Over Time')
plt.xlabel('Date')
plt.ylabel('Pollution Level')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Display the plot
plt.show()

# Print basic statistics
print(f"Mean Pollution Level: {mean_pollution}")
print(f"Max Pollution Level: {max_pollution}")
print(f"Min Pollution Level: {min_pollution}")
