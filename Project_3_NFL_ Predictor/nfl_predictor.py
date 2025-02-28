import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Load the trained model
model = joblib.load("xgboost_model.pkl")

# Load the dataset to get the team list
file_path = "final_nfl_dataset.csv"
df = pd.read_csv(file_path, low_memory=False)

# Encode team names
team_encoder = LabelEncoder()
df["HomeTeamEncoded"] = team_encoder.fit_transform(df["HomeTeam"])
df["AwayTeamEncoded"] = team_encoder.transform(df["AwayTeam"])
team_list = sorted(df["HomeTeam"].unique())

# Streamlit UI
st.title("🏈🏈🏈 NFL Game Winner Predictor 🏈🏈🏈")
st.write("Select a **Home Team** and **Away Team**, and the model will predict the winner.")

# Team selection
home_team = st.selectbox("🏠 Select Home Team", team_list)
away_team = st.selectbox("🚀 Select Away Team", team_list)

# Check if teams are the same
if home_team == away_team:
    st.warning("⚠️ Home and Away teams must be different!")
else:
    # Convert team names to encoded values
    home_team_encoded = team_encoder.transform([home_team])[0]
    away_team_encoded = team_encoder.transform([away_team])[0]

    # Create feature input for model
    input_data = pd.DataFrame({
        "HomeTeamEncoded": [home_team_encoded],
        "AwayTeamEncoded": [away_team_encoded],
        "Down": [1],
        "ToGo": [10],
        "Yards": [0],
        "IsRush": [0],
        "IsPass": [0],
        "IsTouchdown": [0],
        "IsInterception": [0],
        "IsFumble": [0]
    })

    # Make prediction
    prediction = model.predict(input_data)
    winner = home_team if prediction[0] == 1 else away_team

    # Display prediction
    st.success(f"🏆 Predicted Winner: **{winner}**")
