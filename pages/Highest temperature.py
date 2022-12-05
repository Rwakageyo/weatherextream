
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
#import plotly.express as px
##import matplotlib.pyplot as plt
from PIL import Image


st.set_page_config(
    page_title="Rwanda weather Extremes",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    
)

image = Image.open('Govlogo.png')
image2 = Image.open('logos.png')

##st.image(image, caption=None, use_column_width='auto')

col1,col2=st.columns([2,2])

with col1:
    st.image(image,width=30,use_column_width='auto')
with col2:
    st.image(image2,width=30,use_column_width='auto')


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


st.title(' Highest Maximum Temperature Records')

st.markdown("The table below indicates the daily breaking records of maximum temperature recorded at different weather stations across the country. The records are based on the entire available data for each station from when it started operation.")

st.sidebar.markdown("The Below menu allows users to select regions of their interest.")
data = pd.read_csv('Tmax.csv')


###st.table(data)

####data.style.format(precision=0)

Province_select = data['Province'].drop_duplicates()


Province_sidebar = st.sidebar.selectbox('Select a Province:', Province_select)

# Get dataframe where Province is the Province_sidebar.
data1 = data.loc[data.Province == Province_sidebar]

# Get the District column from df1.
data2 = data1['District'].drop_duplicates()
#data2 = data1.District


# Show df2 in the side bar.
#District_select = data['District'].drop_duplicates()
District_sidebar = st.sidebar.selectbox('Select a District:', data2)
dataps=data.loc[data.District==District_sidebar]
dataps


st.markdown("The Metrics below indicates the daily breaking records of Rainfall, Maximum  and Minimum temperature  recorded at different weather stations across the country between 1981 and 2022.")


###st.bar_chart(data,x="Station", y="Value")
st.header("  Chart")
st.bar_chart(data1,x="Station", y="Value ")

##st.line_chart(data1,x="Station", y="Value")


### Metric###########
st.header("Climate Metrics")
st.markdown("The Metrics below indicates the daily breaking records of Rainfall, Maximum  and Minimum temperature  recorded at different weather stations across the country between 1981 and 2022.")
col1, col2, col3,col4 = st.columns(4)
col1.metric(" Maximum Temperature", "70 °C", "1.2 °C")
col2.metric("Minimum Temperature", "15 °C","1.2 °C")
col3.metric("Rainfall", "150 mm","1.2 mm")
###col4.metric("Minimu Temperature", "15 °F","1.2 °F")


fig = go.Figure()



