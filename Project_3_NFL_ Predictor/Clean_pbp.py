import pandas as pd
import glob

# List of all PBP files (2013-2024)
pbp_files = glob.glob("pbp-*.csv")

# Define columns to keep
columns_to_keep = [
    "GameId", "GameDate", "OffenseTeam", "DefenseTeam", "Down", "ToGo", "Yards",
    "IsRush", "IsPass", "IsTouchdown", "IsInterception", "IsFumble", 
    "IsPenaltyAccepted", "PenaltyYards"
]

# Process each file
for file_path in pbp_files:
    print(f"Processing {file_path}...")

    # Load the file
    pbp_data = pd.read_csv(file_path, quotechar='"', on_bad_lines="skip", encoding="utf-8", low_memory=False)

    # Keep only the necessary columns
    pbp_data = pbp_data[columns_to_keep]

    # Convert data types
    pbp_data["GameDate"] = pd.to_datetime(pbp_data["GameDate"], errors="coerce")
    pbp_data["Down"] = pd.to_numeric(pbp_data["Down"], errors="coerce")
    pbp_data["ToGo"] = pd.to_numeric(pbp_data["ToGo"], errors="coerce")
    pbp_data["Yards"] = pd.to_numeric(pbp_data["Yards"], errors="coerce")
    
    # Standardize team names to lowercase
    pbp_data["OffenseTeam"] = pbp_data["OffenseTeam"].str.lower()
    pbp_data["DefenseTeam"] = pbp_data["DefenseTeam"].str.lower()

    # Drop duplicate rows
    pbp_data = pbp_data.drop_duplicates()

    # Save cleaned version
    cleaned_file = file_path.replace(".csv", "-cleaned.csv")
    pbp_data.to_csv(cleaned_file, index=False)

    print(f"Saved cleaned file: {cleaned_file}")

print("All files processed successfully.")
