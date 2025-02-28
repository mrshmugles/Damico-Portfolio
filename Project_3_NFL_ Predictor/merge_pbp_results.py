import pandas as pd

# Load datasets
pbp_master = pd.read_csv("pbp_master_2013_2024.csv", low_memory=False)
game_results = pd.read_csv("nfl_game_results.csv")

# Convert GameDate to datetime
pbp_master["GameDate"] = pd.to_datetime(pbp_master["GameDate"], errors="coerce")
game_results["GameDate"] = pd.to_datetime(game_results["GameDate"], errors="coerce")

# Standardize team names to lowercase)
pbp_master["OffenseTeam"] = pbp_master["OffenseTeam"].str.lower()
pbp_master["DefenseTeam"] = pbp_master["DefenseTeam"].str.lower()
game_results["HomeTeam"] = game_results["HomeTeam"].str.lower()
game_results["AwayTeam"] = game_results["AwayTeam"].str.lower()
game_results["Winner"] = game_results["Winner"].str.lower()

# Merge PBP data with game results
merged_data = pbp_master.merge(
    game_results,
    on=["GameDate"],
    how="left"
)

# Save the final merged dataset
merged_data.to_csv("final_nfl_dataset.csv", index=False)

print("Data saved as final_nfl_dataset.csv")
