import pandas as pd
import random

data = []
genders = ['Male', 'Female']
married = ['Yes', 'No']
work_types = ['Private', 'Self-employed', 'Govt_job', 'children']
residences = ['Urban', 'Rural']
smoking = ['never smoked', 'formerly smoked', 'smokes']

for i in range(100):
    gender = random.choice(genders)
    age = round(random.uniform(18, 85), 1)
    hypertension = random.choice([0, 1])
    heart_disease = random.choice([0, 1])
    ever_married = random.choice(married)
    work_type = random.choice(work_types)
    residence_type = random.choice(residences)
    avg_glucose_level = round(random.uniform(70, 250), 1)
    bmi = round(random.uniform(15.0, 40.0), 1)
    smoking_status = random.choice(smoking)
    stroke = random.choice([0, 1])  # label

    data.append({
        "gender": gender,
        "age": age,
        "hypertension": hypertension,
        "heart_disease": heart_disease,
        "ever_married": ever_married,
        "work_type": work_type,
        "Residence_type": residence_type,
        "avg_glucose_level": avg_glucose_level,
        "bmi": bmi,
        "smoking_status": smoking_status,
        "stroke": stroke
    })

df = pd.DataFrame(data)
df.to_csv("stroke_prediction_data.csv", index=False)
print("✅ stroke_prediction_data.csv saved!")
