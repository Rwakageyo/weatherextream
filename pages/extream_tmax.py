
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
#import plotly.express as px
import matplotlib.pyplot as plt
from PIL import Image

#st.sidebar.image('D:\Radar_Files\Radar_files2DM\extremes\logos.png', use_column_width=True)


image = Image.open('D:\Radar_Files\Radar_files2DM\extremes\logos.png')
image2 = Image.open('D:\Radar_Files\Radar_files2DM\extremes\ext.png')

#st.image(image, caption=None, use_column_width='auto')

col1,col2=st.columns([2,2])

with col1:
    st.image(image,width=360,use_column_width='auto')
with col2:
    st.image(image2,width=360,use_column_width='auto')




st.title(' Rwanda Climate Extremes Breaking Records')

st.markdown('Maximum Temprature extremes')

data = pd.read_csv('D:\Radar_Files\Radar_files2DM\extremes\Tmax.csv')


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


