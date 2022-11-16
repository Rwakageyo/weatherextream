import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
##import hydralit_components as hc

#from PIL import Image
##image = Image.open('logos.png')
##st.image(image)
  
st.title("Rainfall Extream Dashboard")
st.markdown("The dashboard will help a researcher to get to know \
more about the given datasets and it's output")

st.sidebar.markdown("Select the Charts/Plots accordingly:")
  
data = pd.read_csv("Extremes.csv")
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
                                       options = [' Station_name', 
                                                  'Value_mm','Province','District', 
                                                  'Date'])

fig = go.Figure()
  
if chart_visual == 'Line Chart':
    if selected_status == 'Station_name':
        fig.add_trace(go.Scatter(x = data.District, y = data.Value_mm,
                                 mode = 'lines',
                                 name = 'Value_mm'))
    if selected_status == 'District':
        fig.add_trace(go.Scatter(x = data.Station_name, y = data.Value_mm,
                                 mode = 'lines', name = 'Value_mm'))
    if selected_status == 'Station_name':
        fig.add_trace(go.Scatter(x = data.District, y = data.Value_mm,
                                 mode = 'lines',
                                 name = 'Value_mm'))
    if selected_status == 'Province': 
        fig.add_trace(go.Scatter(x=data.Station_name, y=data.Value_mm,
                                 mode='lines',
                                 name="Province"))
  
elif chart_visual == 'Bar Chart':
    if selected_status == 'Station_name':
        fig.add_trace(go.Bar(x=data.Station_name, y=data.Value_mm,
                             name='Value_mm'))
    if selected_status == 'District':
        fig.add_trace(go.Bar(x=data.Station_name, y=data.Value_mm,
                             name='Station_name'))
    if selected_status == 'Province':
        fig.add_trace(go.Bar(x=data.District, y=data.Value_mm,
                             name='Station_name'))
    if selected_status == 'Dates':
        fig.add_trace(go.Bar(x=data.Station_name, y=data.Value_mm,
                             name="Unknown"))
  
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
                                 name = 'Station_name'))
    if selected_status == 'Station_name':
        fig.add_trace(go.Scatter(x=data.District,
                                 y=data.Value_mm,
                                 mode='markers',
                                 marker_size=[10,20,30,40, 60, 80, 60, 40, 50,60,70,100,110,120,130,140,150],
                                 name="Value_mm"))
  
st.plotly_chart(fig, use_container_width=True)
