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
parser.add_argument('-k1','--key1', help='Key Google Spreadsheet Real Time Analytics', default= "KEY")
parser.add_argument('-ws1','--worksheet1', help='Worksheet Google Spreadsheet Real Time Analytics', default= "Data")
parser.add_argument('-k2','--key2', help='Key Google Spreadsheet Metrics of APIs and services', default= "KEY")
parser.add_argument('-ws2','--worksheet2', help='Worksheet Google Spreadsheet Metrics of APIs and services', default= "Summary Year")
args = vars(parser.parse_args())

gc =  gspread.service_account(args['pathjson'])
sh =  gc.open_by_key(args['key1'])
worksheet = sh.worksheet(args['worksheet1'])

#Transform worksheet to pandas dataframe
df = get_as_dataframe(worksheet)

#########################################################################################################

#Set the layout and the image from Arquivo.pt

st.set_page_config(layout="wide", page_title="Arquivo.pt in Numbers", page_icon=":chart:")

st.markdown("<div style='text-align: center;'><img src='https://arquivo.pt/img/arquivo-logo-white.svg'></div>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>in Numbers</h1>", unsafe_allow_html=True)

config = {'displayModeBar': False}

#########################################################################################################

"""
# 1) Data from Arquivo.pt Collections

The data comes from manual entries made by our engineer responsible for the collections. You can see more information in [Collections](https://arquivo.pt/collections).
"""

tab1, tab2, tab3, tab4 = st.tabs(["Collections", "Files Collected", "(TB) Stored", "URL Collected"])

#tab collections
with tab1:
    #Prepare your data
    categories = df['Year'][1:]
    heights = df['Total Collections'][1:].astype(int)

    #Create a bar chart object
    bar_chart = go.Bar(x=categories, y=heights)

    #Create a figure and add the bar chart object
    fig1 = go.Figure()
    fig1.add_trace(bar_chart)
    fig1.update_xaxes(tickvals=categories)


    #Customize the chart (optional)
    fig1.update_layout(
        title='Total Number Collections per Year',
        xaxis_title='Year',
        yaxis_title='Number Collections'
        )

    #Cumulative
    df['Cumulative'] = df['Total Collections'][1:].astype(int).cumsum()

    #Create a bar chart object
    bar_chart = go.Bar(x=categories, y=df['Cumulative'][1:])

    #Create a figure and add the bar chart object
    fig2 = go.Figure()
    fig2.add_trace(bar_chart)
    fig2.update_xaxes(tickvals=categories)


    #Customize the chart (optional)
    fig2.update_layout(
        title='Total Number Collections per Year Cumulative',
        xaxis_title='Year',
        yaxis_title='Number Collections'
    )
    st.expander('expander', expanded=False)
    st.plotly_chart(fig1, config=config, use_container_width=True)
    st.plotly_chart(fig2, config=config, use_container_width=True)

##############################################################################################################

#tab Files Collected
with tab2:

    #Prepare your data
    categories = df['Year'][1:]
    heights = df['Total Files'][1:]
    print(heights)

    #Create a bar chart object
    bar_chart = go.Bar(x=categories, y=heights)

    #Create a figure and add the bar chart object
    fig3 = go.Figure()
    fig3.add_trace(bar_chart)
    fig3.update_xaxes(tickvals=categories)

    #Customize the chart (optional)
    fig3.update_layout(
        title='Total Files Collected per Year',
        xaxis_title='Year',
        yaxis_title='Total Files'
        )

    #Cumulative
    df['Cumulative'] = df['Total Files'][1:].cumsum()
    print(df['Cumulative'] )

    #Create a bar chart object
    bar_chart = go.Bar(x=categories, y=df['Cumulative'][1:])

    #Create a figure and add the bar chart object
    fig4 = go.Figure()
    fig4.add_trace(bar_chart)
    fig4.update_xaxes(tickvals=categories)


    #Customize the chart (optional)
    fig4.update_layout(
        title='Total Files per Year Cumulative',
        xaxis_title='Year',
        yaxis_title='Total Files)'
    )

    #Print the Chart
    st.expander('expander', expanded=False)
    st.plotly_chart(fig3, config=config, use_container_width=True)
    st.plotly_chart(fig4, config=config, use_container_width=True)

##############################################################################################################

