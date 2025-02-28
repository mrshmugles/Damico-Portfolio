import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.utils import resample
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
file_path = "final_nfl_dataset.csv"
df = pd.read_csv(file_path, low_memory=False)

# Encode team names
df["HomeTeamEncoded"] = df["HomeTeam"].astype("category").cat.codes
df["AwayTeamEncoded"] = df["AwayTeam"].astype("category").cat.codes

# Target variable: 1 if home team won, 0 otherwise
df["WinnerEncoded"] = (df["Winner"] == df["HomeTeam"]).astype(int)

# Select features
features = ["HomeTeamEncoded", "AwayTeamEncoded", "Down", "ToGo", "Yards", 
            "IsRush", "IsPass", "IsTouchdown", "IsInterception", "IsFumble"]

# Convert all features to numeric
for col in features:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Drop missing values
df = df.dropna()

# Balance the dataset??
home_wins = df[df["WinnerEncoded"] == 1]
away_wins = df[df["WinnerEncoded"] == 0]

# Downsample home wins (reduce its size)
home_wins_downsampled = resample(home_wins, replace=False, n_samples=len(away_wins), random_state=42)

# Combine balanced data
df_balanced = pd.concat([home_wins_downsampled, away_wins])

# Split into train & test
X = df_balanced[features]
y = df_balanced["WinnerEncoded"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))
