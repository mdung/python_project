import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Function to generate synthetic climate data
def generate_climate_data(num_records=100):
    data = {
        'Date': [],
        'Temperature': [],
        'Humidity': [],
        'Precipitation': [],
        'WindSpeed': []
    }

    start_date = datetime(2020, 1, 1)
    end_date = datetime(2021, 1, 1)
    date_range = [start_date + timedelta(days=x) for x in range((end_date - start_date).days)]

    for _ in range(num_records):
        data['Date'].append(random.choice(date_range).strftime('%Y-%m-%d'))
        data['Temperature'].append(fake.pyfloat(min_value=-10, max_value=40, right_digits=2))
        data['Humidity'].append(fake.pyfloat(min_value=0, max_value=100, right_digits=2))
        data['Precipitation'].append(fake.pyfloat(min_value=0, max_value=10, right_digits=2))
        data['WindSpeed'].append(fake.pyfloat(min_value=0, max_value=30, right_digits=2))

    return pd.DataFrame(data)

# Generate climate data and save to CSV
climate_data = generate_climate_data()
climate_data.to_csv('climate_data.csv', index=False)
print("Climate data CSV file generated successfully.")
