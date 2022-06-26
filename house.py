import streamlit as st
from streamlit_folium import folium_static

import folium
from folium.plugins import MarkerCluster

import pandas as pd
import geopandas
import numpy as np
from datetime import datetime

import plotly.express as px

st.set_page_config( layout='wide')

path = './datasets/kc_house_data.csv'
data = pd.read_csv(path)

url_geofile = 'https://opendata.arcgis.com/datasets/83fc2e72903343aabff6de8cb445b81c_2.geojson'
geofile = geopandas.read_file(url_geofile)

# --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# Extra features on dataset:
# Adding price per squarefoot
data['price_sqft'] = data['price'] / data['sqft_lot']



# # --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# # Data Overview

# 1.1 SIDEBAR - Data Overview filters
f_attributes = st.sidebar.multiselect('Enter columns', data.columns) # criar campo pra especificar filtro
f_zipcode = st.sidebar.multiselect('Ente ZipCode', data['zipcode'].unique() )

# 1.2 MAIN CONTENT - 1st Section Data Overview
st.title('Data Overview')

if (f_zipcode != [] ) & ( f_attributes != [] ):
    data = data.loc[data['zipcode'].isin(f_zipcode), f_attributes]
elif (f_zipcode != [] ) & (f_attributes == []):
    data = data.loc[data['zipcode'].isin(f_zipcode), :]
elif (f_zipcode == [] ) & (f_attributes != []):
    data = data.loc[:, f_attributes]
else:
    data = data.copy()
#
# st.dataframe(data.head())
#
# # 2 MAIN CONTENT - 2nd section, build average/count table
# df1 = data[['id', 'zipcode']].groupby('zipcode').count().reset_index()
# df2 = data[['price', 'zipcode']].groupby('zipcode').mean().reset_index()
# df3 = data[['sqft_living', 'zipcode']].groupby('zipcode').mean().reset_index()
# df4 = data[['price_sqft', 'zipcode']].groupby('zipcode').mean().reset_index()
# m1 = pd.merge(df1,df2, on='zipcode', how='inner')
# m2 = pd.merge(m1,df3, on='zipcode', how='inner')
# df = pd.merge(m2,df4, on='zipcode', how='inner')
#
# df.columns = ['Zipcode','Total Houses', 'Price','Square feet -living',
#               'Price/sqft']
#
# c1, c2 = st.columns(( 1,1 ))  # 2 columns
# c1.header('Average Values - S')  # 1st column
# c1.dataframe(df, height = 600)  # 1st column
#
# # 3 MAIN CONTENT - 3rd section, descriptive stats
# num_attributes = data.select_dtypes(include=['int64', 'float64'])
# mean = pd.DataFrame(num_attributes.apply( np.mean ))
# median = pd.DataFrame(num_attributes.apply( np.median ))
# std = pd.DataFrame(num_attributes.apply( np.std ))
#
# max_ = pd.DataFrame( num_attributes.apply ( np.max ))
# min_ = pd.DataFrame( num_attributes.apply ( np.min ))
#
# df1 = pd.concat([max_,min_, mean, median, std], axis = 1).reset_index()
# df1.columns = ['Attributes', 'Max', 'Min', 'Mean', 'Median', 'Std']
#
# c2.header('Descriptive Statistics')
# c2.dataframe( df1, height = 800)
#
##################

# with st.expander("See explanation"):

st.markdown('Insights on real estate for purchase and resaleInsights on real estate for purchase and resale')

st.write("""
     The chart above shows some numbers I picked for you.
     I rolled actual dice for these, so they're *guaranteed* to
     be random.
 """)

# 4 MAIN CONTENT - 4th section, portfolio density
st.title('Region Overview')

c1, c2 = st.columns((1,1))  # Columns

# 4 - 4th section, column 1
c1.header('Portfolio Density')

df = data.sample(100)

density_map = folium.Map(location = [data['lat'].mean(),
                                     data['long'].mean()],
                         default_zoom_start=15)

marker_cluster = MarkerCluster().add_to(density_map)  # start class for pinmarks
for name, row in data.iterrows():
    folium.Marker( [row['lat'], row['long'] ],\
                   popup='Sold USD{0} on: {1}. Features: {2} sqft, {3} bedrooms, {4} bathrooms, year built: {5}'.format( row['price'],\
                                     row['date'],
                                     row['sqft_living'],
                                     row['bedrooms'],
                                     row['bathrooms'],
                                     row['yr_built'] ) ).add_to( marker_cluster )

