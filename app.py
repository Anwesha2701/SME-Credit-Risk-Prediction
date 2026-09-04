
import streamlit as st
import joblib
import pandas as pd

saved = joblib.load("SME_credit_risk_model.pkl")

model = saved["model"]
scaler = saved["scaler"]
features = saved["features"]
threshold = saved["threshold"]

st.title("SME Credit Risk Predictor")

st.write(
    "Enter the borrower's business, financial and credit information "
    "to estimate the Probability of Default (PD) and assess the borrower's credit risk."
)

st.subheader("Objective")

st.write(
    "The objective of this application is to identify borrowers who may have "
    "a higher likelihood of default based on their financial strength, "
    "leverage, repayment behaviour and credit history."
)
st.subheader("How to Interpret the Result")

st.write(
    "**Probability of Default (PD):** "
    "The estimated likelihood that the borrower may default on the loan."
)

st.write(
    "**Risk Band:** "
    "The PD is translated into a simple risk category ranging from "
    "Very Low Risk to Very High Risk."
)

st.write(
    "**Predicted Default:** "
    "The model classifies the borrower as Predicted Default = Yes when "
    "the estimated PD is 20% or higher. If the PD is below 20%, the "
    "classification is Predicted Default = No."
)
st.subheader("How to Interpret the Result")

st.write(
    "**Probability of Default (PD):** "
    "The estimated likelihood that the borrower may default on the loan."
)

st.write(
    "**Risk Band:** "
    "The PD is translated into a simple risk category ranging from "
    "Very Low Risk to Very High Risk."
)

st.write(
    "**Predicted Default:** "
    "The model classifies the borrower as Predicted Default = Yes when "
    "the estimated PD is 20% or higher. If the PD is below 20%, the "
    "classification is Predicted Default = No."
)
st.subheader("Risk Band Guide")

st.write(
    "The following risk bands are defined as per the model configurations "
    "used in this application. They are project-specific thresholds used "
    "to interpret the model's estimated Probability of Default (PD)."
)

st.write("**Very Low Risk:** PD < 5%")
st.write("**Low Risk:** PD 5%–<10%")
st.write("**Moderate Risk:** PD 10%–<20%")
st.write("**High Risk:** PD 20%–<40%")
st.write("**Very High Risk:** PD ≥ 40%")
st.subheader("1. Business Profile")
# Business Vintage years
business_vintage = st.number_input(
    "Business Vintage (Years)",
    min_value=0.0,
    value=None,
    placeholder="Enter business vintage",
    help="Enter the number of years the business has been operating. This cannot be negative."
)
# No of employees
employees = st.number_input(
    "Number of Employees",
    min_value=0,
    value=None,
    placeholder="Enter number of employees",
    help="Enter the number of years the business has been operating. This cannot be negative."
)
# Remaining tenure
remaining_tenure = st.number_input(
    "Remaining Tenure (Months)",
    min_value=0,
    value=None,
    placeholder="Enter remaining tenure",
    help="Enter the current number of employees. This cannot be negative."
)
st.subheader("2. Credit & Repayment Behaviour")
# Existing exposure
existing_exposure = st.number_input(
    "Existing Exposure (₹ Crore)",
    min_value=0.0,
    value=None,
    placeholder="Enter existing exposure",
    help="Enter the remaining loan tenure in months. This cannot be negative."
)
# Existing Facilities
existing_facilities = st.number_input(
    "Existing Facilities Count",
    min_value=0,
    value=None,
    placeholder="Enter number of existing facilities",
    help="Enter the borrower's existing credit exposure. This cannot be negative."
)
# DPD 30_50 days
dpd_30_59 = st.number_input(
    "DPD 30–59 Days Count",
    min_value=0,
    value=None,
    placeholder="Enter count",
    help="Enter the number of instances where payments were 30–59 days past due. This cannot be negative."
)
# DPD 60_89 days
dpd_60_89 = st.number_input(
    "DPD 60–89 Days Count",
    min_value=0,
    value=None,
    placeholder="Enter count",
    help="Enter the number of instances where payments were 60–89 days past due. This cannot be negative."
)
# DPD 90_plus days
dpd_90_plus = st.number_input(
    "DPD 90+ Days Count",
    min_value=0,
    value=None,
    placeholder="Enter count",
    help="Enter the number of instances where payments were 90 or more days past due. This cannot be negative."
)
# Previous Defaults
previous_defaults = st.number_input(
    "Previous Defaults",
    min_value=0,
    value=None,
    placeholder="Enter number of previous defaults",
    help="Enter the number of previous loan defaults. This cannot be negative."
)
st.subheader("3. Financial Strength & Leverage")
# FY2025 CFO
fy2025_cfo = st.number_input(
    "FY2025 CFO (₹ Crore)",
    value=None,
    placeholder="Enter FY2025 CFO",
    help="Enter FY2025 cash flow from operations. This can be positive or negative."
)

