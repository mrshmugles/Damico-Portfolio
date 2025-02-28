import pandas as pd
import glob

# Find all cleaned PBP files (2013-2024)
pbp_cleaned_files = glob.glob("pbp-*-cleaned.csv")

# Load and merge all files
pbp_data_list = []
for file in pbp_cleaned_files:
    print(f"Loading {file}...")
    df = pd.read_csv(file, low_memory=False)
    pbp_data_list.append(df)

# Concatenate all years into one DataFrame
pbp_master = pd.concat(pbp_data_list, ignore_index=True)

# Convert GameDate to datetime format
pbp_master["GameDate"] = pd.to_datetime(pbp_master["GameDate"], errors="coerce")

# Drop any duplicate plays
pbp_master = pbp_master.drop_duplicates()

# Sort by GameDate
pbp_master = pbp_master.sort_values(by="GameDate")

# Save final master file
pbp_master.to_csv("pbp_master_2013_2024.csv", index=False)

print("files merged into pbp_master_2013_2024.csv!")
