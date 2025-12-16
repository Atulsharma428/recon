import pandas as pd

# File paths
discover_file = "discover_assets.xlsx"
my_assets_file = "my_assets.xlsx"

# Read discover assets
discover_df = pd.read_excel(discover_file)

# Read my assets
my_assets_df = pd.read_excel(my_assets_file)

# Column names
discover_ip_col = "IP Address"
my_ip_col = "Primary_IPAddress"
comment_col = "comment"

# Convert IPs to string & create set for fast lookup
discover_ip_set = set(discover_df[discover_ip_col].astype(str).str.strip())

# Update comments in-place
for idx, row in my_assets_df.iterrows():
    if str(row[my_ip_col]).strip() in discover_ip_set:
        my_assets_df.at[idx, comment_col] = "Already getting scanned"

# Write back to the SAME file
with pd.ExcelWriter(my_assets_file, engine="openpyxl", mode="w") as writer:
    my_assets_df.to_excel(writer, index=False)

print("✅ my_assets.xlsx updated successfully")
