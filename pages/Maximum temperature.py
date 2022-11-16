
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
#import plotly.express as px
#import matplotlib.pyplot as plt
from PIL import Image
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

#st.sidebar.image('D:\Radar_Files\Radar_files2DM\extremes\logos.png', use_column_width=True)


##image = Image.open('D:\Radar_Files\Radar_files2DM\extremes\logos.png')
##image2 = Image.open('D:\Radar_Files\Radar_files2DM\extremes\ext.png')

#st.image(image, caption=None, use_column_width='auto')

##col1,col2=st.columns([2,2])

##with col1:
    ##st.image(image,width=360,use_column_width='auto')
##with col2:
    ##st.image(image2,width=360,use_column_width='auto')


st.title(' Rwanda Climate Extremes Breaking Records')

st.markdown('Maximum Temprature extremes')

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

#District_select = data['District'].drop_duplicates()

District_sidebar = st.sidebar.selectbox('Select a District:', data2)
dataps=data.loc[data.District==District_sidebar]
dataps

st.sidebar.title("Select Visual Charts")
  
chart_visual = st.sidebar.selectbox('Select Charts/Plot type', 
                                    ('Line Chart', 'Bar Chart', 'Bubble Chart'))
  
st.sidebar.checkbox("Show Analysis by Extreme Status", True, key = 1)
selected_status = st.sidebar.selectbox('Select Extreme Status',
                                       options = ['Province', 
                                                  'District','Station_name','Value_mm', 
                                                  'Date'])

fig = go.Figure()
  
if chart_visual == 'Line Chart':
    if selected_status == 'Station_name':
        fig.add_trace(go.Scatter(x = data.District, y = data.Value_mm,
                                 mode = 'lines',
                                 name = 'Station_name'))
    if selected_status == 'District':
        fig.add_trace(go.Scatter(x = data.Station_name, y = data.Value_mm,
                                 mode = 'lines', name = 'District'))
    if selected_status == 'Station_name':
        fig.add_trace(go.Scatter(x = data.District, y = data.Value_mm,
                                 mode = 'lines',
                                 name = 'Station_name'))
    if selected_status == 'Province': 
        fig.add_trace(go.Scatter(x=data.Station_name, y=data.Value_mm,
                                 mode='lines',
                                 name="Province"))
  
elif chart_visual == 'Bar Chart':
    if selected_status == 'Station_name':
        fig.add_trace(go.Bar(x=data.Station_name, y=data.Value_mm,
                             name='Station_name'))
    if selected_status == 'District':
        fig.add_trace(go.Bar(x=data.Station_name, y=data.Value_mm,
                             name='District'))
    if selected_status == 'Province':
        fig.add_trace(go.Bar(x=data.Station_name, y=data.Value_mm,
                             name='Province'))
    if selected_status == 'Dates':
        fig.add_trace(go.Bar(x=data.Station_name, y=data.Value_mm,
                             name="Dates"))
  
elif chart_visual == 'Bubble Chart':
    if selected_status == 'Station_name':
        fig.add_trace(go.Scatter(x=data.Station_name, 
                                 y=data.Value_mm,
                                 mode='markers',
                                 marker_size=[10,20,30,40, 60, 80, 60, 40, 50,60,70,100,110,120,130,140,150],
                                 name='Station_name'))
          
    if selected_status == 'Province':
        fig.add_trace(go.Scatter(x=data.Station_name, y=data.Value_mm,
                                 mode='markers', 
                                 marker_size=[10,20,30,40, 60, 80, 60, 40, 50,60,70,100,110,120,130,140,150],
                                 name='Province'))
          
    if selected_status == 'District':
        fig.add_trace(go.Scatter(x=data.Station_name,
                                 y=data.Value_mm,
                                 mode='markers', 
                                 marker_size=[10,20,30,40, 60, 80, 60, 40, 50,60,70,100,110,120,130,140,150],
                                 name = 'District'))
    if selected_status == 'Station_name':
        fig.add_trace(go.Scatter(x=data.District,
                                 y=data.Value_mm,
                                 mode='markers',
                                 marker_size=[10,20,30,40, 60, 80, 60, 40, 50,60,70,100,110,120,130,140,150],
                                 name="Station_name"))
  
st.plotly_chart(fig, use_container_width=True)


