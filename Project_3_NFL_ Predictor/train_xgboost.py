import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.utils import resample
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
file_path = "final_nfl_dataset.csv"
df = pd.read_csv(file_path, low_memory=False)

# Encode teams
df["HomeTeamEncoded"] = df["HomeTeam"].astype("category").cat.codes
df["AwayTeamEncoded"] = df["AwayTeam"].astype("category").cat.codes

# Target: 1 if home team won, 0 otherwise
df["WinnerEncoded"] = (df["Winner"] == df["HomeTeam"]).astype(int)

# Features
features = ["HomeTeamEncoded", "AwayTeamEncoded", "Down", "ToGo", "Yards", 
            "IsRush", "IsPass", "IsTouchdown", "IsInterception", "IsFumble"]

# Convert to numeric
for col in features:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Drop missing values
df = df.dropna()

# Balance the dataset again
home_wins = df[df["WinnerEncoded"] == 1]
away_wins = df[df["WinnerEncoded"] == 0]
home_wins_downsampled = resample(home_wins, replace=False, n_samples=len(away_wins), random_state=42)
df_balanced = pd.concat([home_wins_downsampled, away_wins])

# Train-test split
X = df_balanced[features]
y = df_balanced["WinnerEncoded"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = XGBClassifier(use_label_encoder=False, eval_metric="logloss")
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save the trained XGBoost model
joblib.dump(model, "xgboost_model.pkl")
print("Model saved as xgboost_model.pkl")