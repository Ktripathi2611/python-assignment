
import streamlit as st #to launch  webpage
from streamlit_option_menu import option_menu
import plotly.express as px  #to plot the graph,chartss 
import pandas as pd #to manipulate the data 
import os #to navigate  the file
import warnings
warnings.filterwarnings("ignore")
st.set_page_config( page_title="weather forcast",
                   page_icon=":sun_small_cloud:",
                   layout="wide"
                   )
st.title("Weather Forecast :sun_small_cloud:")
st.markdown('<style>div.block-container{padding-top:4rem;}</style>', unsafe_allow_html=True)
f1 = st.file_uploader("Upload the file", type=["csv", "txt", "xlsx", "xls"])
if f1 is not None:
    filename=f1.name
    st.write(filename)
    df =pd.read_csv(filename)
else: 
    filename = "C:/Users/Kushal Tripathi/python/Weather Analysis/archive/GlobalWeatherRepository.csv"

df = pd.read_csv(filename)




st.markdown("# Header of the Page")
st.markdown("Welcome to our weather analysis data.")


try:
  from streamlit_option_menu import option_menu
except ModuleNotFoundError:
  st.error("Please install the 'streamlit-option-menu' package: pip install streamlit-option-menu")
  exit()

selected = option_menu(
    menu_title=None,
    options=["Home", "Project", "Contact"],
    icons=["house", "book", "envelop"],
    orientation="horizontal"
)
# Additional logic based on the selected option (optional)
if selected == "Home":
    # Display content for the Home page
    st.write("This is the Home page content.")
elif selected == "Project":
    # Display content for the Project page
    st.write("This is the Project page content.")
elif selected == "Contact":
    # Display content for the Contact page
    st.write("This is the Contact page content.")

# if selected == 'Project':

st.sidebar.header("Select Country and Location")
country_selection = st.sidebar.multiselect("Select Country(ies):", df["country"].unique())
filtered_df = df.copy()  # Start with a copy
if country_selection:
    filtered_df = filtered_df[filtered_df['country'].isin(country_selection)]
condition_text = st.sidebar.multiselect(
    "Select Weather Condition(s):", filtered_df["condition_text"].unique()
)
if condition_text:
    filtered_df = filtered_df[filtered_df['condition_text'].isin(condition_text)]
if not filtered_df.empty:
    st.write("Filtered Weather Data:")
    st.table(filtered_df)  # Display data in a table format
else:
    st.write("No data found based on your filter selections.")







st.header("Weather Data Analysis")
country_options = df["country"].unique()
country_selection = st.multiselect("Select Country(ies):", country_options)
filtered_df = df.copy() 
filtered_df = filtered_df[filtered_df['country'].isin(country_selection)]
if not filtered_df.empty:
    condition_options = filtered_df["condition_text"].unique()
    condition_text = st.multiselect(
        "Select Weather Condition(s):", condition_options
    )

    filtered_df = filtered_df[filtered_df['condition_text'].isin(condition_text)]

if not filtered_df.empty:
    st.subheader("Filtered Weather Data")
    st.write(filtered_df)  # Display the filtered DataFrame
else:
    # No data message (optional)
    if not country_selection:
        st.write("Please select one or more countries to view weather data.")
    else:
        st.write("No data found based on your filter selections.")


