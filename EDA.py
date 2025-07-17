import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import datetime

# Load data (replace with your file)
df = pd.read_excel("hospital_data.xlsx")  # or .csv

# Preview the data
print(df.head())
print(df.info())
print(df.describe())

# Convert dates if needed
df['Admission_Date'] = pd.to_datetime(df['Admission_Date'])
df['Discharge_Date'] = pd.to_datetime(df['Discharge_Date'])

# Calculate Length of Stay
df['Length_of_Stay'] = (df['Discharge_Date'] - df['Admission_Date']).dt.days

# ------------------------------
# 📊 1. Age Distribution
plt.figure(figsize=(8, 4))
sns.histplot(df['Age'], bins=20, kde=True, color='skyblue')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# ------------------------------
# 🚻 2. Gender Statistics
gender_counts = df['Gender'].value_counts()
print("Gender Counts:\n", gender_counts)

sns.countplot(data=df, x='Gender', palette='pastel')
plt.title("Gender Distribution")
plt.show()

# ------------------------------
# 🏥 3. Admissions by Department
plt.figure(figsize=(10, 4))
sns.countplot(data=df, x='Department', order=df['Department'].value_counts().index, palette='viridis')
plt.title("Admissions by Department")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ------------------------------
# 📅 4. Admissions Over Time
df['Admission_Month'] = df['Admission_Date'].dt.to_period('M')
monthly_admissions = df.groupby('Admission_Month').size().reset_index(name='Count')

fig = px.line(monthly_admissions, x='Admission_Month', y='Count', title='Monthly Admissions Trend')
fig.show()

# ------------------------------
# 💰 5. Revenue Summary
total_revenue = df['Billing'].sum()
print(f"Total Revenue: ${total_revenue:,.2f}")

fig = px.box(df, x='Department', y='Billing', title='Billing Amounts by Department')
fig.show()

# ------------------------------
# ⏳ 6. Length of Stay
plt.figure(figsize=(8, 4))
sns.histplot(df['Length_of_Stay'].dropna(), bins=20, color='salmon')
plt.title("Length of Stay Distribution")
plt.xlabel("Days")
plt.tight_layout()
plt.show()

# ------------------------------
# 🚨 7. Check for Missing Values
missing = df.isnull().sum()
print("\nMissing Values:\n", missing)

# ------------------------------
# ⚠️ 8. Detect Outliers in Billing
plt.figure(figsize=(8, 4))
sns.boxplot(x=df['Billing'], color='orange')
plt.title("Outliers in Billing")
plt.tight_layout()
plt.show()
