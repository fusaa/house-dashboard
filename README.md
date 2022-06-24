Kings County Hose Sales    

[**House Sales in King County, USA** by Fulvio](index.html)

Insights on real estate for purchase and resale
===============================================

This project was carried out using data available on the [kaggle](https://www.kaggle.com/datasets/harlfoxem/housesalesprediction) website. The objective is to identify good deals on properties for purchase with subsequent profit.

The dataset comprehends house sales prices for King County, Seattle, USA. It includes homes sold between May 2014 and May 2015.

If you want to jump right to the heroku dashboard with suggestions for deals, please click here..

![](images/How-much-data-is-enough.jpg)

The Insight Analysis was conducted in order to answer the question for potential investors, which houses should be bought and for what value they should be sold.

It was done in Python using libraries like Pandas, Numpy, Streamlit, Folium, Seaborn. Also a dashboard to Heroku was deployed.

### Data

Available data can be described according to the following table:

Name

Description

id

Unique ID for each transaction.

date

Transaction Date.

price

Transaction ammount.

bedrooms

Number of bedrooms.

bathrooms

Number of bathrooms. '.5' accounts for toilet.

sqft\_living

Square footage living area.

sqft\_lot

Lot size.

floors

Number of pavements.

waterfront

Means house has a view to waterfront.

view

Score 1-4 on how good view is.

Name

Description

grade

Score on building construction and design. Eg 7 is average level, the higher the better.

sqft\_above

House interior area above ground level.

yr\_build

Year house was built.

yr\_renovated

When house was renovated.

zipcode

Zipcode.

lat

Property latitude.

lon

Property lontitude.

sqft\_living15

Size in square foot of the nearest 15 neighbors.

sqft\_lot15

Size of the land of the nearest 15 neighbors.

bathrooms

Number of bathrooms.

### The objective

From the point of view of making an investment in a property thinking about resell value with little knowlodge of the local market it was developed a dashboard with a few insights to help the decision making proccess.

### The methodology

Using the available database, it was done an exploratory analysis on the data, in order to identify a good strategy for reselling.

The data provided only one year of transactions, which makes the analysis more limited. However it was still possible to generate interisting insights on the data.

### The data

![](images/01 - price density.png)Price Density

![](images/02 - numerical variables.png)Price Density

![](images/02 - numerical variables.png)Price Density

![](images/02 - numerical variables.png)Price Density

![](images/02 - numerical variables.png)Price Density

![](images/02 - numerical variables.png)Price Density

![](images/02 - numerical variables.png)Price Density
