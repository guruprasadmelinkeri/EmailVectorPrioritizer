import sqlite3
import csv

# Path to your local SQLite DB
DB_PATH = "./emails.db"
CSV_PATH = "./emails.csv"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Select the columns you need for training & indexing
cursor.execute("""
    SELECT subject, body, sender, is_high_priority
    FROM emails
""")

rows = cursor.fetchall()

# Column names
columns = [desc[0] for desc in cursor.description]

# Write to CSV
with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(columns)
    writer.writerows(rows)

conn.close()
print(f"Exported {len(rows)} rows to {CSV_PATH}")