#tab (TB) Stored
with tab3:

    #Prepare your data
    categories = df['Year'][1:]
    heights = df['Total Stored (TB)'][1:].astype(int)

    #Create a bar chart object
    bar_chart = go.Bar(x=categories, y=heights)

    #Create a figure and add the bar chart object
    fig5 = go.Figure()
    fig5.add_trace(bar_chart)
    fig5.update_xaxes(tickvals=categories)


    #Customize the chart (optional)
    fig5.update_layout(
        title='Total Stored (TB) per Year',
        xaxis_title='Year',
        yaxis_title='Total Stored (TB)'
        )

    #Cumulative
    df['Cumulative'] = df['Total Stored (TB)'][1:].astype(int).cumsum()

    #Create a bar chart object
    bar_chart = go.Bar(x=categories, y=df['Cumulative'][1:])

    #Create a figure and add the bar chart object
    fig6 = go.Figure()
    fig6.add_trace(bar_chart)
    fig6.update_xaxes(tickvals=categories)


    #Customize the chart (optional)
    fig6.update_layout(
        title='Total Stored (TB) per Year Cumulative',
        xaxis_title='Year',
        yaxis_title='Total Stored (TB)'
    )

    #Print the Chart
    st.expander('expander', expanded=False)
    st.plotly_chart(fig5, config=config, use_container_width=True)
    st.plotly_chart(fig6, config=config, use_container_width=True)

#############################################################################################

#tab URL Collected
with tab4:

    #Prepare your data
    categories = df['Year'][1:]
    heights = df['Total Seeds'][1:].astype(int)

    #Create a bar chart object
    bar_chart = go.Bar(x=categories, y=heights)

    #Create a figure and add the bar chart object
    fig7 = go.Figure()
    fig7.add_trace(bar_chart)
    fig7.update_xaxes(tickvals=categories)


    #Customize the chart (optional)
    fig7.update_layout(
        title='Total URLs Collected per Year',
        xaxis_title='Year',
        yaxis_title='Total URLs'
        )

    #Cumulative
    df['Cumulative'] = df['Total Seeds'][1:].astype(int).cumsum()

    #Create a bar chart object
    bar_chart = go.Bar(x=categories, y=df['Cumulative'][1:])

    #Create a figure and add the bar chart object
    fig8 = go.Figure()
    fig8.add_trace(bar_chart)
    fig8.update_xaxes(tickvals=categories)


    #Customize the chart (optional)
    fig8.update_layout(
        title='Total URLs Collected per Year Cumulative',
        xaxis_title='Year',
        yaxis_title='Total URLs'
    )

    st.expander('expander', expanded=False)
    st.plotly_chart(fig7, config=config, use_container_width=True)
    st.plotly_chart(fig8, config=config, use_container_width=True)


#########################################################################################################

"""
# 2) Data from AWStats Software

The data comes from the Arquivo.pt Logs and is processed by AWStats Software. Information can only be accessed internally.
"""

tab1, tab2, tab3, tab4 = st.tabs(["Bandwidth (TB)", "Number of Visits", "Number of Pages Visited", "Number of Unique Users"])

#tab Bandwidth (TB)
with tab1:

    filtered_df = df[df['Bandwidth (TB)'] != 0]

    #Prepare your data
    categories = filtered_df['Year'][1:]
    heights = filtered_df['Bandwidth (TB)'][1:].astype(int)

    #Create a bar chart object
    bar_chart = go.Bar(x=categories, y=heights)

    #Create a figure and add the bar chart object
    fig9 = go.Figure()
    fig9.add_trace(bar_chart)
    fig9.update_xaxes(tickvals=categories)

    #Customize the chart (optional)
    fig1.update_layout(
        title='Bandwidth (TB) from Arquivo.pt per Year',
        xaxis_title='Year',
        yaxis_title='Bandwidth (TB)'
        )

    #Cumulative
    filtered_df['Cumulative'] = filtered_df['Bandwidth (TB)'][1:].astype(int).cumsum()

    #Create a bar chart object
    bar_chart = go.Bar(x=categories, y=filtered_df['Cumulative'][1:])

    #Create a figure and add the bar chart object
    fig10 = go.Figure()
    fig10.add_trace(bar_chart)
    fig10.update_xaxes(tickvals=categories)

    #Customize the chart (optional)
    fig10.update_layout(
        title='Bandwidth (TB) per Year Cumulative',
        xaxis_title='Year',
        yaxis_title='Bandwidth (TB)'
    )

    st.expander('expander', expanded=False)
    st.plotly_chart(fig9, config=config, use_container_width=True)
    st.plotly_chart(fig10, config=config, use_container_width=True)


