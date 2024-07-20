import matplotlib.pyplot as plt  
import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit.elements import html
warnings.filterwarnings("ignore")

st.set_page_config(
    page_title="Weather Forecast",
    page_icon=":sun_small_cloud:",
    layout="wide"
)


st.title("Weather Forecast :sun_small_cloud:")
st.markdown('<style>div.block-container{padding-top:3rem;}</style>', unsafe_allow_html=True) 


#to take the file from the user  
f1 = st.file_uploader("Upload the file", type=["csv", "txt", "xlsx", "xls"])
if f1 is not None:
    filename=f1.name
    st.write(filename)
    df =pd.read_csv(filename)
else: 
    filename = r"C:\Users\Kushal Tripathi\python\Weather Analysis\TestDashBoard\CleanedWeatherData.csv"

df = pd.read_csv(filename)


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





#this is a block of code to pick date (date picker between the range )
st.header("select the country(s) ") 
col1 , col2=st.columns((2))
df["last_updated"]=pd.to_datetime(df["last_updated"])
#gett minmmun and maxmin the date s
startdate =pd.to_datetime(df["last_updated"]).min()
enddate =pd.to_datetime(df["last_updated"]).max()
with col1:
    Date1=pd.to_datetime(st.date_input("strt date :date: ",startdate))
with col2:
    Date2=pd.to_datetime(st.date_input("end  date :date: ",enddate))
df=df[(df["last_updated"]>=Date1)& (df["last_updated"]<=Date2)].copy()    
    
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


    
        

category_df = filtered_df.groupby(by=["location_name"], as_index=False)[
    "temperature_celsius"
].mean()  # Use mean instead of sum for average

# Create container for the first chart title
col1 = st.container()

with col1:
    st.subheader(
        "Average Temperature by Location (Celsius):world_map: and weather:sun_behind_rain_cloud:"
    )

# Create the bar chart for average temperature
fig = px.bar(
    category_df,
    x="location_name",
    y="temperature_celsius",
    template="seaborn",
    title="Average Temperature (°C) by Location",  # Update title
    text=category_df["temperature_celsius"].apply("{:.2f}".format),  # Use correct column name
)


# Display the first chart
st.plotly_chart(fig, use_container_width=True, height=200)

# Create container for the second chart title
col2 = st.container()

with col2:
    st.subheader("Cloud Cover Distribution by Location")

# Create the pie chart for cloud cover
fig = px.pie(filtered_df, values="cloud", names="location_name", hole=0.5)
fig.update_traces(text=filtered_df["location_name"], textposition="outside")
fig.update_layout(title="Cloud Cover Distribution")  # Update title

# Display the second chart
st.plotly_chart(fig, use_container_width=True, height=200)





try:
  df = pd.read_csv(filename)
except FileNotFoundError:
  print("Error: File not found. Please provide the correct file path.")
  exit()

# Select temperature data (Celsius or Fahrenheit)
temperature_column = 'temperature_celsius'  # Replace with 'temperature_fahrenheit' if needed
locations = df['location_name'].tolist()
temperatures = df[temperature_column].tolist()

# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(locations, temperatures, color='skyblue')
plt.xlabel("Location")
plt.ylabel(f"Temperature (°{temperature_column.upper()})")
plt.title(f"Average {temperature_column.upper()} Temperatures in Different Locations")
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()




def create_graph(df, x_axis, y_axis, chart_type="histogram"):
  
  if x_axis == "country":
    # Assume country names are categorical (not numerical)
    fig = px.bar(df, x=x_axis, y=y_axis, title=f"{y_axis} by Country")
  else:
    # Use scatter plot for other x-axis data (assuming numerical)
    fig = px.histogram(df, x=x_axis, y=y_axis, title=f"{y_axis} vs {x_axis}")
  return fig
def display_graphs(df):
  
  with col1:
    st.subheader("Data Visualization")
    x_axis_options = ["country"] + [col for col in df.columns if col != "country"]
    y_axis_options = df.columns

    selected_x_axis = st.selectbox("Select X-axis", x_axis_options)
    selected_y_axis = st.selectbox("Select Y-axis", y_axis_options)

    if selected_x_axis and selected_y_axis:
      fig = create_graph(df.copy(), selected_x_axis, selected_y_axis)
      st.plotly_chart(fig, use_container_width=True)
display_graphs(df)


if not filtered_df.empty:
    st.subheader("Filtered Weather Data")
    st.write(filtered_df)  # Display the filtered DataFrame
else:
    # No data message (optional)
    if not country_selection:
        st.write("Please select one or more countries to view weather data.")
    else:
        st.write("No data found based on your filter selections.")




