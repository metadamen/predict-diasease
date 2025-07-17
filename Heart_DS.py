import pandas as pd
import random

ages = [random.randint(29, 77) for _ in range(100)]
genders = [random.choice(['Male', 'Female']) for _ in range(100)]
cp_types = [random.choice(['TA', 'ATA', 'NAP', 'ASY']) for _ in range(100)]
resting_bp = [random.randint(80, 180) for _ in range(100)]
chol = [random.randint(100, 400) for _ in range(100)]
fasting_bs = [random.choice([0, 1]) for _ in range(100)]
max_hr = [random.randint(100, 200) for _ in range(100)]
angina = [random.choice(['Yes', 'No']) for _ in range(100)]
oldpeak = [round(random.uniform(0.0, 6.2), 1) for _ in range(100)]
st_slope = [random.choice(['Up', 'Flat', 'Down']) for _ in range(100)]
heart_disease = [random.choice([0, 1]) for _ in range(100)]

df = pd.DataFrame({
    'Age': ages,
    'Gender': genders,
    'ChestPainType': cp_types,
    'RestingBP': resting_bp,
    'Cholesterol': chol,
    'FastingBS': fasting_bs,
    'MaxHR': max_hr,
    'ExerciseAngina': angina,
    'Oldpeak': oldpeak,
    'ST_Slope': st_slope,
    'HeartDisease': heart_disease
})

df.to_csv('heart_disease_data.csv', index=False)
print("✅ Dataset saved as heart_disease_data.csv")