#########################################################################################################

#tab Number of Visits
with tab2:

    filtered_df = df[df['Number of visits'] != 0]


    #Prepare your data
    categories = filtered_df['Year'][1:]
    heights = filtered_df['Number of visits'][1:].astype(int)

    #Create a bar chart object
    bar_chart = go.Bar(x=categories, y=heights)

    #Create a figure and add the bar chart object
    fig11 = go.Figure()
    fig11.add_trace(bar_chart)
    fig11.update_xaxes(tickvals=categories)

    #Customize the chart (optional)
    fig11.update_layout(
        title='Number of Visits in Arquivo.pt per Year',
        xaxis_title='Year',
        yaxis_title='Number of Visits'
        )

    #Cumulative
    filtered_df['Cumulative'] = filtered_df['Number of visits'][1:].astype(int).cumsum()

    #Create a bar chart object
    bar_chart = go.Bar(x=categories, y=filtered_df['Cumulative'][1:])

    #Create a figure and add the bar chart object
    fig12 = go.Figure()
    fig12.add_trace(bar_chart)
    fig12.update_xaxes(tickvals=categories)

    #Customize the chart (optional)
    fig12.update_layout(
        title='Number of Visits in Arquivo.pt per Year Cumulative',
        xaxis_title='Year',
        yaxis_title='Number of Visits'
    )

    st.expander('expander', expanded=False)
    st.plotly_chart(fig11, config=config, use_container_width=True)
    st.plotly_chart(fig12, config=config, use_container_width=True)

#########################################################################################################

#tab Number of Pages Visited
with tab3:
    filtered_df = df[df['Pages'] != 0]

    #Prepare your data
    categories = filtered_df['Year'][1:]
    heights = filtered_df['Pages'][1:].astype(int)

    #Create a bar chart object
    bar_chart = go.Bar(x=categories, y=heights)

    #Create a figure and add the bar chart object
    fig13 = go.Figure()
    fig13.add_trace(bar_chart)
    fig13.update_xaxes(tickvals=categories)


    #Customize the chart (optional)
    fig13.update_layout(
        title='Number of Pages Visited',
        xaxis_title='Year',
        yaxis_title='Number of Pages'
        )

    #Cumulative
    filtered_df['Cumulative'] = filtered_df['Pages'][1:].astype(int).cumsum()

    #Create a bar chart object
    bar_chart = go.Bar(x=categories, y=filtered_df['Cumulative'][1:])

    #Create a figure and add the bar chart object
    fig14 = go.Figure()
    fig14.add_trace(bar_chart)
    fig14.update_xaxes(tickvals=categories)


    #Customize the chart (optional)
    fig14.update_layout(
        title='Number of Pages per Year Cumulative',
        xaxis_title='Year',
        yaxis_title='Number of Pages'
    )

    st.expander('expander', expanded=False)
    st.plotly_chart(fig13, config=config, use_container_width=True)
    st.plotly_chart(fig14, config=config, use_container_width=True)

##############################################################################################################

#tab Number of Unique Users
with tab4:

    filtered_df = df[df['Unique Users'] != 0]

    #Prepare your data
    categories = filtered_df['Year'][1:]
    heights = filtered_df['Unique Users'][1:].astype(int)

    #Create a bar chart object
    bar_chart = go.Bar(x=categories, y=heights)

    #Create a figure and add the bar chart object
    fig21 = go.Figure()
    fig21.add_trace(bar_chart)
    fig21.update_xaxes(tickvals=categories)

    #Customize the chart (optional)
    fig21.update_layout(
        title='Unique Users from Arquivo.pt per Year',
        xaxis_title='Year',
        yaxis_title='Unique Users'
        )

    #Cumulative
    filtered_df['Cumulative'] = filtered_df['Unique Users'][1:].astype(int).cumsum()

    #Create a bar chart object
    bar_chart = go.Bar(x=categories, y=filtered_df['Cumulative'][1:])

    #Create a figure and add the bar chart object
    fig22 = go.Figure()
    fig22.add_trace(bar_chart)
    fig22.update_xaxes(tickvals=categories)

    #Customize the chart (optional)
    fig22.update_layout(
        title='Unique Users per Year Cumulative',
        xaxis_title='Year',
        yaxis_title='Unique Users'
    )

    st.expander('expander', expanded=False)
    st.plotly_chart(fig21, config=config, use_container_width=True)
    st.plotly_chart(fig22, config=config, use_container_width=True)

