import sqlite3
from faker import Faker
import random
import datetime

# Connect to database
conn = sqlite3.connect('example.db')

# Create people table
conn.execute('''CREATE TABLE people
             (id INTEGER PRIMARY KEY,
              first_name TEXT,
              last_name TEXT,
              age INTEGER,
              email TEXT,
              phone_number TEXT,
              created_at TEXT,
              updated_at TEXT);''')

# Use Faker to generate fake data
fake = Faker()

# Insert 200 fake people into the people table
for i in range(200):
    first_name = fake.first_name()
    last_name = fake.last_name()
    age = random.randint(1, 100)
    email = fake.email()
    phone_number = fake.phone_number()
    created_at = datetime.datetime.now()
    updated_at = created_at

    # Insert data into table
    conn.execute('''INSERT INTO people
                 (first_name, last_name, age, email, phone_number, created_at, updated_at)
                 VALUES (?, ?, ?, ?, ?, ?, ?)''',
                 (first_name, last_name, age, email, phone_number, created_at, updated_at))

# Commit changes and close connection
conn.commit()
conn.close()
