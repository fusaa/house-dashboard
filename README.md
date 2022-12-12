<div id="wrapper">

<div id="main">

<div class="inner">

[**House Sales in King County, USA** by Fulvio](index.html)

<div id="banner" class="section">

<div class="content">

# Insights on real estate for purchase and resale

This project was carried out using data available on the [kaggle](https://www.kaggle.com/datasets/harlfoxem/housesalesprediction) website. The objective is to identify good deals on properties for purchase with subsequent profit.

The dataset comprehends house sales prices for King County, Seattle, USA. It includes homes sold between May 2014 and May 2015.

### [Streamlit Dashboard](https://fu-seattle.streamlit.app/)
If you want to jump right to the Streamlit -  dashboard with suggestions for deals, please [please click here](https://fu-seattle.streamlit.app/).

### [Jupyter Notebook](https://github.com/fusaa/house-dashboard/blob/main/0%20-%20king%20county.ipynb)
You can also check the Jupyter notebook for the project [here](https://github.com/fusaa/house-dashboard/blob/main/0%20-%20king%20county.ipynb).

## 
The Insight Analysis was conducted in order to answer the question for potential investors about which houses should be bought and for what value they should be sold.

</div>

</div>

<div class="section">
It was done in Python using libraries like Pandas, Numpy, Streamlit, Folium, and Seaborn. Also, a dashboard was deployed originally using Heroku however the deployment was migrated to streamlit.io.

<div class="col-4 col-12-medium">



### The methodology

An EDA (exploratory data analysis) was done using the available database to seek insights and understand the impact of each variable on the region.

![image](./MindMap.png)
  
### Data

The data provided only one year of transactions, which limited the analysis. However, it was still possible to generate interesting insights.

One crucial aspect that investors tend to think about is the price per square foot. That feature has been engineered in the analysis.

Available data can be described according to the following table:


| Name         | Description                                    | Name           | Description                                                                              |
| ------------ | ---------------------------------------------- | -------------- | ---------------------------------------------------------------------------------------- |
| id           | Unique ID for each transaction.                | grade          | Score on building construction and design. Eg 7 is average level, the higher the better. |
| date         | Transaction Date.                              | sqft\_above    | House interior area above ground level.                                                  |
| price        | Transaction ammount.                           | yr\_build      | Year house was built.                                                                    |
| bedrooms     | Number of bedrooms.                            | yr\_renovated  | When house was renovated.                                                                |
| bathrooms    | Number of bathrooms. '.5' accounts for toilet. | zipcode        | Zipcode.                                                                                 |
| sqft\_living | Square footage living area.                    | lat            | Property latitude.                                                                       |
| sqft\_lot    | Lot size.                                      | lon            | Property lontitude.                                                                      |
| floors       | Number of pavements.                           | sqft\_living15 | Size in square foot of the nearest 15 neighbors.                                         |
| waterfront   | Means house has a view to waterfront.          | sqft\_lot15    | Size of the land of the nearest 15 neighbors.                                            |
| view         | Score 1-4 on how good view is.                 | bathrooms      | Number of bathrooms.                                                                     |
|              |                                                | condition      | An index from 1 to 5 on the condition of the apartment.                                  |





## Numerical and Categorical attributes Correlation
  
  
### During the data explorarion a few hypothesis were generated:
  1) The square foot of newer houses are more expensive.  
  Not true; they tend to be cheaper. The graph shows properties have gone through a decline in price in the 50s and have been like that from the 60s onwards.  
  ![image](https://user-images.githubusercontent.com/66756007/175946753-a4f0545f-7a9a-46cb-89a4-d7a9f2969971.png)

  2) Cheaper properties are easier to resell.  
  It is true the properties that sell the most are the ones between 300.000 and 400.000 dollars. Moreover, the properties between 200.000 and 600.000 account for over 67% of the transactions.  
  ![image](https://user-images.githubusercontent.com/66756007/175947287-c685603f-9370-4bd4-9e49-bdeab8e9dce2.png)

  3) The larger the property(living area) the cheaper the square foot:  
  That would be true in relative terms. If considered the properties only with a size of up to 2.500 sqft, beyond that, values will get higher. So the statement must be rejected. 
  ![image](https://user-images.githubusercontent.com/66756007/175947619-57826309-f859-4910-9986-bfe74919dee0.png)

  4) The larger the property + lot size, the cheaper the square foot:
  To answer this, the dataset has been sliced in 20.000 sqft increments for the computed area. According to the graph and the presence of outliers, this hypothesis has become inconclusive. So can´t be validated using the whole dataset.
  
  ![image](https://user-images.githubusercontent.com/66756007/175947936-531fb2ae-6a6b-4201-9bde-be860731c314.png)

  5) During certain quarters of the year prices are higher.
  The dataset comprehends only one year, making it hard to conclude. However, the graph for the specific period the data is available shows no significant difference between quarters. 
   
  ![image](https://user-images.githubusercontent.com/66756007/175948131-e6225c6f-41f6-4935-a19c-cf176f448871.png)
  
  6) Properties renovated in the last 30 years will sell more expensive.
  As seen on the graph, 'recently' renovated properties will sell for more- a question to raise would be what kind of renovation a property must undergo to be considered renovated. Therefore this assumption can be accepted.  
  ![image](https://user-images.githubusercontent.com/66756007/175949030-bc3270ae-93ad-430b-997a-32affa301314.png)

  
  7) Regions where the renovation rate is higher tend to have a higher price.
  Calculating the median price for each specific zip code and comparing the renovation rate (which takes into account the percentage of properties transacted in the period that had been renovated), it is safe to assume that a neighbourhood with higher renovation rates will have higher prices. The correlation result of 0.66 clearly shows that. Hypothesis accepted.  
  ![image](https://user-images.githubusercontent.com/66756007/175949159-71990459-333e-47b9-94d7-5bcc6d2b59c6.png)
  
  
  
 ##  Multivariate analysis
  There are a few exciting correlations noticed. Prices strongly correlate to areas of the construction (sqft_living, sqft_above, sqft_basement), as well as to the construction area of the surrounding properties(sqf_living15), which makes sense.  
Waterfront properties tend to have a high view rating, as well as the number of bedrooms, bathrooms, floors, and grade all strongly relate to each other.

![image](https://user-images.githubusercontent.com/66756007/175943062-a7c91ae3-151b-45f9-8623-d756828d9d09.png)

## Region Ranking
To seek the best regions to invest, a ranking system has been applied. First, the top 15 areas in terms of transactions numbers were selected, followed by the top 10 in price, and finally, the following top 5 region in terms of condition for the properties. The condition has been considered in order to avoid potential issues for investors.

The chosen region given the criteria was zip code 98133 (Shoreline).
![image](https://user-images.githubusercontent.com/66756007/176123662-a818c606-a31c-4c23-8fa5-7ea7a0c5ceda.png)

TThe region has had 494 properties transacted during the period and has a median price per square foot of USD245,21. The median lot size is 7.305 sqft, and the mean condition is 3,54. And important to mention the median price for the properties is USD375.000,00, which puts the property right in the price range of properties most transacted.

## Potential Deals

A potential strategy could be acquiring properties under the median price per square foot and reselling them over that. Say an investor buys a house 20% under the median price, that house could be resold on the median with a 20% gain, or if the investor gets a better deal, 10% over, so that would make a profit of 30%. However, it is always essential to check on the peculiarities of each agreement. There were 213 properties in the time period transacted under the 20% lower mark of the median price. If an investor were to buy all these properties, the transaction amount would be USD84.149.567,00. While the potential sell USD109.394.437,10 at a 30% higher price. That would make a possible profit of USD25.244.870,10. Of course, we are considering the bulk of the area. Not considering an aggressive buy would drive prices up - however for a small investor, that would be a possible strategy.

## Other Top Regions

Even though we have chosen a single region, other regions could yield great deals. Check the summary:

![image](https://user-images.githubusercontent.com/66756007/176127715-cfaccd73-929c-46c4-9c8c-7beb25c7d4ab.png)



---
Outdated old dashboard url: https://house-analysis-dashboard.herokuapp.com/
New dashboard url: https://fu-seattle.streamlit.app/




