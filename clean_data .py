import pandas as pd

# load the raw data
df = pd.read_csv("data/raw/cybersecurity_cases_india_combined.csv")
print("Rows before cleaning:", len(df))

# make column names uppercase
df.columns = df.columns.str.upper()

# remove extra spaces from text columns
df["INCIDENT_TYPE"] = df["INCIDENT_TYPE"].str.strip()
df["CITY"] = df["CITY"].str.strip()
df["CATEGORY"] = df["CATEGORY"].str.strip()

# Malware_Attacks and Malware are the same thing, so merge them
df["INCIDENT_TYPE"] = df["INCIDENT_TYPE"].replace("Malware_Attacks", "Malware")

# check for missing values and duplicates
print("Missing values:")
print(df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())

df = df.dropna()
df = df.drop_duplicates()

# add an index column for each case
df.insert(0, "INDEX", range(1, len(df) + 1))

# save the cleaned file
df.to_csv("data/cleaned/cybersecurity_cases_india_cleaned.csv", index=False)
print("Rows after cleaning:", len(df))
print(df["INCIDENT_TYPE"].value_counts())
