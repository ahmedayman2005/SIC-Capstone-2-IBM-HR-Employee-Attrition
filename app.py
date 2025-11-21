import streamlit as st
import pickle
import joblib
import pandas as pd

# -------------------- Load artifacts --------------------
with open("xgb_model.pkl", "rb") as f:
    model = pickle.load(f)

scaler = joblib.load("scaler2.pkl")

with open("xgb_model_col.pkl", "rb") as f:
    feature_columns = pickle.load(f)  # expected order for the model

# -------------------- Page config & styling --------------------
st.set_page_config(page_title="Employee Attrition Predictor", layout="wide")

st.markdown("""
<style>
/* tighten overall padding */
.block-container {padding-top: 1.2rem;}

/* Sidebar look */
section[data-testid="stSidebar"] .block-container {padding-top: 1rem;}
.sidebar-title {font-weight:700; font-size:1.05rem; margin-top:.3rem; margin-bottom:.5rem;}
.sidebar-section {font-weight:600; margin: .8rem 0 .3rem 0;}
hr.sidebar-divider {border: 0; height: 1px; background: #3a3a3a; margin: .6rem 0 .6rem 0;}

/* Predict button on the right – big and bold */
button[kind="primary"] {
  width: 260px; height: 46px; font-weight: 700; border-radius: .5rem;
}

/* Result card */
.result-ok {
  background: #1b4332; color: #d8f3dc; padding: .9rem 1.0rem; border-radius: .6rem;
  border: 1px solid #2d6a4f;
}
.result-bad {
  background: #5c2b29; color: #ffe3e0; padding: .9rem 1.0rem; border-radius: .6rem;
  border: 1px solid #8a3a37;
}

.centered {
    text-align: center;
}
button[kind="primary"] {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 260px;
    height: 48px;
    font-weight: 600;
    border-radius: 8px;
}
.result-ok {
  background: #1b4332; color: #d8f3dc; padding: .9rem 1.0rem; border-radius: .6rem;
  border: 1px solid #2d6a4f; text-align:center;
}
.result-bad {
  background: #5c2b29; color: #ffe3e0; padding: .9rem 1.0rem; border-radius: .6rem;
  border: 1px solid #8a3a37; text-align:center;
}


</style>
""", unsafe_allow_html=True)

# -------------------- Layout: sidebar (inputs) | main (title / predict / result) --------------------
sidebar = st.sidebar
main_col = st.container()

# ========== LEFT SIDEBAR ==========
sidebar.markdown('<div class="sidebar-title">Employee Details</div>', unsafe_allow_html=True)


# Personal & commute
sidebar.markdown('<div class="sidebar-section"> Personal & Commute</div>', unsafe_allow_html=True)
age = sidebar.number_input("Age", 18, 65, 30, step=1)
monthly_income = sidebar.number_input("Monthly Income", 1000, 200000, 5000, step=100)
distance = sidebar.slider("Distance From Home (km)", 0, 100, 5, step=1)


# Divider
sidebar.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)

# Work Factors section (your 8 model features grouped nicely)
sidebar.markdown('<div class="sidebar-section"> Work Factors</div>', unsafe_allow_html=True)

# Feature inputs (ONLY the 8 used by your model)
job_level = sidebar.selectbox("Job Level", [1, 2, 3, 4, 5], index=0)
salary_hike = sidebar.slider("Percent Salary Hike (%)", 0, 50, 15, step=1)
years_with_manager = sidebar.number_input("Years With Current Manager", 0, 40, 2, step=1)
num_companies = sidebar.number_input("Number of Companies Worked", 0, 20, 1, step=1)
total_work_years = sidebar.number_input("Total Working Years", 0, 50, 5, step=1)



# Build input row exactly in the order your model expects
input_row = [
    job_level,
    salary_hike,
    years_with_manager,
    num_companies,
    total_work_years,
    age,
    monthly_income,
    distance
]
input_df = pd.DataFrame([input_row], columns=feature_columns)
input_scaled = scaler.transform(input_df)

# ========== RIGHT MAIN AREA ==========
st.markdown("<h2 class='centered'>🚀 Employee Attrition Predictor</h2>", unsafe_allow_html=True)
st.markdown("<p class='centered'>Predict if an employee is likely to leave based on key factors.</p>", unsafe_allow_html=True)

# Centered Predict button
go = st.button("🎯 Predict Attrition Risk", type="primary")


# Results
if go:
    pred = model.predict(input_scaled)[0]
    proba = model.predict_proba(input_scaled)[0]  # [stay, leave]

    st.write("")  # small gap
    if pred == 1:
        st.markdown(
            f'<div class="result-bad">⚠️ <b>High Attrition Risk</b> — This employee is likely to <b>leave</b>. '
            f'Chance of leaving: <b>{proba[1]*100:.1f}%</b></div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f'<div class="result-ok">✅ <b>Low Attrition Risk</b> — This employee is likely to <b>stay</b>. '
            f'Chance of leaving: <b>{proba[1]*100:.1f}%</b></div>',
            unsafe_allow_html=True
        )

    st.markdown("### Prediction Probabilities")
    st.write(f"**Stay:** {proba[0]:.2f} &nbsp;&nbsp;|&nbsp;&nbsp; **Leave:** {proba[1]:.2f}")

