import joblib
import pandas as pd
import streamlit as st

# # -------------------- CUSTOM CSS --------------------
# st.markdown("""
#     <style>
#     /* 1. GLOBAL THEME RESET */
#     :root {
#         --primary-color: #1E3A8A;
#         --background-color: #F8F9FA;
#         --secondary-background-color: #FFFFFF;
#         --text-color: #1E293B;
#         --font: 'Inter', sans-serif;
#     }

#     .stApp {
#         background-color: var(--background-color);
#         color: var(--text-color);
#     }

#     /* 2. FORCE LABEL VISIBILITY */
#     /* This targets the actual text inside the labels */
#     div[data-testid="stWidgetLabel"] p, 
#     .stSlider label, 
#     .stSelectbox label, 
#     .stNumberInput label {
#         color: #1E3A8A !important;
#         font-weight: 700 !important;
#         font-size: 1.1rem !important;
#         opacity: 1 !important;
#     }

#     /* 3. SIDEBAR FIX */
#     [data-testid="stSidebar"] {
#         background-color: #FFFFFF !important;
#         border-right: 1px solid #E2E8F0;
#     }
    
#     [data-testid="stSidebar"] * {
#         color: #1E293B !important;
#     }

#     /* 4. INPUT FIELD STYLING */
#     /* Makes the input boxes look cleaner and prevents "ghosting" */
#     .stSelectbox div[data-baseweb="select"], 
#     .stNumberInput div[data-baseweb="input"] {
#         background-color: #FFFFFF !important;
#         border-radius: 8px !important;
#         border: 1px solid #CBD5E1 !important;
#     }

#     /* 5. BUTTON GRADIENT */
#     .stButton>button {
#         background: linear-gradient(90deg, #1E3A8A 0%, #3B82F6 100%) !important;
#         color: white !important;
#         font-weight: 600 !important;
#         border: none !important;
#         padding: 0.6rem 2rem !important;
#         border-radius: 10px !important;
#         box-shadow: 0 4px 6px rgba(0,0,0,0.1);
#     }
#     </style>
#     """, unsafe_allow_html=True)

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

# -------------------- LOAD MODEL --------------------
model = joblib.load("rf_model.joblib")
model_features = joblib.load("model_columns.joblib")

# # -------------------- LOAD DATA --------------------
df = pd.read_csv("cleaned_df.csv")

# -------------------- HEADER --------------------
st.markdown("""
    <h1 style="text-align: center; font-weight: 800; color: #1E3A8A; margin-bottom: 0px;">
        🏠 PrimeEstate
    </h1>
    """, unsafe_allow_html=True)

st.markdown("""
    <p style="text-align: center; font-weight: 700; font-size: 20px; color: #475569; margin-top: 0px;">
        Premium Real Estate ML Estimator
    </p>
    """, unsafe_allow_html=True)
