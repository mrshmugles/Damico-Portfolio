import requests
from bs4 import BeautifulSoup

# Test a single season
season = 2024  
url = f"https://www.pro-football-reference.com/years/{season}/games.htm"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find the table with game results
    table = soup.find("table", {"id": "games"})
    
    if table:
        rows = table.find("tbody").find_all("tr")
        
        for row in rows[:5]:
            cols = row.find_all("td")
            print("\nNEW ROW:")
            for i, col in enumerate(cols):
                print(f"Column {i}: {col.text.strip()}")
