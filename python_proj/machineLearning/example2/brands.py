import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load social media engagement data from a CSV file (replace with your actual data)
data = pd.read_csv('social_media_data.csv')

# Basic data exploration
print("Data Summary:")
print(data.head())
print("\nData Info:")
print(data.info())

# Calculate engagement rate (likes + comments + shares)
data['EngagementRate'] = (data['Likes'] + data['Comments'] + data['Shares']) / data['Followers'] * 100

# Calculate average engagement rate
avg_engagement_rate = data['EngagementRate'].mean()

# Plotting
plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x='Date', y='EngagementRate', marker='o')
plt.title('Social Media Engagement Over Time')
plt.xlabel('Date')
plt.ylabel('Engagement Rate (%)')
plt.xticks(rotation=45)
plt.axhline(y=avg_engagement_rate, color='r', linestyle='--', label='Average Engagement Rate')
plt.legend()
plt.tight_layout()

# Display the plot
plt.show()

# Group data by brand and calculate total engagement
brand_engagement = data.groupby('Brand')['EngagementRate'].sum()

# Plotting
plt.figure(figsize=(8, 5))
brand_engagement.sort_values().plot(kind='barh', color='skyblue')
plt.title('Total Engagement Rate by Brand')
plt.xlabel('Total Engagement Rate')
plt.ylabel('Brand')
plt.tight_layout()

# Display the plot
plt.show()

# Calculate engagement statistics
engagement_stats = data.groupby('Brand')['EngagementRate'].describe()

# Print engagement statistics
print("Engagement Statistics:")
print(engagement_stats)
