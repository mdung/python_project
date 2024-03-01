import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Function to generate synthetic data
def generate_synthetic_data(num_samples=1000):
    np.random.seed(42)

    # Generate random timestamps within a specific range
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2022, 12, 31)
    date_range = [start_date + timedelta(days=x) for x in range((end_date - start_date).days)]
    timestamps = np.random.choice(date_range, num_samples)

    # Generate random transaction amounts
    amounts = np.random.uniform(0.1, 1000, num_samples)

    # Generate random transaction types (e.g., 'send', 'receive')
    transaction_types = np.random.choice(['send', 'receive'], num_samples)

    # Generate random wallet addresses (for simplicity, using integers)
    sender_addresses = np.random.randint(1000000, 9999999, num_samples)
    receiver_addresses = np.random.randint(1000000, 9999999, num_samples)

    # Create a DataFrame
    data = pd.DataFrame({
        'timestamp': timestamps,
        'amount': amounts,
        'transaction_type': transaction_types,
        'sender_address': sender_addresses,
        'receiver_address': receiver_addresses
    })

    return data

# Generate synthetic data
num_samples = 1000
synthetic_data = generate_synthetic_data(num_samples)

# Save the dataset to a CSV file
synthetic_data.to_csv('your_dataset.csv', index=False)
