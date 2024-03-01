import matplotlib.pyplot as plt
import pandas as pd

# Sample data (replace with your actual data)
data = {
    'Date': ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01'],
    'Location': ['Intersection A', 'Street B', 'Intersection C', 'Street D', 'Intersection A'],
    'Severity': ['Minor', 'Major', 'Minor', 'Fatal', 'Major']
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Count accident occurrences by location
location_counts = df['Location'].value_counts()

# Plotting
plt.figure(figsize=(10, 6))
location_counts.plot(kind='bar', color='skyblue')
plt.title('Traffic Accident Patterns by Location')
plt.xlabel('Location')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.tight_layout()

# Display the plot
plt.show()

# Count accident severity
severity_counts = df['Severity'].value_counts()

# Plotting
plt.figure(figsize=(8, 5))
severity_counts.plot(kind='pie', autopct='%1.1f%%', colors=['gold', 'lightcoral', 'lightskyblue'])
plt.title('Traffic Accident Severity Distribution')
plt.tight_layout()

# Display the plot
plt.show()
