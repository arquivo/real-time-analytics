import pandas as pd
from PIL import Image
import plotly.graph_objects as go
import streamlit as st
from gspread_dataframe import get_as_dataframe, set_with_dataframe
import gspread
import argparse

#import pdb;pdb.set_trace()

# Parse args
parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('-j','--pathjson', help='Destination of the json file with google service key', default= "JSON")
parser.add_argument('-k','--key', help='Key Google Spreadsheet', default= "KEY")
parser.add_argument('-ws','--worksheet', help='Worksheet Google Spreadsheet', default= "Data")
args = vars(parser.parse_args())

#Connect gspread
gc = gspread.service_account(filename=args['pathjson'])
sh =  gc.open_by_key(args['key'])
worksheet = sh.worksheet(args['worksheet'])

#Transform worksheet to pandas dataframe
df = get_as_dataframe(worksheet)

#########################################################################################################

#Set image from Arquivo.pt and the Layout
st.set_page_config(layout="wide", page_title="Arquivo.pt in Numbers", page_icon=":chart:")

st.markdown("<div style='text-align: center;'><img src='https://arquivo.pt/img/arquivo-logo-white.svg'></div>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>in Numbers</h1>", unsafe_allow_html=True)

#########################################################################################################

#Load the data from the dataframe
#'Year', 'Total Collections', 'Total Files', 'Total Seeds', 'Total Stored (TB)' -> From the Collection Table
#'Unique Users' -> From AWStats
#colnames=['Year', 'Total Collections', 'Total Files', 'Total Seeds', 'Total Stored (TB)', 'Unique Users']
#df = pd.read_csv("data.csv", sep=';', names=colnames, header=None, encoding='utf-8')

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
    title='Total Nr Collections per Year',
    xaxis_title='Year',
    yaxis_title='Nr Collections'
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
    title='Total Nr Collections per Year Cumulative',
    xaxis_title='Year',
    yaxis_title='Nr Collections'
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
    title='Total Files Collected per Year',
    xaxis_title='Year',
    yaxis_title='Total Files'
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
    title='Total Files per Year Cumulative',
    xaxis_title='Year',
    yaxis_title='Total Files)'
)

#Print the Chart
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
    title='Total URLs Collected per Year',
    xaxis_title='Year',
    yaxis_title='Total URLs'
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
    title='Total URLs Collected per Year Cumulative',
    xaxis_title='Year',
    yaxis_title='Total URLs'
)

#Print the Chart
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
    title='Total Stored (TB) per Year',
    xaxis_title='Year',
    yaxis_title='Total Stored (TB)'
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
    title='Total Stored (TB) per Year Cumulative',
    xaxis_title='Year',
    yaxis_title='Total Stored (TB)'
)

#Print the Chart
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig7)

with col2:
    st.plotly_chart(fig8)

##############################################################################################################

#5) Top domains

#Commandline to get the information
#cat *.cdxj | sort | cut -d ')' -f 1 | uniq -c > out_domain.txt

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
    title='Top 10 Domains in Arquivo.pt',
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
    title='Top 10 .PT Domains in Arquivo.pt',
    xaxis_title='Nr URLs',
    yaxis_title='.PT Domains'
)

#Print the Chart
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig9)

with col2:
    st.plotly_chart(fig10)


##############################################################################################################

###Arquivo404 usage


#Data
months = ['01-2023', '02-2023', '03-2023', '04-2023', '05-2023', '06-2023', '07-2023', '08-2023', '09-2023', '10-2023']
arquivo404_requests = [245, 203, 399, 229, 782, 3531, 13221, 8071, 11054, 1095]

#Create a horizontal bar chart using Plotly
fig9 = go.Figure(data=go.Bar(y=arquivo404_requests, x=months))

#Customize the chart layout
fig9.update_layout(
    title='Nr of Arquivo404 Requests per Month in 2023',
    xaxis_title='Nr Requests',
    yaxis_title='Month'
)

#Data
arquivo404_visits = [62, 23, 93, 18, 84, 377, 1708, 740, 1266, 121]

#Create a horizontal bar chart using Plotly
fig10 = go.Figure(data=go.Bar(y=arquivo404_visits, x=months))

#Customize the chart layout
fig10.update_layout(
    title='Nr of visits in Arquivo.pt from Arquivo404 service per Month in 2023',
    xaxis_title='Nr Visits',
    yaxis_title='Month'
)

#Print the Chart
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig9)

with col2:
    st.plotly_chart(fig10)


##############################################################################################################

###SavePageNow Service usage

#Data
months = ['01-2023', '02-2023', '03-2023', '04-2023', '05-2023', '06-2023', '07-2023', '08-2023', '09-2023', '10-2023']
savepagenow_requests = [255864, 185379, 841209, 118743, 189352, 172161, 154466, 202062, 160998, 11510]

#Create a horizontal bar chart using Plotly
fig11 = go.Figure(data=go.Bar(y=savepagenow_requests, x=months))

#Customize the chart layout
fig11.update_layout(
    title='SavePageNow requests per month (save/now/record/ endpoint)',
    xaxis_title='Nr Requests',
    yaxis_title='Month'
)

#st.plotly_chart(fig11)

#8)Unique users per year

#Prepare your data
categories = df['Year'][1:]
heights = df['Unique Users'][1:].astype(int)


#Create a bar chart object
bar_chart = go.Bar(x=categories, y=heights)

#Create a figure and add the bar chart object
fig12 = go.Figure()
fig12.add_trace(bar_chart)

#Customize the chart (optional)
fig12.update_layout(
    title='Total number of unique users per year',
    xaxis_title='Year',
    yaxis_title='Unique users'
    )


col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig11)

with col2:
    st.plotly_chart(fig12)