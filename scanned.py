import pandas as pd

# File paths
discover_file = "discover_assets.xlsx"
my_assets_file = "my_assets.xlsx"

# Read files
discover_df = pd.read_excel(discover_file)
my_assets_df = pd.read_excel(my_assets_file)

# Column names (case-sensitive)
discover_ip_col = "IP Address"
my_ip_col = "Primary_IPAddress"
comment_col = "comment"

# Clean IP columns (important)
discover_ips = discover_df[discover_ip_col].astype(str).str.strip()
my_assets_df[my_ip_col] = my_assets_df[my_ip_col].astype(str).str.strip()

# Update comment ONLY where IP matches
my_assets_df.loc[
    my_assets_df[my_ip_col].isin(discover_ips),
    comment_col
] = "Already getting scanned"

# Write back to SAME file
with pd.ExcelWriter(my_assets_file, engine="openpyxl", mode="w") as writer:
    my_assets_df.to_excel(writer, index=False)

print("✅ my_assets.xlsx updated successfully")
