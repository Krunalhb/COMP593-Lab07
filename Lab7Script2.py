import sqlite3
import pandas as pd
import os

# Connect to database
conn = sqlite3.connect('example.db')

# Execute SQL query to get name and age of all people at least 50 years old
query = '''SELECT first_name, last_name, age FROM people WHERE age >= 50'''
c = conn.cursor()
c.execute(query)

# Fetch query results
results = c.fetchall()

# Print name and age of each person in the query result within a sentence
for row in results:
    print(f"{row[0]} {row[1]} is {row[2]} years old.")

# Save results to a CSV file in the same folder as the script
df = pd.DataFrame(results, columns=['First Name', 'Last Name', 'Age'])
path = os.path.join(os.getcwd(), 'old_people.csv')
df.to_csv(path, index=False, header=True)

# Close connection to database
conn.close()