#########################################################################################################

"""
# 3) Memorial Data
The data comes from manual entries made by our digital curator who is responsible for curating the Memorial websites.
"""

filtered_df = df[df['Memorial'] != 0]

#Prepare your data
categories = filtered_df['Year']
heights = filtered_df['Memorial'].astype(int)

#Create a bar chart object
bar_chart = go.Bar(x=categories, y=heights)

#Create a figure and add the bar chart object
fig21 = go.Figure()
fig21.add_trace(bar_chart)
fig21.update_xaxes(tickvals=categories)

#Customize the chart (optional)
fig21.update_layout(
    title='Number of Websites in the Arquivo.pt Memorial per Year',
    xaxis_title='Year',
    yaxis_title='Number of Websites'
    )

#Cumulative
filtered_df['Cumulative'] = filtered_df['Memorial'].astype(int).cumsum()

#Create a bar chart object
bar_chart = go.Bar(x=categories, y=filtered_df['Cumulative'])

#Create a figure and add the bar chart object
fig22 = go.Figure()
fig22.add_trace(bar_chart)
fig22.update_xaxes(tickvals=categories)


#Customize the chart (optional)
fig22.update_layout(
    title='Number of Websites in the Arquivo.pt Memorial per Year Cumulative',
    xaxis_title='Year',
    yaxis_title='Number of Websites'
)

st.expander('expander', expanded=False)
st.plotly_chart(fig21, config=config, use_container_width=True)
st.plotly_chart(fig22, config=config, use_container_width=True)


##############################################################################################################

gc = gspread.service_account(args['pathjson'])
sh =  gc.open_by_key(args['key2'])
worksheet = sh.worksheet(args['worksheet2'])

#Transform worksheet to pandas dataframe
df = get_as_dataframe(worksheet, index='false', evaluate_formulas=True)

"""
# 4) Metrics of APIs and Services Apache Log Data 
The data comes from a script that analyzes Apache Logs data focus only in data from APIs and other services. The only filter used was to discard internal requests.
"""

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Number of Requests /textsearch", "Number of Requests /imagesearch", "Number of Requests /wayback/cdx", "Number of Requests /wayback/timemap", "Number of Requests /services/savepagenow"])

#tab Number of Requests /textsearch
with tab1:


    filtered_df = df[df['Total Filtered Requests /textsearch'] != 0]


    #Prepare your data
    categories = filtered_df['Year']
    heights = filtered_df['Total Filtered Requests /textsearch'].astype(int)

    #Create a bar chart object
    bar_chart = go.Bar(x=categories, y=heights)

    #Create a figure and add the bar chart object
    fig15 = go.Figure()
    fig15.add_trace(bar_chart)
    fig15.update_xaxes(tickvals=categories)

    #Customize the chart (optional)
    fig15.update_layout(
        title='Total Requests /textsearch per Year',
        xaxis_title='Year',
        yaxis_title='Total Requests /textsearch'
        )

    filtered_df = df[df['Total Distinct IP Addresses /textsearch'] != 0]

    categories = filtered_df['Year']
    heights = filtered_df['Total Distinct IP Addresses /textsearch'].astype(int)

    #Create a bar chart object
    bar_chart = go.Bar(x=categories, y=heights)

    #Create a figure and add the bar chart object
    fig16 = go.Figure()
    fig16.add_trace(bar_chart)
    fig16.update_xaxes(tickvals=categories)


    #Customize the chart (optional)
    fig16.update_layout(
        title='Total Distinct IP Addresses /textsearch per Year Cumulative',
        xaxis_title='Year',
        yaxis_title='Total Distinct IP Addresses /textsearch'
    )

    st.expander('expander', expanded=False)
    st.plotly_chart(fig15, config=config, use_container_width=True)
    st.plotly_chart(fig16, config=config, use_container_width=True)

##############################################################################################################

