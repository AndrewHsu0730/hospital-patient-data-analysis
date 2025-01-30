import pandas as pd

df = pd.read_csv("../hospital_readmission_renamed_data.csv")

print(df)

# Remove unnecessary columns


# Remove duplicate rows
df = df.drop_duplicates()
