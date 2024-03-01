import pandas as pd
from sklearn.preprocessing import StandardScaler

# Sample data input (replace this with your own dataset)
data = {
    'Age': [25, 30, None, 22, 35, 28, None, 40, 32, 27],
    'Income': [50000, 60000, 75000, 42000, None, 55000, 62000, 80000, 72000, 48000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Handling missing values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Income'].fillna(df['Income'].mean(), inplace=True)

# Data preprocessing - Scaling numerical features
scaler = StandardScaler()
df[['Age', 'Income']] = scaler.fit_transform(df[['Age', 'Income']])

# Print cleaned and preprocessed data
print(df)
