import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Assignment 8 - Country Data", layout="wide",
                   page_icon=':U+1F979:')

st.header("yeh main table h  idhar sab data visible hai  samja na  ")



file_path = r"C:\Users\Kushal Tripathi\python\Assigment8\cleaned_country_wise_latest.csv"
df = pd.read_csv(file_path)
st.dataframe(df)


st.header(" kuch bhi select karna hoga toh side bar use kr  ", divider="rainbow")

st.sidebar.header("Filter Data")


selected_countries = st.sidebar.multiselect(
    "Select Countries:",
    options=df['Country/Region'].unique(),
    
)
case_type_options = ['Confirmed', 'Deaths', 'Recovered']  # Adjust as needed
if not all(col in df.columns for col in case_type_options):
    st.error("Please ensure your dataset has columns for Confirmed, Deaths, and Recovered.")
else:
    selected_case_type = st.sidebar.selectbox(
        "Select Case Type:",
        case_type_options
    )



df_selection = df.query(
    "`Country/Region` == @selected_countries"
)

st.header("mamu tera selected data idhar dikh  ", divider="rainbow")
st.dataframe(df_selection)


st.header('chalo bye bs itne me itna hi  milega ' ,divider="rainbow")
st.subheader("atlest yeh bar toh full marks de de  plz plz 🥹", divider="rainbow")





