import pandas as pd

# File paths
discover_file = "discover_assets.xlsx"
my_assets_file = "my_assets.xlsx"

# Read Excel files
discover_df = pd.read_excel(discover_file)
my_assets_df = pd.read_excel(my_assets_file)

# Column names
discover_ip_col = "IP Address"
my_ip_col = "Primary_IPAddress"
comment_col = "comment"

# Create a set of IPs for fast lookup
discover_ip_set = set(discover_df[discover_ip_col].astype(str))

# Update comments only where IP matches
my_assets_df[comment_col] = my_assets_df.apply(
    lambda row: "Already getting scanned"
    if str(row[my_ip_col]) in discover_ip_set
    else row[comment_col],
    axis=1
)

# Save updated file
my_assets_df.to_excel("my_assets_updated.xlsx", index=False)

print("✅ Script completed. Updated file saved as 'my_assets_updated.xlsx'")
