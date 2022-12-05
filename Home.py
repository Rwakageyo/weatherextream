import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
##import hydralit_components as hc
from PIL import Image
##image = Image.open('logos.png')
##st.image(image)


st.set_page_config(
    page_title="Rwandan Climate Extremes Monitoring Portal",
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

st.title("Rwandan Climate Extremes Monitoring Portal ")
st.markdown("Welcome to Meteo Rwanda’s online home of the Rwandan climate extremes monitoring portal.This website provides comprehensive and timely information about climate extremes of temperature and rainfall. Climate extremes can have significant social, environmental and economic impacts, with floods and high temperature prime examples. One of the most significant impacts of climate variability and climate change occurs through changes in the frequency and severity of extreme events. This portal has been designed to provide a better basis for monitoring such changes so that we can understand, prepare for and adapt to future changes in extreme events.")

### Metric###########
st.header("Climate Metrics")
st.markdown("The Metrics below indicates the daily breaking records of Rainfall, Maximum  and Minimum temperature  recorded at different weather stations across the country between 1981 and 2022.")
col1, col2, col3,col4 = st.columns(4)
col1.metric(" Maximum Temperature", "70 °C", "1.2 °C")
col2.metric("Minimum Temperature", "15 °C","1.2 °C")
col3.metric("Rainfall", "150 mm","1.2 mm")
###col4.metric("Minimu Temperature", "15 °F","1.2 °F")