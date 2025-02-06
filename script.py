import pandas as pd

df = pd.read_csv("../hospital_readmission_renamed_data.csv")

print(df)

# Remove unnecessary columns


# Remove duplicate rows
df = df.drop_duplicates()

# Check NA values
df.isna().sum()

# Handle NA values


# Check column data type
df.info()

# Change column data type


# Check potential problems

