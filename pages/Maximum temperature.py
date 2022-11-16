
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
#import plotly.express as px
##import matplotlib.pyplot as plt
from PIL import Image

st.set_page_config(
    page_title="Rwanda weather Extrem",
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


hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """

st.markdown(hide_menu_style, unsafe_allow_html=True)

st.title(' Rwanda Climate Extremes Breaking Records')

st.markdown("This is the  Maximum Temperature  Extrem values computed from 1986 to 2021 will help a researcher to get to know \
more about the given datasets and it's output")

data = pd.read_csv('Tmax.csv')


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

fig = go.Figure()


