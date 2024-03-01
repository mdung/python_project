import pandas as pd
import numpy as np

# Generate sample time series data
np.random.seed(42)  # Set seed for reproducibility

# Date range
date_rng = pd.date_range(start='2022-01-01', end='2023-12-31', freq='D')

# Trend component
trend = np.linspace(0, 100, num=len(date_rng))

# Seasonality component
seasonality = 10 * np.sin(2 * np.pi * (date_rng.dayofyear) / 365)

# Noise component
noise = np.random.normal(0, 5, size=len(date_rng))

# Combine components to create time series data
value = trend + seasonality + noise

# Create DataFrame
df = pd.DataFrame({'Date': date_rng, 'Value': value})

# Save the DataFrame to an Excel file
excel_file_path = 'C:/python_proj/python/excel/excel_file.xlsx'
df.to_excel(excel_file_path, index=False)

print(f"Excel file saved at: {excel_file_path}")
