import streamlit as st
import pandas as pd
import plotly as plt
import plotly.graph_objects as go
  
st.title("Rwanda Weather Extrem Dashboard")
st.markdown("The dashboard will help a researcher to get to know \
more about the given datasets and it's output")

st.sidebar.markdown("Select the Charts/Plots accordingly:")
  
data = pd.read_csv("C:/Users/METEO/Desktop/streamlite/extremes.csv")
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
  
st.sidebar.checkbox("Show Analysis by Extreme Status", True, key = 3)
selected_status = st.sidebar.selectbox('Select Extreme Status',
                                       options = ['STN_Name', 
                                                  'Value_mm','District', 
                                                  'Province'])

fig = go.Figure()
  
if chart_visual == 'Line Chart':
    if selected_status == 'STN_Name':
        fig.add_trace(go.Scatter(x = data.STN_Name, y = data.Value_mm,
                                 mode = 'lines',
                                 name = 'District'))
    if selected_status == 'Elementd':
        fig.add_trace(go.Scatter(x = data.District, y = data.Element,
                                 mode = 'lines', name = 'Elements'))
    if selected_status == 'Never_Elementd':
        fig.add_trace(go.Scatter(x = data.District, y = data.Never_Elementd,
                                 mode = 'lines',
                                 name = 'Never_Elementd'))
    if selected_status == 'Value_mm': 
        fig.add_trace(go.Scatter(x=data.District, y=data.Value_mm,
                                 mode='lines',
                                 name="Value_mm"))
  
elif chart_visual == 'Bar Chart':
    if selected_status == 'STNName':
        fig.add_trace(go.Bar(x=data.District, y=data.STN_Name,
                             name='STN_Name'))
    if selected_status == 'Element':
        fig.add_trace(go.Bar(x=data.District, y=data.Value_mm,
                             name='Value_mm'))
    if selected_status == 'Never_Element':
        fig.add_trace(go.Bar(x=data.District, y=data.Element,
                             name='Never_Elementd'))
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
          
    if selected_status == 'Never_Elementd':
        fig.add_trace(go.Scatter(x=data.District,
                                 y=data.Never_Elementd,
                                 mode='markers', 
                                 marker_size=[40, 60, 80, 60, 40, 50],
                                 name = 'Never_Elementd'))
    if selected_status == 'Unknown':
        fig.add_trace(go.Scatter(x=data.District,
                                 y=data.Value_mm,
                                 mode='markers',
                                 marker_size=[40, 60, 80, 60, 40, 50], 
                                 name="Unknown"))
  
st.plotly_chart(fig, use_container_width=True)
