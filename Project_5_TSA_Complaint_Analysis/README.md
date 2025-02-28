# TSA Complaint Analysis  

## Overview  
This project analyzes **TSA complaint data** to identify trends, patterns, and opportunities for improving passenger experience and security processes. The goal is to provide **TSA decision-makers** with actionable insights into complaint volumes across **airports, complaint categories, and time periods** to inform targeted improvements in TSA procedures.  

## Data  
The dataset consists of TSA complaints categorized by:  
- **Airport** – Location of complaint occurrence  
- **Complaint Type** – General category of the issue (e.g., security screening, property mishandling)  
- **Subcategory** – Specific complaint details (e.g., damaged luggage, inappropriate screening)  
- **Time Period** – Complaints spanning multiple years, capturing **seasonal trends**  
- **Geographic Data** – Integrated **IATA/ICAO codes** for mapping complaint locations  

## Technologies Used  
- **Programming**: Python  
- **Libraries**: Pandas, NumPy, Matplotlib, Seaborn, Folium  
- **Data Visualization**: Power BI, Tableau, Canva  
- **Geospatial Analysis**: Folium (for mapping complaint distributions)  

## Project Workflow  
### 1. Data Cleaning & Preprocessing  
- Merged complaint data with **IATA/ICAO airport codes** for location mapping  
- Identified and handled **missing values**  
- Converted **date fields** for time-series analysis  

### 2. Exploratory Data Analysis (EDA)  
- **Top 10 Airports by Complaint Volume** – Identified major airports with high complaint rates  
- **Complaint Distribution Across Airports** – Box plot analysis of **variability in complaints**  
- **Top Complaint Categories** – Highlighted most frequent issues (e.g., property mishandling, security screening)  
- **Seasonal Trends in Complaints** – Heatmap visualization of complaint spikes during peak travel months  

### 3. Geographic Visualization  
- **Choropleth Map**: Displayed regional variations in complaint volumes  
- **Marker Cluster Map**: Highlighted **high-complaint airports** with geospatial mapping  

### 4. Findings  
- **Major hubs (e.g., LAX, JFK, ATL) report the highest complaint volumes** due to increased passenger traffic  
- **Common complaints involve security screening, customer service, and baggage handling**  
- **Complaint volumes spike during peak travel periods (summer, holiday seasons)**, indicating the need for resource reallocation  

## Future Improvements  
- Incorporate **passenger volume data** to normalize complaint rates by airport traffic  
- Implement **machine learning models** to predict future complaint trends  
- Develop an **interactive dashboard** for real-time TSA complaint monitoring  

## Contributors  
- **Joseph Damico** – Applied Data Science, Bellevue University  
