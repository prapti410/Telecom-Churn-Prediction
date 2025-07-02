# **Enhancing Retention Strategies: Machine Learning for Telecom Customer Churn Prediction**
Customer churn, or the rate at which customers leave a service, is a major challenge for telecom companies. Retaining customers is often more cost-effective than acquiring new ones, making churn prediction essential. Accurate churn prediction enables telecom providers to proactively address customer needs, enhance satisfaction, and implement targeted retention strategies, ultimately reducing churn and stabilizing revenue.

## **Project Workflow**

### **Data Collection and Understanding**

* Examined and understood the dataset, noted key features such as customer demographics, service usage, billing information, and the target variable Churn.

### **Data Cleaning**

* Handled missing values, corrected data types, and cleaned up anomalies (e.g., ensure TotalCharges is numeric, handle any NaN values).

### **Exploratory Data Analysis (EDA)**

* Used visualizations (via Seaborn and Matplotlib) to understand relationships and trends in the data.
* Identified key features affecting churn, such as Contract, PaymentMethod, MonthlyCharges, and TotalCharges.

### **Inferential Statistics**

* Conducted statistical tests (e.g., 1-sample t-test, Mann-Whitney U test, Chi-square test) to validate inferences from EDA.

### **Data Preprocessing**

* Performed encoding for categorical variables (e.g., ordinal and frequency encoding for Contract and PaymentMethod).

### **Model Development (Predictive Modeling)**

* Split the data into training and testing sets.
* Trained multiple machine learning models including Logistic Regression, Naive Bayes, Decision Tree, Bagging Classifier, Random Forest, Gradient Boosting, and XGBoost.

## **Model Evaluation and Selection**

* Evaluated models using metrics like recall, precision, accuracy, and F1-score.
* Selected the best-performing model, which in this case was Bagging Classifier based on its highest recall for classifying churned customers (Churn = 1).

## **Business Insights**

* Analyzed feature importance to identify drivers of churn, confirming that Contract, PaymentMethod, MonthlyCharges, and TotalCharges were primary factors.
* Summarized actionable insights to guide retention strategies for high-risk customers.
