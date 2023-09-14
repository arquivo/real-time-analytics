import pandas as pd
import streamlit as st
from PIL import Image
import plotly.graph_objects as go
import streamlit as st
import PyPDF2
import re

st.set_page_config(layout="wide", page_title="Arquivo.pt em números", page_icon=":chart:")

st.markdown("<div style='text-align: center;'><img src='https://arquivo.pt/img/arquivo-logo-white.svg'></div>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>em números</h1>", unsafe_allow_html=True)

#Load the data from the dataframe
#colnames=['Year', 'January - April Size', 'May - August Size', 'September - December Size', 'Total Year Size', 'January - April Nr Collections', 'May - August Nr Collections', 'September - December Nr Collections', 'Total Year Nr Collections'] 
#df = pd.read_csv("1.csv", sep=',', names=colnames, header=None)

colnames=['Year', 'Total Collections', 'Total Files', 'Total Seeds', 'Total Stored (TB)', 'Unique Users'] 
df = pd.read_csv("2.csv", sep=';', names=colnames, header=None)

#########################################################################################################

#1) Number of collections per year

#Prepare your data
categories = df['Year'][1:]
heights = df['Total Collections'][1:].astype(int)

#Create a bar chart object
bar_chart = go.Bar(x=categories, y=heights)

#Create a figure and add the bar chart object
fig1 = go.Figure()
fig1.add_trace(bar_chart)

#Customize the chart (optional)
fig1.update_layout(
    title='Total nr collections per year',
    xaxis_title='Year',
    yaxis_title='Nr collections'
    )

#Cumulative
df['Cumulative'] = df['Total Collections'][1:].astype(int).cumsum()
print(df['Cumulative'])

#Create a bar chart object
bar_chart = go.Bar(x=categories, y=df['Cumulative'])

#Create a figure and add the bar chart object
fig2 = go.Figure()
fig2.add_trace(bar_chart)

#Customize the chart (optional)
fig2.update_layout(
    title='Total nr collections per year cumulative',
    xaxis_title='Year',
    yaxis_title='Nr collections'
)

#st.plotly_chart(fig1)
#st.plotly_chart(fig2)

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig1)

with col2:
    st.plotly_chart(fig2)

##############################################################################################################

#2) Number of files per year

#Prepare your data
categories = df['Year'][1:]
heights = df['Total Files'][1:].astype(int)

#Create a bar chart object
bar_chart = go.Bar(x=categories, y=heights)

#Create a figure and add the bar chart object
fig3 = go.Figure()
fig3.add_trace(bar_chart)

#Customize the chart (optional)
fig3.update_layout(
    title='Total files per year',
    xaxis_title='Year',
    yaxis_title='Total files'
    )

#Cumulative
df['Cumulative'] = df['Total Files'][1:].astype(int).cumsum()
print(df['Cumulative'])

#Create a bar chart object
bar_chart = go.Bar(x=categories, y=df['Cumulative'])

#Create a figure and add the bar chart object
fig4 = go.Figure()
fig4.add_trace(bar_chart)

#Customize the chart (optional)
fig4.update_layout(
    title='Total files per year cumulative',
    xaxis_title='Year',
    yaxis_title='Total files)'
)

#st.plotly_chart(fig3)
#st.plotly_chart(fig4)

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig3)

with col2:
    st.plotly_chart(fig4)


##############################################################################################################

#3) Number of seeds per year

#Prepare your data
categories = df['Year'][1:]
heights = df['Total Seeds'][1:].astype(int)

#Create a bar chart object
bar_chart = go.Bar(x=categories, y=heights)

#Create a figure and add the bar chart object
fig5 = go.Figure()
fig5.add_trace(bar_chart)

#Customize the chart (optional)
fig5.update_layout(
    title='Total seeds per year',
    xaxis_title='Year',
    yaxis_title='Total seeds'
    )

#Cumulative
df['Cumulative'] = df['Total Seeds'][1:].astype(int).cumsum()
print(df['Cumulative'])

#Create a bar chart object
bar_chart = go.Bar(x=categories, y=df['Cumulative'])

#Create a figure and add the bar chart object
fig6 = go.Figure()
fig6.add_trace(bar_chart)

#Customize the chart (optional)
fig6.update_layout(
    title='Total seeds per year cumulative',
    xaxis_title='Year',
    yaxis_title='Total seeds'
)

