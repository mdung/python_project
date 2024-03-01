import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generate a sample dataset
np.random.seed(42)

# Create a date range
start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 12, 31)
date_range = pd.date_range(start=start_date, end=end_date)

# Create random prices
prices = np.random.uniform(low=100, high=200, size=len(date_range))

# Create a DataFrame
df = pd.DataFrame({'Date': date_range, 'Close': prices})

# Save the DataFrame to a CSV file
df.to_csv('your_data.csv', index=False)

# Display the DataFrame
print(df.head())
