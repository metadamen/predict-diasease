import pandas as pd

# 🔹 Step 1: Load the CSV file (make sure it's in your project folder)
df = pd.read_csv("diabetic_data.csv")  # change the filename if needed

# 🔹 Step 2: Replace "?" with NaN (missing values)
df.replace("?", pd.NA, inplace=True)

# 🔹 Step 3: Drop columns with many missing values
columns_to_drop = ["weight", "payer_code", "medical_specialty"]
df.drop(columns=columns_to_drop, inplace=True)

# 🔹 Step 4: View the cleaned dataframe
print("✅ Data Loaded and Cleaned")
print(df.head())
print("\nRemaining Columns:", df.columns.tolist())
