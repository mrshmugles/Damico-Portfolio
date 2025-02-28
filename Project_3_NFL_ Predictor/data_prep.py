import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load the dataset
file_path = "final_nfl_dataset.csv"
df = pd.read_csv(file_path, low_memory=False)

# Encode team names as numbers
team_encoder = LabelEncoder()
df["HomeTeamEncoded"] = team_encoder.fit_transform(df["HomeTeam"])
df["AwayTeamEncoded"] = team_encoder.transform(df["AwayTeam"])

# Create target variable: 1 if home team won, 0 otherwise
df["WinnerEncoded"] = (df["Winner"] == df["HomeTeam"]).astype(int)

# Select features for model training
features = ["HomeTeamEncoded", "AwayTeamEncoded", "Down", "ToGo", "Yards", 
            "IsRush", "IsPass", "IsTouchdown", "IsInterception", "IsFumble"]

X = df[features]
y = df["WinnerEncoded"]

# Split data into training and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Data is prepared.")
