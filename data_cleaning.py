import pandas as pd
import numpy as np

print("Libraries imported successfully!")

import pandas as pd
import numpy as np

print("Libraries imported successfully!")

# Load financial dataset
df = pd.read_excel("Financial Sample.xlsx")

# Display first 5 rows
print(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove rows with missing values
df = df.dropna()

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Check duplicate rows
print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

# Check outliers using IQR method

numeric_columns = df.select_dtypes(include=np.number).columns

for column in numeric_columns:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = df[(df[column] < lower_limit) | (df[column] > upper_limit)]

    print(f"\n{column}: {len(outliers)} outliers")

# Variable Selection

selected_variables = [
    "Segment",
    "Product",
    "Units Sold",
    "Sale Price",
    "Gross Sales",
    "COGS",
    "Profit"
]

selected_data = df[selected_variables]

print("\nSelected Variables:")
print(selected_data.head()) 

print("\nExact Column Names:")
for column in df.columns:
    print(repr(column))

    
