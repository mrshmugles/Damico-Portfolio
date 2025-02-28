# AQI Project

## Overview  
This project aims to **predict PM2.5 air pollution levels** using **geographic and administrative data**. By leveraging machine learning techniques, the model provides insights into air quality trends, helping policymakers and researchers make informed decisions about pollution control and public health.  

## Data  
The dataset consists of **PM2.5 air quality measurements** from **2022 to 2024**, sourced from the **U.S. Environmental Protection Agency (EPA)**. The key features include:  
- **Geographic Information**: Latitude, Longitude  
- **Administrative Data**: State Code, County Code  
- **Air Quality Metrics**: PM2.5 concentration levels, monitoring methods  

The data was filtered using **EPA advisory recommendations** to ensure accurate and reliable analysis.  

## Technologies Used  
- **Programming**: Python  
- **Libraries**: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn  
- **Machine Learning Model**: Random Forest Regressor  
- **Data Visualization**: Power BI, Tableau  
- **Big Data Processing**: PySpark  

## Project Workflow  
### 1. Data Collection & Cleaning  
- Combined annual PM2.5 monitoring data  
- Filtered based on EPA-approved methods  
- Saved cleaned dataset for further analysis  

### 2. Exploratory Data Analysis (EDA)  
- Visualized **PM2.5 distribution across states and counties**  
- Identified regions with **high pollution levels**  
- Analyzed **feature importance** for prediction  

### 3. Machine Learning Model  
- Trained a **Random Forest Regressor** using geographic and administrative features  
- Evaluated model performance with:  
  - **Root Mean Squared Error (RMSE):** 1.01 µg/m³  
  - **R² Score:** 0.58  
- Identified **latitude and longitude** as the most influential predictors  

### 4. Results & Insights  
- **Geographic data significantly impacts PM2.5 predictions**  
- **Current model explains 58% of variance**, with room for improvement  
- **Recommendations**: Incorporate **meteorological data (temperature, wind speed), traffic density, and industrial emissions** for better accuracy  

## Future Improvements  
- **Enhance prediction accuracy** by integrating **weather and real-time data**  
- Develop a **public dashboard** to display **real-time air quality insights**  
- Extend analysis to **predict AQI beyond PM2.5**  

## Contributors  
- **Joseph Damico** – Applied Data Science, Bellevue University  
