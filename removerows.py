import pandas as pd

file_path = "your_file.xlsx"  # change this

# Read Excel
df = pd.read_excel(file_path)

# Drop completely empty rows
df.dropna(how='all', inplace=True)

# Write back to the same file
df.to_excel(file_path, index=False)

print("Completely empty rows removed from the same file.")
