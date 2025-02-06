import pandas as pd

df = pd.read_csv("../hospital_readmission_renamed_data.csv")

print(df)

# Identify the dependent column


# Remove unnecessary columns


# Remove duplicate rows
df = df.drop_duplicates()

# Check NA values
df.isna().sum()

# Handle NA values


# Check column data types
df.info()

# Change column data types
df["Readmitted"] = df["Readmitted"].astype(bool)
df["Smoker"] = df["Smoker"].astype(bool)
df["AlcoholUse"] = df["AlcoholUse"].astype(bool)
df["RegularExercise"] = df["RegularExercise"].astype(bool)
df["ChronicCondition"] = df["ChronicCondition"].astype(bool)
df["HighRiskMedication"] = df["HighRiskMedication"].astype(bool)
df["Gender"] = df["Gender"].astype("category")
df["Ethnicity"] = df["Ethnicity"].astype("category")
df["EducationLevel"] = df["EducationLevel"].astype("category")
df["EmploymentStatus"] = df["EmploymentStatus"].astype("category")
df["MaritalStatus"] = df["MaritalStatus"].astype("category")
df["InsuranceType"] = df["InsuranceType"].astype("category")
df["DischargeCondition"] = df["DischargeCondition"].astype("category")


# Check potential problems

