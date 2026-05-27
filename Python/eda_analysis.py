import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

#connect database
conn = sqlite3.connect("../healthcare.db")

#read data
df = pd.read_sql_query("SELECT * FROM patients", conn)

# =========================
# Stroke Cases Summary
# =========================
total_patients = len(df)
stroke_cases = df["stroke"].sum()

print("Total Patients:", total_patients)
print("Stroke Cases:", stroke_cases)

stroke_rate = (stroke_cases / total_patients) * 100

print(f"Stroke Rate: {stroke_rate:.2f}%")

# =========================
# Stroke by Gender
# =========================
gender_analysis = df.groupby("gender")["stroke"].mean() * 100

print("\nStroke Percentage by Gender:")
print(gender_analysis)

# =========================
# Visualization
# =========================
gender_analysis.plot(kind="bar")

plt.title("Stroke Percentage by Gender")
plt.xlabel("Gender")
plt.ylabel("Stroke Percentage")

plt.tight_layout()

plt.savefig("../stroke_by_gender.png")

plt.show()

conn.close()