import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data input (replace this with your own climate change data)
data = {
    'Year': [2000, 2005, 2010, 2015, 2020],
    'GlobalTemperature': [0.5, 0.7, 0.9, 1.1, 1.3],
    'CO2Emissions': [30, 35, 40, 45, 50]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the 'Year' column as the index
df.set_index('Year', inplace=True)

# Line plot for global temperature over the years
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['GlobalTemperature'], marker='o')
plt.xlabel('Year')
plt.ylabel('Global Temperature (°C)')
plt.title('Global Temperature Over the Years')
plt.grid(True)
plt.show()

# Bar plot for CO2 emissions over the years
plt.figure(figsize=(10, 6))
sns.barplot(x=df.index, y=df['CO2Emissions'], palette='viridis')
plt.xlabel('Year')
plt.ylabel('CO2 Emissions (million tons)')
plt.title('CO2 Emissions Over the Years')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
