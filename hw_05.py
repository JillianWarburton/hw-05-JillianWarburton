import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st
import re

url = 'https://github.com/esnt/Data/raw/main/Names/popular_names.csv'

df = pd.read_csv(url)

st.title("Popular Baby Names")

# Add a text input with regex validation
selected_name = st.text_input("Enter a name:", placeholder="Enter a name here", max_chars=15)

fig = px.line(df[df['name']==selected_name], x='year',y='n', color='sex', hover_data=['n'],
              title='Line Plot', color_discrete_sequence=['#FF69B4', '#0000FF'])
fig.update_layout(title=f'Name Trends for {selected_name}')
fig.update_layout(title={'text': f'Name Trends for {selected_name} between 1910-2021', 
                         'font': {'size': 24}})

# Update the x and y axis names
fig.update_xaxes(title='Year', range=[1910, 2021])
fig.update_yaxes(title='Number', range=[0,None])

st.plotly_chart(fig)