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

## ETL Workflow

1. Extracted healthcare patient data from CSV datasets
2. Cleaned and transformed missing BMI and demographic values using Python Pandas
3. Loaded transformed healthcare data into a SQLite database
4. Queried healthcare metrics and patient trends using SQL
5. Built interactive Power BI dashboards for healthcare analytics visualization

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

## Business Questions Explored

- Which patient demographics demonstrate the highest stroke risk?
- Does hypertension correlate with stroke occurrence?
- How does smoking status impact patient stroke rates?
- Which age groups show elevated healthcare risk patterns?
- How can healthcare dashboards support clinical and operational decision-making?

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

- Stroke occurrence increased significantly among patients over age 60
- Patients with hypertension demonstrated higher stroke rates
- Former smokers showed elevated stroke percentages compared to non-smokers
- Patient demographic analysis revealed noticeable healthcare risk differences across age and gender groups
- Interactive dashboards improved visibility into patient health trends and operational analytics

---

## Key Insights

- Stroke rates increased significantly among older patients
- Hypertension showed strong correlation with stroke occurrence
- Smoking status demonstrated noticeable differences in stroke rates

---

## Data Dictionary

| Column | Description |
|---|---|
| age | Patient age |
| gender | Patient gender |
| hypertension | Indicates whether the patient has hypertension |
| heart_disease | Indicates whether the patient has heart disease |
| avg_glucose_level | Average glucose level recorded for the patient |
| bmi | Body Mass Index |
| smoking_status | Patient smoking history |
| stroke | Indicates whether the patient experienced a stroke |

---

## Dataset

Stroke Prediction Dataset from Kaggle.
