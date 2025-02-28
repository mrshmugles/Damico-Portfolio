# Loan Default Risk Predictor  

## Overview  
This project builds a **machine learning model** to predict **loan default risk**, helping banks and financial institutions assess borrower risk before approving loans. The model identifies **high-risk applicants** based on key financial and demographic indicators, aiming to improve loan approval processes and reduce financial losses.  

## Data  
The dataset consists of **loan applications and borrower details**, including:  
- **Demographics** – Age, marital status, employment type  
- **Financials** – Income, loan amount, interest rate, credit score  
- **Debt-to-Income Ratio** – A newly engineered feature for better risk assessment  
- **Loan Details** – Term length, mortgage status, number of credit lines  
- **Target Variable** – Whether the loan was **defaulted (1) or paid off (0)**  

## Technologies Used  
- **Programming**: Python  
- **Libraries**: Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn  
- **Machine Learning**: Logistic Regression, Random Forest  
- **Big Data Processing**: SMOTE (Synthetic Minority Over-sampling)  

## Project Workflow  
### 1. Data Cleaning & Preprocessing  
- Handled **missing values** with mean (numerical) and mode (categorical) imputation  
- Created a **Debt-to-Income (DTI) ratio** feature to improve risk prediction  
- One-hot encoded categorical variables for machine learning compatibility  
- Addressed **class imbalance** using **SMOTE** to improve model performance  

### 2. Exploratory Data Analysis (EDA)  
- **Histograms** – Distribution of **income, loan amount, and credit scores**  
- **Box Plots** – Credit score comparison across **default vs. non-default cases**  
- **Correlation Heatmap** – Identified **relationships between financial variables**  
- **Bar Charts** – Default rates segmented by **employment type and marital status**  

### 3. Model Training & Evaluation  
- Tested **Logistic Regression** and **Random Forest** models  
- **Final Model**: **Random Forest** due to its strong performance on non-linear data  
- **Evaluation Metrics**:  
  - **Precision**: Minimized false positives for high-risk loans  
  - **Recall**: Ensured high detection of default cases  
  - **F1-Score**: Balanced precision and recall for better classification  
  - **AUC-ROC Score**: Achieved **0.95**, indicating strong predictive performance  

### 4. Results & Insights  
- **High debt-to-income ratio is a key predictor of loan default**  
- **Low credit scores and high-interest rates increase default probability**  
- **Married borrowers tend to have lower default rates than single applicants**  
- **Final Model** successfully predicted default risk with **91% accuracy**  

## Future Improvements  
- Integrate **external credit data** for more comprehensive risk assessment  
- Implement a **dynamic interest rate model** based on predicted risk scores  
- Deploy the model in a **real-time decision support system** for banks  

## Contributors  
- **Joseph Damico** – Applied Data Science, Bellevue University  
