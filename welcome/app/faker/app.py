# Generates fake JSON data every 2 seconds for 10 seconds using the faker library.
import time
import json
from faker import Faker

fake = Faker()

def generate_fake_data():
    return {
        "fullname": fake.name(),
        "age": fake.random_int(min=18, max=80),
        "id": fake.uuid4(),
        "phone": fake.phone_number(),
        "message": fake.text()
    }

for _ in range(5):  # Run for 10 seconds (5 iterations x 2 seconds)
    print(json.dumps(generate_fake_data()))
    time.sleep(2)

exit(0)
