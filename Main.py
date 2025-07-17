import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("diabetic_data.csv")
df.replace('?', pd.NA, inplace=True)

# Drop columns with too many missing values
df.drop(columns=['weight', 'payer_code', 'medical_specialty'], inplace=True)

# Drop rows with missing values
df.dropna(inplace=True)

# Convert target 'readmitted' to binary (1 = readmitted <30, 0 = otherwise)
df['readmitted'] = df['readmitted'].apply(lambda x: 1 if x == '<30' else 0)

# Drop columns that won't help model or are IDs
df.drop(columns=['encounter_id', 'patient_nbr'], inplace=True)

# 🔵 Encode categorical columns to numeric using one-hot encoding
df_encoded = pd.get_dummies(df, drop_first=True)

# Split features and target
X = df_encoded.drop("readmitted", axis=1)
y = df_encoded["readmitted"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Fit model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

print("✅ Model trained successfully.")
