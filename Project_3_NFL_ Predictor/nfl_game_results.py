import requests
import pandas as pd
from bs4 import BeautifulSoup
import time

# Define the seasons to scrape
seasons = list(range(2013, 2025))

# Base URL for schedules
base_url = "https://www.pro-football-reference.com/years/{}/games.htm"

# Store results
game_results = []

for season in seasons:
    url = base_url.format(season)
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find the table with game results
        table = soup.find("table", {"id": "games"})
        
        if table:
            rows = table.find("tbody").find_all("tr")

            for row in rows:
                cols = row.find_all("td")
                if cols:
                    game_date = cols[1].text.strip()
                    game_time = cols[2].text.strip()

                    # Home and Away team logic
                    if cols[4].text.strip() == "@":
                        home_team = cols[5].text.strip()
                        away_team = cols[3].text.strip()
                    else:
                        home_team = cols[3].text.strip()
                        away_team = cols[5].text.strip()

                    # Check if scores are empty
                    home_score_text = cols[7].text.strip()
                    away_score_text = cols[8].text.strip()

                    if home_score_text == "" or away_score_text == "":
                        continue

                    # Convert scores to integers
                    home_score = int(home_score_text)
                    away_score = int(away_score_text)

                    # Determine the winner
                    winner = home_team if home_score > away_score else away_team

                    # Store the game result
                    game_results.append({
                        "SeasonYear": season,
                        "GameDate": game_date,
                        "GameTime": game_time,
                        "HomeTeam": home_team,
                        "AwayTeam": away_team,
                        "HomeScore": home_score,
                        "AwayScore": away_score,
                        "Winner": winner
                    })

        print(f"Finished scraping {season} season.")
    else:
        print(f"Failed to retrieve data for {season}")

    # Avoid getting blocked again...
    time.sleep(3)

# Convert to DataFrame
df_results = pd.DataFrame(game_results)

# Save to CSV
df_results.to_csv("nfl_game_results.csv", index=False)

# Display first few rows
print(df_results.head())
