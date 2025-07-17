import pandas as pd
import random
from faker import Faker
from datetime import timedelta
fake = Faker()

departments = ['Cardiology', 'Neurology', 'Orthopedics', 'Oncology', 'Pediatrics', 'General Surgery']
diagnoses = ['Hypertension', 'Stroke', 'Fracture', 'Cancer', 'Infection', 'Migraine']

data = []

for i in range(100):
    pid = f"P{i+1:03d}"
    name = fake.name()
    age = random.randint(1, 90)
    gender = random.choice(['Male', 'Female'])
    dept = random.choice(departments)
    admission_date = fake.date_between(start_date='-6M', end_date='-1d')
    length_of_stay = random.randint(2, 20)
    discharge_date = admission_date + timedelta(days=length_of_stay)
    diagnosis = random.choice(diagnoses)
    billing = random.randint(3000, 40000)
    readmitted = random.choice(['Yes', 'No'])

    data.append({
        "Patient_ID": pid,
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Department": dept,
        "Admission_Date": admission_date,
        "Discharge_Date": discharge_date,
        "Diagnosis": diagnosis,
        "Billing": billing,
        "Readmitted": readmitted
    })

df = pd.DataFrame(data)
df.to_csv("hospital_data.csv", index=False)
df.to_excel("hospital_data.xlsx", index=False)

print("✅ Sample hospital dataset saved as 'hospital_data.csv' and 'hospital_data.xlsx'")
