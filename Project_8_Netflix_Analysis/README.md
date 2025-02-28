# Netflix Analysis  

## Overview  
This project analyzes **Netflix viewership data** to uncover trends in **content popularity, regional preferences, and engagement levels**. The insights from this analysis help **content and marketing teams** optimize Netflix’s content strategy by identifying which shows and movies perform best across different categories and countries.  

## Data  
The dataset consists of **Netflix viewership records** from multiple sources, including:  
- **Global Weekly Rankings** – Shows and movies ranked by weekly viewership hours  
- **Country-Specific Data** – Top 10 rankings by country and category  
- **Most Popular Titles** – Views and hours watched in the first 91 days after release  
- **Genres & Categories** – Breakdown of TV (English & Non-English) and Film performance  

## Technologies Used  
- **Programming**: Python  
- **Libraries**: Pandas, NumPy, Matplotlib, Seaborn  
- **Data Visualization**: Power BI, Tableau  
- **Time-Series Analysis**: Plotly  

## Project Workflow  
### 1. Data Cleaning & Preprocessing  
- Merged **global, country, and most popular datasets**  
- Formatted **date fields for time-series analysis**  
- Handled **missing values and inconsistencies**  

### 2. Exploratory Data Analysis (EDA)  
- **Category Breakdown** – Proportion of hours viewed in TV vs. Films  
- **Top 10 Shows by Hours Viewed** – Identified high-engagement content  
- **Most Popular Movies** – Analyzed the first 91-day performance  
- **Hours Viewed by Movie Rank** – Assessed how rankings impact longevity  

### 3. Visualizations & Insights  
- **Pie Chart**: Proportion of viewership by category (TV vs. Films)  
- **Bar Chart**: Top 10 most-watched shows based on total hours  
- **Box Plot**: Distribution of hours watched by movie rank  
- **Line Graph**: Weekly views for the top 5 most popular shows  
- **Geographic Heatmap**: Top-ranked countries by cumulative weeks in the Top 10  

### 4. Findings  
- **TV Shows (especially English-language) dominate Netflix viewership**  
- **High-performing movies see peak engagement in the first 91 days**, after which viewership drops  
- **Certain countries consistently rank in the Top 10**, suggesting strong regional preferences  
- **Lower-ranked movies tend to have significantly shorter lifespans**, impacting licensing and content retention strategies  

## Future Improvements  
- Integrate **sentiment analysis from social media** to understand audience engagement beyond viewership numbers  
- Develop **predictive models** to anticipate which upcoming shows/movies will perform well  
- Create an **interactive dashboard** for Netflix teams to explore real-time viewership trends  

## Contributors  
- **Joseph Damico** – Applied Data Science, Bellevue University  
