import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

from PIL import Image

st.set_page_config(
    page_title="Rwanda weather Extrem",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    
)
def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image:('logos.png');
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "My Company Name";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
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
##import hydralit_components as hc

#from PIL import Image
#image = Image.open('logos.png')
#st.image(image)
  
st.title("Minimum Temperature Extremes Breaking Records")

st.markdown("This is the  Temperature Minimum  Extrem values computed from 1986 to 2021 will help a researcher to get to know \
more about the given datasets and it's output")

st.sidebar.markdown("Select the Charts/Plots accordingly:")
data = pd.read_csv("ExtremeTmin.csv")
### data = pd.read_csv('D:\Extremes.csv')

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

st.sidebar.title("Select Visual Charts")
  
chart_visual = st.sidebar.selectbox('Select Charts/Plot type', 
                                    ('Line Chart', 'Bar Chart', 'Bubble Chart'))
  
st.sidebar.checkbox("Show Analysis by Extreme Status", True, key = 1)
selected_status = st.sidebar.selectbox('Select Extreme Status',
                                       options = ['Station', 
                                                  'Value','District','Dates', 
                                                  'Province'])

fig = go.Figure()
  
if chart_visual == 'Line Chart':
    if selected_status == 'Station':
        fig.add_trace(go.Scatter(x = data.Station, y = data.Value,
                                 mode = 'lines',
                                 name = 'Station'))
    if selected_status == 'Elementd':
        fig.add_trace(go.Scatter(x = data.District, y = data.Value,
                                 mode = 'lines', name = 'Value'))
    if selected_status == 'Station':
        fig.add_trace(go.Scatter(x = data.District, y = data.Value,
                                 mode = 'lines',
                                 name = 'Value'))
    if selected_status == 'Value': 
        fig.add_trace(go.Scatter(x=data.District, y=data.Province,
                                 mode='lines',
                                 name="Province"))
  
elif chart_visual == 'Bar Chart':
    if selected_status == 'Station':
        fig.add_trace(go.Bar(x=data.District, y=data.Value,
                             name='Value'))
    if selected_status == 'Element':
        fig.add_trace(go.Bar(x=data.District, y=data.Value,
                             name='Station'))
    if selected_status == 'Province':
        fig.add_trace(go.Bar(x=data.District, y=data.Value,
                             name='Station'))
    if selected_status == 'Unknown':
        fig.add_trace(go.Bar(x=data.District, y=data.Unknown,
                             name="Unknown"))
  
elif chart_visual == 'Bubble Chart':
    if selected_status == 'STNName':
        fig.add_trace(go.Scatter(x=data.District, 
                                 y=data.Value_mm,
                                 mode='markers',
                                 marker_size=[40, 60, 80, 60, 40, 50],
                                 name='STNName'))
          
    if selected_status == 'Elementd':
        fig.add_trace(go.Scatter(x=data.District, y=data.Elements,
                                 mode='markers', 
                                 marker_size=[40, 60, 80, 60, 40, 50],
                                 name='Elementd'))
          
    if selected_status == 'Station':
        fig.add_trace(go.Scatter(x=data.District,
                                 y=data.Station,
                                 mode='markers', 
                                 marker_size=[40, 60, 80, 60, 40, 50],
                                 name = 'Station'))
    if selected_status == 'Station':
        fig.add_trace(go.Scatter(x=data.District,
                                 y=data.Dates,
                                 mode='markers',
                                 marker_size=[40, 60, 80, 60, 40, 50], 
                                 name="Unknown"))
  
st.plotly_chart(fig, use_container_width=True)
