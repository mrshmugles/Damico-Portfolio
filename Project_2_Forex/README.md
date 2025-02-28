# Forex Predictions  

## Overview  
This project explores the **prediction of Forex market volatility** using **machine learning and time-series models**. The goal is to determine whether **historical OHLC (Open, High, Low, Close) price data** can be used to forecast future price movements and volatility in the **EUR/USD currency pair**.  

## Data  
The dataset consists of **historical Forex price data** from **TradingView**, including:  
- **Date** – Timestamp of each observation  
- **Open** – Opening price of the trading day  
- **High** – Highest price reached during the trading day  
- **Low** – Lowest price reached during the trading day  
- **Close** – Closing price of the trading day  
- **Daily Returns** – Percentage change in the closing price  
- **ATR (Average True Range)** – Measures market volatility  
- **Bollinger Bands** – Upper and lower price bands based on standard deviations from a moving average  

## Technologies Used  
- **Programming**: Python  
- **Libraries**: Pandas, NumPy, Scikit-learn, Statsmodels, Matplotlib  
- **Machine Learning Models**: Random Forest Regressor, ARIMA  
- **Time-Series Forecasting**: ARIMA (AutoRegressive Integrated Moving Average)  

## Project Workflow  
### 1. Data Collection & Preprocessing  
- Loaded **historical Forex price data** from TradingView  
- Converted timestamps to **datetime format**  
- Engineered features such as **Daily Returns, ATR, and Bollinger Bands**  

### 2. Exploratory Data Analysis (EDA)  
- **Visualized historical price trends** in the EUR/USD currency pair  
- **Analyzed volatility using ATR and Bollinger Bands**  
- **Plotted distribution of daily returns** to identify market patterns  

### 3. Machine Learning & Statistical Models  
#### **Random Forest Regressor**  
- Trained using **Daily Returns, ATR, and Bollinger Bands**  
- **RMSE:** 0.0287  
- **R² Score:** -2.73 (poor correlation, ineffective prediction)  

#### **ARIMA (5,1,0)**  
- Modeled **autoregressive trends** in Forex price movements  
- **RMSE:** 0.0175  
- **R² Score:** -0.39 (slightly better but still ineffective)  

### 4. Results & Insights  
- **Forex prices exhibit random walk behavior**, making short-term predictions unreliable  
- **Machine learning models struggled to find strong correlations** between historical price features and future movements  
- **ATR and Bollinger Bands effectively measure past volatility but do not predict future price direction**  

## Future Improvements  
- Implement **LSTM (Long Short-Term Memory) neural networks** to capture sequential dependencies  
- Integrate **macroeconomic indicators and news sentiment analysis**  
- Develop a **real-time Forex volatility monitoring dashboard**  

## Contributors  
- **Joseph Damico** – Applied Data Science, Bellevue University  
