import streamlit as st
from streamlit_folium import folium_static

import folium
from folium.plugins import MarkerCluster

import pandas as pd
import geopandas
import numpy as np
from datetime import datetime
import plotly.express as px



def features(data):
    # Extra features on dataset:
    data['aux_sqft_living_price'] = data['price'] / data['sqft_living']
    zipcode_avg_price = data[['zipcode','price','sqft_living','aux_sqft_living_price','condition','grade','yr_built']].groupby('zipcode').median().reset_index()
    zipcode_avg_price.rename(columns = {'aux_sqft_living_price': 'median_aux_sqft_living_price', 'price':'median_price'}, inplace =True)
    # Code zipcode mean price + misc, per region in the df:
    new_df = zipcode_avg_price[['zipcode','median_price','median_aux_sqft_living_price']]
    new_df = new_df.rename(columns = {'mean_price':'mean_region_price', 'median_aux_sqft_living_price':'median_region_price_sqft'})
    data = data.merge(new_df, how = 'inner', left_on='zipcode', right_on='zipcode' )
    data['difference_median_of_region'] = (((data['aux_sqft_living_price'] / data['median_region_price_sqft'])-1)*100)
    return data


def main(data, geofile):

    # Sidebars
    f_zipcode = st.sidebar.multiselect('Enter ZipCode(s)', data['zipcode'].unique() )
    if (f_zipcode != [] ):
        data = data.loc[data['zipcode'].isin(f_zipcode)]
    else:
        data = data.copy()

    st.sidebar.title('Map Options')  # cria subtitulo na sessao do sidebar.

    data['date'] = pd.to_datetime( data['date']).dt.strftime('%Y-%m-%d' )

    min_year_built = int( data['yr_built'].min() )
    max_year_built = int( data['yr_built'].max() )
    st.sidebar.subheader('Select Min Year Built')
    f_min_year_built = st.sidebar.slider('Yr built', min_year_built,max_year_built,min_year_built)
    st.sidebar.subheader('Select Max Year Built')
    f_max_year_built = st.sidebar.slider('Yr built', min_year_built,max_year_built,max_year_built)
    data = data.loc[(data['yr_built'] <= f_max_year_built) & (data['yr_built'] >= f_min_year_built)]

    min_price = int(data['price'].min())
    max_price = int(data['price'].max())
    st.sidebar.subheader('Minimun property price')
    min_price = st.sidebar.slider('Min Price', min_price,max_price,min_price, 1000)
    st.sidebar.subheader('Maximum property price')
    max_price = st.sidebar.slider('Max Price', min_price,max_price,max_price, 1000)
    data = data.loc[(data['price'] <= max_price) & (data['price'] >= min_price)]

    min_cond = int(data['condition'].min())
    max_cond = int(data['condition'].max())
    st.sidebar.subheader('Minimun Condition')
    min_cond = st.sidebar.slider('Min Condition', min_cond,max_cond,min_cond)
    st.sidebar.subheader('Maximum Condition')
    max_cond = st.sidebar.slider('Min Condition', min_cond,max_cond,max_cond)
    data = data.loc[(data['condition'] <= max_cond) & (data['condition'] >= min_cond)]

    st.sidebar.subheader('Difference lower or higher than the mean for region')
    agree = st.sidebar.checkbox('Activate this for median % filter on sqft prices')
    mean_comp = st.sidebar.slider('Percentage Difference(don´t forget to check the box above):', -40, 40, 0, step = 5)
    if agree:
        if mean_comp > 0:
            data = data.loc[data['difference_median_of_region'] >=  float(mean_comp)]
        elif mean_comp < 0:
            data = data.loc[data['difference_median_of_region'] <= float(mean_comp)]
        else:
            data = data.loc[data['difference_median_of_region'] == float(mean_comp)]

    st.markdown('# **Insights on real estate for purchase and resale - Interactive Map**, __by Fulvio__')

    st.markdown("""
    ***
    This project was carried out using data available on the
    [kaggle](https://www.kaggle.com/datasets/harlfoxem/housesalesprediction)
    website. The objective is to identify good deals on properties for
    purchase with subsequent profit.
    
    This is the interactive map for the project, it helps to find on map houses based custom criteria. 
    Just select the options from the left sidebar and have a go.
         
    Do not forget to check on the sidebar that filters properties under the specific percentage mean price difference for the region. 
    This will allow you to view the properties following the same criteria used in the project. Or even create your own.    
    It is possible to limit the number of regions you check by selecting specific zipcodes.
         
    You can also check the Jupyther notebook for the project [here](https://github.com/fusaa/house-dashboard/blob/main/0%20-%20king%20county.ipynb).
    ***
     """)

    c1, c2 = st.columns((1,1))  # Columns

    # 4 - 4th section, column 1
    c1.header('Portfolio Density')

    # df = data.sample(100)  # testing  sample

    density_map = folium.Map(location = [data['lat'].mean(),
                                         data['long'].mean()],
                             default_zoom_start=15)

    marker_cluster = MarkerCluster().add_to(density_map)  # start class for pinmarks
    #"{:,}".format(num)
    for name, row in data.iterrows():
        html = 'Sold USD {0}<br> Date: {1}, <br>{2} sqft,<br>{3} bedrooms,<br>{4} bathrooms,<br>{5} $/sqft region,<br>{6} $/sqft this property,<br>{7} year built,<br>{8} condition,<br>{9} Transaction ID.'.format(
            '{:,.2f}'.format(row['price']), \
            row['date'],
            row['sqft_living'],
            row['bedrooms'],
            row['bathrooms'],
            '{:.2f}'.format(row['median_region_price_sqft']),
            '{:.2f}'.format(row['aux_sqft_living_price']),
            row['yr_built'],
            row['condition'],
            row['id'])

        iframe = folium.IFrame(html, width=200, height=250)
        popup = folium.Popup(iframe, max_width=200)
        folium.Marker([row['lat'], row['long']], \
                      popup=popup).add_to(marker_cluster)

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

    ######################
    # TODO Readme file, write it to another file.
    readme = """
    ***
    ## Region Ranking
    In order to seek the best regions to invest it has been applied a ranking system. First the top 15 regions in terms of number of transactions were selected, followed the top 10 in price, and finally the next top 5 region in terms of condition for the properties. The condition has been considered in order to avoid potential issues for investors.
    
    The chosen region given the criteria was zipcode 98133 (Shoreline).
    
    ![image](https://user-images.githubusercontent.com/66756007/176123662-a818c606-a31c-4c23-8fa5-7ea7a0c5ceda.png)
    
    The region has had 494 properties transactioned during the period, has a median price per square foot of USD245,21. The median lot size is 7.305 sqft, and the mean condition 3,54. And important to mention the median price for the properties are USD375.000,00 which puts the property right in the price range of properties most transactioned.
    
    ## Potential Deals
    
    A potential strategy could be acquiring properties under the median price per square foot, and reselling them over that. Say an investor buys a house 20% under the median price, that house could be resold on the median with a 20% gain, or if the investor gets a better deal, 10% over, so that would make a profit of 30%. However it is always important to check on the peculiarities of each deal. There were 213 properties in the time period transactioned under 
    the 20% lower mark of the median price. If an investing party were to buy all of these properties the transaction ammount would be USD84.149.567,00. While the potential sell USD109.394.437,10 on a 30% higher price. That would make a possible profit of USD25.244.870,10. Of course we are considering the bulk of the area, not considering an aggresive buy would drive prices up. However a for a small investor that would be a possible strategy.
    
    ## Other Regions Top 5 Regions
    
    Even though we have chosen a single region, the other top 5 regions could yield great deals as well. Check the summary for the other 5 top regions:
    
    ![image](https://user-images.githubusercontent.com/66756007/176127715-cfaccd73-929c-46c4-9c8c-7beb25c7d4ab.png)
    
    
    
    """



    st.markdown(readme)




@st.cache(allow_output_mutation=True)  # decorador que carrega do cache o arquivo )
def load_data(path):
    data = pd.read_csv(path)
    return data


@st.cache(allow_output_mutation=True)  # definir quadrantes pra fzer densidade por preco
def load_geofile(url):
    geofile = geopandas.read_file(url)
    return geofile



if __name__ == '__main__':
    st.set_page_config(layout='wide')
    path = './datasets/kc_house_data.csv'
    # url_geofile = 'https://opendata.arcgis.com/datasets/83fc2e72903343aabff6de8cb445b81c_2.geojson'
    url_geofile = 'https://services2.arcgis.com/I7NQBinfvOmxQbXs/arcgis/rest/services/sps_geo_zone_ES_2021_2022/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson'
    data = load_data(path)
    geofile = load_geofile(url_geofile)

    data = features(data)
    main(data, geofile)