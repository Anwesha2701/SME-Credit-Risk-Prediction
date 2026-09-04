# SME Credit Risk Prediction

This project is an **SME credit risk assessment and default prediction application** built using Python, Logistic Regression, and Streamlit.

The idea behind the project is simple: use a borrower's business, financial and credit information to estimate their **Probability of Default (PD)** and understand their overall credit risk.

## Why I Built This Project

Having worked in credit and risk management, I wanted to explore how the credit assessment process could be supported using **data analytics and machine learning**.

The project takes familiar credit-risk concepts such as repayment behaviour, leverage, cash flow, interest coverage and LTV, and uses them as inputs to a machine-learning model.

It also shows how a trained model can be converted into a simple application that a user can actually interact with.

## Dataset

The project uses a **synthetic SME loan dataset with 12,113 borrower records and 34 variables**.

Synthetic data was used because real borrower-level banking data is confidential. The dataset was designed to represent realistic SME credit characteristics without using confidential customer information.

The data covers areas such as:

* Business and borrower characteristics
* Loan and facility information
* Credit rating and repayment behaviour
* Financial performance
* Cash flow
* Debt and leverage
* Collateral and LTV

## Model Development

I evaluated three classification models:

* Logistic Regression
* Decision Tree
* Random Forest

The final model used in the application is **Logistic Regression**.

Model selection focused primarily on the ability to identify borrowers who actually defaulted, while also considering precision, recall, F1-score and ROC-AUC.

## Variables Used by the Final Model

The final model uses 16 credit, financial and business-related variables:

* Business Vintage
* Employees
* Remaining Loan Tenure
* Existing Credit Exposure
* Existing Credit Facilities
* DPD 30–59 Days
* DPD 60–89 Days
* DPD 90+ Days
* Previous Defaults
* FY2025 Cash Flow from Operations
* EBITDA Margin
* Interest Coverage Ratio
* Debt-to-Revenue Ratio
* Negative CFO Flag
* Serious Credit Event Flag
* Loan-to-Value (LTV)

## Probability of Default

The model estimates the **Probability of Default (PD)** for each borrower.

As per the model configuration used in this application:

* **PD below 20% → Predicted Default: No**
* **PD of 20% or above → Predicted Default: Yes**

## Risk Bands

The application also converts the estimated PD into a simple risk band.

These thresholds are **defined as per the model configurations used in this project** and are not intended to represent universal regulatory or industry thresholds.

| Probability of Default | Risk Band      |
| ---------------------- | -------------- |
| Below 5%               | Very Low Risk  |
| 5% to below 10%        | Low Risk       |
| 10% to below 20%       | Moderate Risk  |
| 20% to below 40%       | High Risk      |
| 40% or above           | Very High Risk |

## Model Performance

The final model was evaluated on a test dataset containing **2,423 observations**, including **291 actual default cases**.

The Logistic Regression model achieved:

* **True Positives:** 161
* **False Positives:** 295
* **True Negatives:** 1,837
* **False Negatives:** 130
* **Precision:** 0.35
* **Recall:** 0.55
* **F1-Score:** 0.43
* **ROC-AUC:** 0.824

A key focus of this project was **True Positives** — identifying as many borrowers who actually defaulted as possible.

## Streamlit Application

The trained model has been integrated into a Streamlit application.

A user can enter the required borrower information and receive:

* Probability of Default
* Risk Band
* Predicted Default classification

The application is intended to demonstrate the complete journey from **credit data and model development to a usable credit-risk assessment tool**.

## Tools Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Streamlit
* Jupyter Notebook

## Disclaimer

This is a portfolio project built using synthetic data designed to represent realistic SME credit characteristics. It does not contain confidential customer information.

The application is intended for analytical and educational purposes and should not be used as the sole basis for actual lending decisions.
