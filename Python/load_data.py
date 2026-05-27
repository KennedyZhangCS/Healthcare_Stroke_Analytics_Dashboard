import pandas as pd
import sqlite3
import os

#read csv
csv_path = "../data/healthcare-dataset-stroke-data.csv"
df = pd.read_csv(csv_path)

#delete id column
if "id" in df.columns:
    df = df.drop(columns=["id"])


df["bmi"] = df["bmi"].fillna(df["bmi"].median())

#build sql database
db_path = "../healthcare.db"
conn = sqlite3.connect(db_path)

#write it into database
df.to_sql("patients", conn, if_exists="replace", index=False)

cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM patients;")
count = cursor.fetchone()[0]

print("Data loaded successfully!")
print("Total rows:", count)

conn.close()