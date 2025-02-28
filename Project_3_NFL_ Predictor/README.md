# NFL Predictor  

## Overview  
This project develops an **NFL game prediction model** using **historical play-by-play data** and machine learning. The goal is to create a system that accurately predicts game winners based on key game statistics. While the original plan included **live injury and weather data**, these have been set aside for future improvements.  

## Data  
The dataset consists of **NFL play-by-play data and game results (2013-2024)**, sourced from:  
- **NFL Savant** – Play-by-play (PBP) data  
- **Pro-Football-Reference** – Game results for labeling winners  

### Key Features Used:  
- **Game Details** – Home/Away Team, Game Date  
- **Play Metrics** – Down, Yards to Go, Turnovers, Play Type (Pass/Rush)  
- **Scoring Events** – Touchdowns, Fumbles, Interceptions  

## Technologies Used  
- **Programming**: Python  
- **Libraries**: Pandas, NumPy, Scikit-learn, XGBoost  
- **Web Scraping**: BeautifulSoup (for game results)  
- **Data Processing**: Streamlit (for dashboard), Joblib (for model deployment)  

## Project Workflow  
### 1. Data Collection & Cleaning  
- Scraped **game results** from Pro-Football-Reference  
- Processed **play-by-play (PBP) data** from NFL Savant  
- Merged datasets to **label each game’s winner**  

### 2. Exploratory Data Analysis (EDA)  
- **Win Distribution** – Home vs. Away wins over time  
- **Impact of Turnovers** – How fumbles and interceptions affect game outcomes  
- **Play Type Analysis** – Run vs. Pass trends in game-winning scenarios  

### 3. Model Training & Evaluation  
#### **Logistic Regression (Baseline Model)**  
- Over-predicted **home team wins** due to dataset imbalance  
#### **XGBoost (Final Model)**  
- **Balanced dataset** to prevent home team bias  
- **Trained on key game metrics** (e.g., turnovers, yards gained)  
- **Final Accuracy**: **99%** (on fully labeled game data)  

### 4. Deployment & Dashboard  
- **Streamlit-based UI** for selecting teams and predicting game winners  
- **Trained XGBoost model** used for real-time predictions  

## Results & Insights  
- **Turnovers & "Yards to Go" are the strongest predictors** of game outcomes  
- **Home teams win slightly more often, but model adjustments reduced bias**  
- **Future Goal**: Integrate **live data feeds** for real-time game predictions  

## Future Improvements  
- Add **injury & weather data** to improve prediction accuracy  
- Implement **live API integration** for real-time game analysis  
- Develop a **confidence score** for each prediction  

## Contributors  
- **Joseph Damico** – Applied Data Science, Bellevue University  