# EBITDA Margin
ebitda_margin = st.number_input(
    "EBITDA Margin (%)",
    value=None,
    placeholder="Enter EBITDA margin",
    help="Formula: EBITDA Margin = (EBITDA ÷ Revenue) × 100. Example: EBITDA ₹5 Cr ÷ Revenue ₹50 Cr × 100 = 10%. The value can be positive or negative depending on business performance."
)

# Interest Coverage Ratio
interest_coverage_ratio = st.number_input(
    "Interest Coverage Ratio",
    value=None,
    placeholder="Enter interest coverage ratio",
    help="Formula: Interest Coverage Ratio = EBIT ÷ Interest Expense. Example: EBIT ₹10 Cr ÷ Interest Expense ₹2 Cr = 5.0 times.The ratio can be positive or negative depending on the borrower's earnings."
)

# Debt to Revenue
debt_to_revenue = st.number_input(
    "Debt to Revenue",
    min_value=0.0,
    value=None,
    placeholder="Enter debt to revenue",
    help="Formula: Debt-to-Revenue Ratio = Total Debt ÷ Revenue. Example: Total Debt ₹30 Cr ÷ Revenue ₹60 Cr = 0.50. The ratio cannot be negative."
)

# Negative CFO Flag
negative_cfo_flag = st.selectbox(
    "Negative CFO Flag",
    options=[0, 1],
    index=None,
    placeholder="Select 0 or 1",
    help="Select 1 if the borrower's cash flow from operations is negative. Select 0 if it is not negative."
)

# Serious Credit Event Flag
serious_credit_event_flag = st.selectbox(
    "Serious Credit Event Flag",
    options=[0, 1],
    index=None,
    placeholder="Select 0 or 1",
    help="Select 1 if the borrower has experienced a significant adverse credit event such as NPA classification, restructuring due to financial stress, write-off, serious repayment failure, or insolvency proceedings. Otherwise select 0."
)

# LTV
ltv = st.number_input(
    "LTV (%)",
    min_value=0.0,
    value=None,
    placeholder="Enter LTV",
    help="Formula: LTV = (Loan Amount ÷ Collateral Value) × 100. Example: Loan ₹50 Cr ÷ Collateral ₹100 Cr × 100 = 50%. LTV cannot be negative. There is no fixed 100% upper limit in this application."
)

X_input = pd.DataFrame([[
    business_vintage,
    employees,
    remaining_tenure,
    existing_exposure,
    existing_facilities,
    dpd_30_59,
    dpd_60_89,
    dpd_90_plus,
    previous_defaults,
    fy2025_cfo,
    ebitda_margin,
    interest_coverage_ratio,
    debt_to_revenue,
    negative_cfo_flag,
    serious_credit_event_flag,
    ltv
]], columns=features)

if st.button("Predict Credit Risk"):

    if X_input.isna().any().any():

        st.error("Please enter all 16 borrower details before making a prediction.")
   
    else:

        X_scaled = scaler.transform(X_input)

        pd_probability = model.predict_proba(X_scaled)[0][1]

        predicted_default = int(pd_probability >= threshold)

        if pd_probability < 0.05:
         risk_band = "Very Low Risk"
        elif pd_probability < 0.10:
         risk_band = "Low Risk"
        elif pd_probability < 0.20:
         risk_band = "Moderate Risk"
        elif pd_probability < 0.40:
         risk_band = "High Risk"
        else:
         risk_band = "Very High Risk"


        st.subheader("Credit Risk Assessment")

        st.metric(
            "Probability of Default",
            f"{pd_probability:.2%}"
)

        st.write(f"**Risk Band:** {risk_band}")

        if risk_band == "Very Low Risk":
            st.write("The borrower has a relatively low estimated probability of default.")

        elif risk_band == "Low Risk":
            st.write("The borrower has a low estimated probability of default.")

        elif risk_band == "Moderate Risk":
            st.write("The borrower has a moderate estimated probability of default and may require additional review.")

        elif risk_band == "High Risk":
            st.write("The borrower has a high estimated probability of default and requires closer credit review.")

        else:
            st.write("The borrower has a very high estimated probability of default and requires careful credit assessment.")
        if predicted_default == 1:
            st.error("**Predicted Default:** Yes")
        else:
            st.success("**Predicted Default:** No")

st.divider()

st.subheader("Disclaimer")

st.write(
    "This application is developed as a portfolio project using synthetic data "
    "designed to represent realistic SME credit characteristics. The dataset "
    "does not contain confidential customer information. The application is "
    "intended for analytical and educational purposes and should not be used "
    "as the sole basis for actual lending decisions."
)