#tab Number of Requests /imagesearch
with tab2:

    filtered_df = df[df['Total Filtered Requests /imagesearch'] != 0]

    #Prepare your data
    categories = filtered_df['Year']
    heights = filtered_df['Total Filtered Requests /imagesearch'].astype(int)

    #Create a bar chart object
    bar_chart = go.Bar(x=categories, y=heights)

    #Create a figure and add the bar chart object
    fig17 = go.Figure()
    fig17.add_trace(bar_chart)
    fig17.update_xaxes(tickvals=categories)

    #Customize the chart (optional)
    fig17.update_layout(
        title='Total Requests /imagesearch per Year',
        xaxis_title='Year',
        yaxis_title='Total Requests /imagesearch'
        )

    filtered_df = df[df['Total Distinct IP Addresses /imagesearch'] != 0]

    categories = filtered_df['Year']
    heights = filtered_df['Total Distinct IP Addresses /imagesearch'].astype(int)

    #Create a bar chart object
    bar_chart = go.Bar(x=categories, y=heights)

    #Create a figure and add the bar chart object
    fig18 = go.Figure()
    fig18.add_trace(bar_chart)
    fig18.update_xaxes(tickvals=categories)

    #Customize the chart (optional)
    fig18.update_layout(
        title='Total Distinct IP Addresses /imagesearch per Year Cumulative',
        xaxis_title='Year',
        yaxis_title='Total Distinct IP Addresses /imagesearch'
    )

    st.expander('expander', expanded=False)
    st.plotly_chart(fig17, config=config, use_container_width=True)
    st.plotly_chart(fig18, config=config, use_container_width=True)

##############################################################################################################

#tab Number of Requests /wayback/cdx
with tab3:

    filtered_df = df[df['Total Filtered Requests /wayback/cdx'] != 0]

    #Prepare your data
    categories = filtered_df['Year']
    heights = filtered_df['Total Filtered Requests /wayback/cdx'].astype(int)

    #Create a bar chart object
    bar_chart = go.Bar(x=categories, y=heights)

    #Create a figure and add the bar chart object
    fig17 = go.Figure()
    fig17.add_trace(bar_chart)
    fig17.update_xaxes(tickvals=categories)

    #Customize the chart (optional)
    fig17.update_layout(
        title='Total Requests /wayback/cdx per Year',
        xaxis_title='Year',
        yaxis_title='Total Requests /wayback/cdx'
        )

    filtered_df = df[df['Total Distinct IP Addresses /wayback/cdx'] != 0]

    categories = filtered_df['Year']
    heights = filtered_df['Total Distinct IP Addresses /wayback/cdx'].astype(int)

    #Create a bar chart object
    bar_chart = go.Bar(x=categories, y=heights)

    #Create a figure and add the bar chart object
    fig18 = go.Figure()
    fig18.add_trace(bar_chart)
    fig18.update_xaxes(tickvals=categories)

    #Customize the chart (optional)
    fig18.update_layout(
        title='Total Distinct IP Addresses /wayback/cdx per Year Cumulative',
        xaxis_title='Year',
        yaxis_title='Total Distinct IP Addresses /wayback/cdx'
    )

    st.expander('expander', expanded=False)
    st.plotly_chart(fig17, config=config, use_container_width=True)
    st.plotly_chart(fig18, config=config, use_container_width=True)

##############################################################################################################

#tab Number of Requests /wayback/timemap
with tab4:

    filtered_df = df[df['Total Filtered Requests /wayback/timemap'] != 0]

    #Prepare your data
    categories = filtered_df['Year']
    heights = filtered_df['Total Filtered Requests /wayback/timemap'].astype(int)

    #Create a bar chart object
    bar_chart = go.Bar(x=categories, y=heights)

    #Create a figure and add the bar chart object
    fig21 = go.Figure()
    fig21.add_trace(bar_chart)
    fig21.update_xaxes(tickvals=categories)

    #Customize the chart (optional)
    fig21.update_layout(
        title='Total Requests /wayback/timemap per Year',
        xaxis_title='Year',
        yaxis_title='Total Requests /wayback/timemap'
        )

    filtered_df = df[df['Total Distinct IP Addresses /wayback/timemap'] != 0]

    categories = filtered_df['Year']
    heights = filtered_df['Total Distinct IP Addresses /wayback/timemap'].astype(int)

    #Create a bar chart object
    bar_chart = go.Bar(x=categories, y=heights)

    #Create a figure and add the bar chart object
    fig22 = go.Figure()
    fig22.add_trace(bar_chart)
    fig22.update_xaxes(tickvals=categories)

    #Customize the chart (optional)
    fig22.update_layout(
        title='Total Distinct IP Addresses /wayback/timemap per Year Cumulative',
        xaxis_title='Year',
        yaxis_title='Total Distinct IP Addresses /wayback/timemap'
    )

    st.expander('expander', expanded=False)
    st.plotly_chart(fig21, config=config, use_container_width=True)
    st.plotly_chart(fig22, config=config, use_container_width=True)