#st.plotly_chart(fig5)
#st.plotly_chart(fig6)

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig5)

with col2:
    st.plotly_chart(fig6)


##############################################################################################################

#4) Total stored per year

#Prepare your data
categories = df['Year'][1:]
heights = df['Total Stored (TB)'][1:].astype(int)

#Create a bar chart object
bar_chart = go.Bar(x=categories, y=heights)

#Create a figure and add the bar chart object
fig7 = go.Figure()
fig7.add_trace(bar_chart)

#Customize the chart (optional)
fig7.update_layout(
    title='Total stored (TB) per year',
    xaxis_title='Year',
    yaxis_title='Total stored (TB)'
    )

#Cumulative
df['Cumulative'] = df['Total Stored (TB)'][1:].astype(int).cumsum()
print(df['Cumulative'])

#Create a bar chart object
bar_chart = go.Bar(x=categories, y=df['Cumulative'])

#Create a figure and add the bar chart object
fig8 = go.Figure()
fig8.add_trace(bar_chart)

#Customize the chart (optional)
fig8.update_layout(
    title='Total stored (TB) per year cumulative',
    xaxis_title='Year',
    yaxis_title='Total stored (TB)'
)

#st.plotly_chart(fig7)
#st.plotly_chart(fig8)

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig7)

with col2:
    st.plotly_chart(fig8)

##############################################################################################################

#5) Top domains

#cat Roteiro.cdxj | cut -d ')' -f 1 | uniq -c
#cat *.cdxj | sort | cut -d ')' -f 1 | uniq -c

#Data
cities = ['fortunecity.com', 'dre.pt', 'members.fortunecity.com', 'yt3.ggpht.com', 'geocities.com', 'youtube.com', 'publico.pt', 'tek.sapo.pt', 'noticiasdacovilha.pt', 'regiaodeagueda.com']
population = [43230045, 43640068, 26301933, 21862962, 16983647, 14926793, 13163730, 12373934, 11376784, 10944150]

#Sort the cities based on population in descending order
sorted_data = sorted(zip(population, cities))
population, cities = zip(*sorted_data)

#Create a horizontal bar chart using Plotly
fig9 = go.Figure(data=go.Bar(y=cities, x=population, orientation='h'))

#Customize the chart layout
fig9.update_layout(
    title='Top 10 domains in Arquivo.pt',
    xaxis_title='Nr URLs',
    yaxis_title='Domains'
)

#Data
cities = ['dre.pt', 'publico.pt', 'tek.sapo.pt', 'noticiasdacovilha.pt', 'destak.pt', 'sabado.pt', 'iol.tvi24.pt', 'jornaldofundao.pt', 'jornaldoalgarve.pt', 'tsf.pt']
population = [43640068, 13163730, 12373934, 11376784, 9858192, 9771033, 9722996, 9510040, 9452618, 9339705]

#Sort the cities based on population in descending order
sorted_data = sorted(zip(population, cities))
population, cities = zip(*sorted_data)

#Create a horizontal bar chart using Plotly
fig10 = go.Figure(data=go.Bar(y=cities, x=population, orientation='h'))

#Customize the chart layout
fig10.update_layout(
    title='Top 10 PT domains in Arquivo.pt',
    xaxis_title='Nr URLs',
    yaxis_title='PT Domains'
)

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig9)

with col2:
    st.plotly_chart(fig10)

##############################################################################################################

#6)Unique users per year

#Prepare your data
categories = df['Year'][1:]
heights = df['Unique Users'][1:].astype(int)


#Create a bar chart object
bar_chart = go.Bar(x=categories, y=heights)

#Create a figure and add the bar chart object
fig11 = go.Figure()
fig11.add_trace(bar_chart)

#Customize the chart (optional)
fig11.update_layout(
    title='Total number of unique users per year',
    xaxis_title='Year',
    yaxis_title='unique users'
    )

st.plotly_chart(fig11)


##############################################################################################################


# Add a sidebar for the 'Year' field
#selected_year = st.sidebar.selectbox('Select Year', df['Year'])

# Filter the data based on the selected year
#filtered_df = df[df['Year'] == selected_year]

# Display the filtered data
#st.write(filtered_df)





#Quando dados fizemos
#Quando paginas salvamos
#Quando links citados 
#Quantas links recolhemos
