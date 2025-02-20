import pandas as pd
import random
from faker import Faker

# Initialize Faker for generating realistic names and dates
fake = Faker()

# Generate a large dataset with 10,000 records
num_records = 10000

data = {
    "id": list(range(1, num_records + 1)),
    "name": [fake.name() for _ in range(num_records)],
    "age": [random.randint(18, 65) for _ in range(num_records)],
    "date": [fake.date_between(start_date="-5y", end_date="today").strftime("%Y-%m-%d") for _ in range(num_records)],
    "salary": [random.randint(30000, 120000) for _ in range(num_records)]
}

# Convert dictionary to DataFrame
df_large = pd.DataFrame(data)

# Save to CSV file
df_large.to_csv("data.csv", index=False)

print("CSV file 'data.csv' has been created successfully!")
