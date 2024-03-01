import matplotlib.pyplot as plt
import pandas as pd

# Sample data (replace with your actual data)
data = {
    'Date': ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01'],
    'VaccinationRate': [10, 25, 40, 60, 75]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['VaccinationRate'], marker='o')
plt.title('COVID-19 Vaccination Rates Over Time')
plt.xlabel('Date')
plt.ylabel('Vaccination Rate (%)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Display the plot
plt.show()
