# Healthcare Analytics Dashboard

## Project Overview

This project analyzes healthcare stroke data using SQL, Python, SQLite, and Power BI. The goal was to explore patient demographics and identify potential stroke risk factors through data analytics and visualization.

---

## Tools & Technologies

- Python
- Pandas
- SQLite
- SQL
- Power BI

---

## Key Features

- Built a healthcare analytics database using SQLite
- Cleaned and transformed patient data using Python
- Wrote SQL queries for demographic and risk analysis
- Developed interactive Power BI dashboards
- Analyzed stroke risk factors including:
  - smoking status
  - hypertension
  - age
  - gender

---

## Example SQL Analysis

```sql
SELECT
    gender,
    COUNT(*) AS total_patients,
    SUM(stroke) AS stroke_cases
FROM patients
GROUP BY gender;
```

---

## Dashboard Preview

<img width="957" height="537" alt="image" src="https://github.com/user-attachments/assets/dd5c34ce-fad9-4f70-978b-fd513c804217" />

---

## Key Insights

- Stroke rates increased significantly among older patients
- Hypertension showed strong correlation with stroke occurrence
- Smoking status demonstrated noticeable differences in stroke rates

---

## Dataset

Stroke Prediction Dataset from Kaggle.
