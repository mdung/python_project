from faker import Faker
import pandas as pd
import random

fake = Faker()

# Generate synthetic data
num_samples = 1000

data = {
    'text': [fake.text() for _ in range(num_samples)],
    'label': [random.choice(['ham', 'spam']) for _ in range(num_samples)]
}

# Create a DataFrame and save it to CSV
df = pd.DataFrame(data)
df.to_csv('spam_dataset.csv', index=False)
