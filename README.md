<div id="wrapper">

<div id="main">

<div class="inner">

[**House Sales in King County, USA** by Fulvio](index.html)

<div id="banner" class="section">

<div class="content">

# Insights on real estate for purchase and resale

This project was carried out using data available on the
[kaggle](https://www.kaggle.com/datasets/harlfoxem/housesalesprediction)
website. The objective is to identify good deals on properties for
purchase with subsequent profit.

The dataset comprehends house sales prices for King County, Seattle,
USA. It includes homes sold between May 2014 and May 2015.

If you want to jump right to the HEROKU dashboard with suggestions for
deals, [please click here](https://house-analysis-dashboard.herokuapp.com/).

You can also check the Jupyther notebook for the project [here](https://github.com/fusaa/house-dashboard/blob/main/0%20-%20king%20county.ipynb).
</div>

</div>

<div class="section">

The Insight Analysis was conducted in order to answer the question for
potential investors, which houses should be bought and for what value
they should be sold.

It was done in Python using libraries like Pandas, Numpy, Streamlit,
Folium, Seaborn. Also a dashboard to Heroku was deployed.

<div class="col-4 col-12-medium">


### The objective

From the point of view of making an investment in a property thinking
about resell value with little knowlodge of the local market it was
developed a dashboard with a few insights to help the decision making
proccess.

### The methodology

Using the available database, it was done an EDA (exploratory data analysis) on the
data, in order to seek insights and understand the impact of each variable on the region.

![image](./MindMap.png)
  
### Data

  The data provided only one year of transactions, which made the
analysis more limited. However it was still possible to generate
interisting insights on the data.
  
One important aspect that investors tend to think about is the price per square-foot. That feature has been engineered in the analysis.

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
  1) The square foot of newer houses are more expensive:
  Not true, they tend to be cheaper. The graph shows that properties that was a decline in price in the 50s and it has been kept from 60s onwards.
  ![image](https://user-images.githubusercontent.com/66756007/175946753-a4f0545f-7a9a-46cb-89a4-d7a9f2969971.png)

  2) Cheaper properties are easier to resell.
  It is true, the properties that sell the most are the ones between 300.000 and 400.000 dollars. Moreover the properties between 200.000 and 600.000 account for over 67% of the transactions.
  ![image](https://user-images.githubusercontent.com/66756007/175947287-c685603f-9370-4bd4-9e49-bdeab8e9dce2.png)

  3) The larger the property(living area) the cheaper the square foot:
  That would be true in relative terms. If considered the properties only with a size up to 2.500 sqft, beyond that values will get higher. So the statement must be rejected.
  ![image](https://user-images.githubusercontent.com/66756007/175947619-57826309-f859-4910-9986-bfe74919dee0.png)

  4) The larger the property + lot size, the cheaper the square foot:
  To answer this the dataset has been sliced in 20.000 sqft increaments for the computated area, according to the graph and the presence of outliers this hypothesis has become unconclusive. So can´t be validated using the whole of the dataset.
  
  ![image](https://user-images.githubusercontent.com/66756007/175947936-531fb2ae-6a6b-4201-9bde-be860731c314.png)

  5) During certain quarters of the year prices are higher:
  The dataset comprehends only one year, so it makes it hard to come to a conclusion. Worth mentioning the graph for the specific period the data is available shows no significant difference between quarters.
  ![image](https://user-images.githubusercontent.com/66756007/175948131-e6225c6f-41f6-4935-a19c-cf176f448871.png)
  
  6) Properties renovated in the last 30 years will sell more expensive.:
  As seen on the graph, 'recently' renovated properties will sell for more- a question to raise would be what kind of renovation a property has to undergo in order to be considered renovated.  Therefore this assumption can be accepted.
  ![image](https://user-images.githubusercontent.com/66756007/175949030-bc3270ae-93ad-430b-997a-32affa301314.png)



  
  7) Regions where the renovation rate is higher tend to have a higher price.
  Calculating the median price for each specific zipcode and comparing the renovation-rate(which takes in account the percentage of properties transactioned in the period that had been renovated) it is safe to assume that a neighbourhood that has higher renovation rates will have higher prices. The correlation result of 0.66 clearly shows that. Hypothesis accepted.
  ![image](https://user-images.githubusercontent.com/66756007/175949159-71990459-333e-47b9-94d7-5bcc6d2b59c6.png)
  
  
  
 ##  Multivariate analysis
  Checking the multivariate analysis there are a few interesting correlations noticed, prices strongly correlates to areas of the construction (sqft_living, sqft_above, sqft_basement), as well to the construction area of the surrounding properties(sqf_living15), which makes sense.

Waterfront properties tend to have a high view rating, as well as the number of bedrooms, bathrooms, floors and grade have all strongly relates to each other

![image](https://user-images.githubusercontent.com/66756007/175943062-a7c91ae3-151b-45f9-8623-d756828d9d09.png)


![image](https://user-images.githubusercontent.com/66756007/175942914-7fcdaeea-f7ad-4bc9-a0eb-c508d2f18659.png)


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