##############################################################################################################

#tab Number of Requests /services/savepagenow
with tab5:

    filtered_df = df[df['Total Filtered Requests /services/savepagenow'] != 0]

    #Prepare your data
    categories = filtered_df['Year']
    heights = filtered_df['Total Filtered Requests /services/savepagenow'].astype(int)

    #Create a bar chart object
    bar_chart = go.Bar(x=categories, y=heights)

    #Create a figure and add the bar chart object
    fig23 = go.Figure()
    fig23.add_trace(bar_chart)
    fig23.update_xaxes(tickvals=categories)

    #Customize the chart (optional)
    fig23.update_layout(
        title='Total Requests /services/savepagenow per Year',
        xaxis_title='Year',
        yaxis_title='Total Requests /services/savepagenow'
        )

    filtered_df = df[df['Total Distinct IP Addresses /services/savepagenow'] != 0]

    categories = filtered_df['Year']
    heights = filtered_df['Total Distinct IP Addresses /services/savepagenow'].astype(int)

    #Create a bar chart object
    bar_chart = go.Bar(x=categories, y=heights)

    #Create a figure and add the bar chart object
    fig24 = go.Figure()
    fig24.add_trace(bar_chart)
    fig24.update_xaxes(tickvals=categories)

    #Customize the chart (optional)
    fig24.update_layout(
        title='Total Distinct IP Addresses /services/savepagenow per Year Cumulative',
        xaxis_title='Year',
        yaxis_title='Total Distinct IP Addresses /services/savepagenow'
    )

    st.expander('expander', expanded=False)
    st.plotly_chart(fig23, config=config, use_container_width=True)
    st.plotly_chart(fig24, config=config, use_container_width=True)

##############################################################################################################

"""
# 5) Top Domains Available in Arquivo.pt
The data comes from a script that processes the CDXJs indexes from Arquivo.pt.
"""

#Commandline to get the information
#cat *.cdxj | sort | cut -d ')' -f 1 | uniq -c > out_domain.txt

#Data
cities = ['fortunecity.com', 'dre.pt', 'members.fortunecity.com', 'yt3.ggpht.com', 'geocities.com', 'youtube.com', 'publico.pt', 'tek.sapo.pt', 'noticiasdacovilha.pt', 'regiaodeagueda.com']
population = [43230045, 43640068, 26301933, 21862962, 16983647, 14926793, 13163730, 12373934, 11376784, 10944150]

#Sort the cities based on population in descending order
sorted_data = sorted(zip(population, cities))
population, cities = zip(*sorted_data)

#Create a horizontal bar chart using Plotly
fig19 = go.Figure(data=go.Bar(y=cities, x=population, orientation='h'))

#Customize the chart layout
fig19.update_layout(
    title='Top 10 Domains in Arquivo.pt',
    xaxis_title='Number URLs',
    yaxis_title='Domains'
)

#Data
cities = ['dre.pt', 'publico.pt', 'tek.sapo.pt', 'noticiasdacovilha.pt', 'destak.pt', 'sabado.pt', 'iol.tvi24.pt', 'jornaldofundao.pt', 'jornaldoalgarve.pt', 'tsf.pt']
population = [43640068, 13163730, 12373934, 11376784, 9858192, 9771033, 9722996, 9510040, 9452618, 9339705]

#Sort the cities based on population in descending order
sorted_data = sorted(zip(population, cities))
population, cities = zip(*sorted_data)

#Create a horizontal bar chart using Plotly
fig20 = go.Figure(data=go.Bar(y=cities, x=population, orientation='h'))

#Customize the chart layout
fig20.update_layout(
    title='Top 10 .PT Domains in Arquivo.pt',
    xaxis_title='Number URLs',
    yaxis_title='.PT Domains'
)

#Print the Chart
st.expander('expander', expanded=False)
st.plotly_chart(fig19, config=config, use_container_width=True)
st.plotly_chart(fig20, config=config, use_container_width=True)

