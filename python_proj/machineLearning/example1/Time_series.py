import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Sample data input (replace this with your own time series data)
data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'Value': [50, 55, 60, 70, 65]
}

# Create a DataFrame
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Time series decomposition
result = seasonal_decompose(df['Value'], model='additive')

# Visualize the original time series
plt.figure(figsize=(10, 6))
plt.subplot(411)
plt.plot(df.index, df['Value'], label='Original')
plt.legend(loc='upper left')

# Visualize the trend component
plt.subplot(412)
plt.plot(result.trend, label='Trend')
plt.legend(loc='upper left')

# Visualize the seasonal component
plt.subplot(413)
plt.plot(result.seasonal, label='Seasonal')
plt.legend(loc='upper left')

# Visualize the residual component
plt.subplot(414)
plt.plot(result.resid, label='Residual')
plt.legend(loc='upper left')

plt.tight_layout()
plt.show()
