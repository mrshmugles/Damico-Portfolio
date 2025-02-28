# Security Log Analysis  

## Overview  
This project examines **security logging data** to identify gaps in documentation, assess missing values, and highlight areas for improvement in record-keeping practices. The analysis focuses on **White House visitor and access logs**, emphasizing the impact of incomplete records on security oversight.  

## Data  
The dataset consists of **White House security logs**, including:  
- **Visitor Information** – Names, entry/exit times, access type  
- **Meeting Records** – Location, host, and appointment details  
- **Security Badge Data** – Badge numbers and clearance levels  
- **Timestamps** – Log dates for access and appointment records  

A key challenge in this dataset is the **high volume of missing data**, particularly in badge numbers and timestamps, which affects security monitoring accuracy.  

## Technologies Used  
- **Programming**: Python  
- **Libraries**: Pandas, NumPy, Matplotlib, Seaborn  
- **Data Visualization**: Power BI, Tableau  
- **Geospatial & Time-Series Analysis**: Folium, Plotly  

## Project Workflow  
### 1. Data Cleaning & Preprocessing  
- Merged multiple **security log files**  
- Identified **incomplete records and missing values**  
- Standardized date formats for time-series analysis  

### 2. Exploratory Data Analysis (EDA)  
- **Missing Values by Column** – Assessed gaps in security logs  
- **Badge Number Issues** – Analyzed incomplete badge assignments  
- **Trends Over Time** – Identified patterns in missing entries  

### 3. Visualizations & Insights  
- **Bar Chart**: Missing values by log category  
- **Stacked Bar Chart**: Missing badge numbers vs. total appointments  
- **Scatter Plot**: Missing values over time  
- **Line Graph**: Incomplete appointment cancellation records  
- **Pie Chart**: Overall proportion of missing vs. recorded entries  

### 4. Findings  
- **Over 300,000 missing badge numbers**, reducing accountability in security checks  
- **Significant missing timestamps**, making it difficult to track access patterns  
- **Missing values increased toward the end of the year**, indicating potential lapses in data entry  
- **Incomplete appointment cancellation records**, leaving gaps in security reporting  

## Future Improvements  
- Implement **automated validation checks** to prevent missing entries  
- Enhance **data entry protocols** to ensure security records are complete  
- Develop an **interactive dashboard** to monitor security log completeness in real time  

## Contributors  
- **Joseph Damico** – Applied Data Science, Bellevue University  