with c1:  # with - streamlit requirement rule
    folium_static(density_map) #

# 5 - 5th section, column 2
c2.header('Price Density')

df = data[['price','zipcode']].groupby('zipcode').mean().reset_index()
df.columns = ['ZIP', 'PRICE']
# df = df.sample(11)  # limited for faster testing

geofile = geofile[geofile['ZIP'].isin( df['ZIP'].tolist() )] # filtering dataset with info in sample list

# folium object on screen:
region_price_map = folium.Map(location = [data['lat'].mean(),\
                                     data['long'].mean()],\
                         default_zoom_start=15)

# folium data:
region_price_map.choropleth(data = df, geo_data = geofile,
                            columns=['ZIP', 'PRICE'],
                            key_on='feature.properties.ZIP',
                            fill_color='YlOrRd',
                            fill_opacity=0.7,
                            line_opacity=0.2,
                            legend_name='AVG PRICE')

with c2:  # plt data
    folium_static(region_price_map )

# 6 6th Section

#  6.1 - Sidebar

st.sidebar.title('Commercial Options')  # cria subtitulo na sessao do sidebar.
st.title('Commercial  Attributes')

data['date'] = pd.to_datetime( data['date']).dt.strftime('%Y-%m-%d' )

min_year_built = int( data['yr_built'].min() )
max_year_built = int( data['yr_built'].max() )

st.sidebar.subheader('Select Max Year Built')
f_year_built = st.sidebar.slider('Yr built', min_year_built,max_year_built,min_year_built)
data = data.loc[data['yr_built'] < f_year_built]

# # 6.2 - Main Content
# st.header('Average Price vs Year Built')
#
# df = data.loc[data['yr_built'] < f_year_built]
# df = df[['yr_built', 'price']].groupby('yr_built').mean().reset_index()
#
# fig = px.line(df, x='yr_built', y='price')
# st.plotly_chart(fig, use_container_width=True)

# # 7 AVG price per day
# # 7.1  Sidebar
# st.sidebar.header("Max. date for Average Day Price")
#
# # 7.2 - MAIN SCREEN
# st.header('Avg Price per day')
#
# min_date = datetime.strptime( data['date'].min(), '%Y-%m-%d' )
# max_date = datetime.strptime( data['date'].max(), '%Y-%m-%d' )
# f_date = st.sidebar.slider('Date', min_date, max_date, min_date)
#
# data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d')
# df = data.loc[data['date'] < f_date]
# df = df[['date', 'price']].groupby('date').mean().reset_index()
#
# fig = px.line(df, x='date', y='price')
# st.plotly_chart(fig, use_container_width=True)
#
# #  Section - By Attributes
# # 8 Sidebars Bedroom
# st.sidebar.title('Attributes Options')
#
# f_bedrooms = st.sidebar.selectbox('Max # bedrooms:',
#                                   sorted( set(data['bedrooms'].unique())))
#
# # 9 Sidebar Bathroom
# f_bathrooms = st.sidebar.selectbox('Max # bathrooms:',
#                                    sorted( set(data['bathrooms'].unique())))
#
# #  8 and 9  Main window Bedroom and bathroom
# c1, c2 = st.columns( 2 )
#
#
# c1.header('Bedrooms')
# df = data[data['bedrooms'] < f_bedrooms]
# fig = px.histogram(df, x='bedrooms', nbins =19)
# c1.plotly_chart(fig, use_container_width=True)
#
# c2.header('Bathrooms')
# df = data[data['bathrooms'] < f_bathrooms]
# fig = px.histogram(df, x = 'bathrooms', nbins =19)
# c2.plotly_chart(fig, use_container_width=True)
#
# # Houses floor and Waterview
# # 10 - Sidebar Max number of floors
# f_floors = st.sidebar.selectbox('Max number of floor',
#                                    sorted( set(data['floors'].unique())))
#
# # 11 - Sidebar filter water view
# f_waterview = st.sidebar.checkbox( 'Only Houses with Water View')
#
#
# # 10 and 11 Main window:
# c1,c2 = st.columns(2)
#
# c1.title('Houses per floor')
# df = data[data['floors'] < f_floors]
# fig = px.histogram(df, x = 'floors', nbins =19)
# c1.plotly_chart(fig, use_container_width=True)
#
#
# c2.title('Waterview')
# if f_waterview:
#     df = data[data['waterfront'] == 1]
# else:
#     df= data.copy()
#
#
# fig = px.histogram(df, x='waterfront', nbins=10)
# c2.plotly_chart(fig, use_container_width=True)
#
#
#

