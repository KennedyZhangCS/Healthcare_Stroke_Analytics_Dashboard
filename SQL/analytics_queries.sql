SELECT *
FROM patients
LIMIT 10;

SELECT
    gender,
    COUNT(*) AS total_patients,
    SUM(stroke) AS stroke_cases,
    ROUND(
        CAST(SUM(stroke) AS FLOAT) / COUNT(*) * 100,
        2
    ) AS stroke_percentage
FROM patients
GROUP BY gender;

SELECT
    hypertension,
    COUNT(*) AS total_patients,
    SUM(stroke) AS stroke_cases,
    ROUND(
        CAST(SUM(stroke) AS FLOAT) / COUNT(*) * 100,
        2
    ) AS stroke_percentage
FROM patients
GROUP BY hypertension;

SELECT
    CASE
        WHEN age < 20 THEN '0-19'
        WHEN age < 40 THEN '20-39'
        WHEN age < 60 THEN '40-59'
        ELSE '60+'
    END AS age_group,

    COUNT(*) AS total_patients,

    SUM(stroke) AS stroke_cases,

    ROUND(
        CAST(SUM(stroke) AS FLOAT) / COUNT(*) * 100,
        2
    ) AS stroke_percentage

FROM patients

GROUP BY age_group

ORDER BY stroke_percentage DESC;