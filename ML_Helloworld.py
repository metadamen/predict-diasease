
import pandas as pd

# Load the dataset (replace with your path if needed)
df = pd.read_csv("diabetic_data.csv")

# Replace '?' with actual NaN for easier handling
df.replace('?', pd.NA, inplace=True)

# Drop columns with too many missing values
columns_to_drop = ['weight', 'payer_code', 'medical_specialty']
df.drop(columns=columns_to_drop, inplace=True)

# Optional: Check if the columns were dropped
print("Remaining columns:", df.columns.tolist())


print(df.head())
print(df.columns)