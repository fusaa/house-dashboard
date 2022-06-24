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

If you want to jump right to the heroku dashboard with suggestions for
deals, please click here..

</div>

<span class="image object"> ![](images/How-much-data-is-enough.jpg)
</span>

</div>

<div class="section">

The Insight Analysis was conducted in order to answer the question for
potential investors, which houses should be bought and for what value
they should be sold.

It was done in Python using libraries like Pandas, Numpy, Streamlit,
Folium, Seaborn. Also a dashboard to Heroku was deployed.

<div class="col-4 col-12-medium">

### Data

Available data can be described according to the following table:

<div class="row">

<div class="col-6 col-12-small">

<div class="table-wrapper">

| Name         | Description                                    |
| ------------ | ---------------------------------------------- |
| id           | Unique ID for each transaction.                |
| date         | Transaction Date.                              |
| price        | Transaction ammount.                           |
| bedrooms     | Number of bedrooms.                            |
| bathrooms    | Number of bathrooms. '.5' accounts for toilet. |
| sqft\_living | Square footage living area.                    |
| sqft\_lot    | Lot size.                                      |
| floors       | Number of pavements.                           |
| waterfront   | Means house has a view to waterfront.          |
| view         | Score 1-4 on how good view is.                 |

</div>

</div>

<div class="col-6 col-12-small">

<div class="table-wrapper">

| Name           | Description                                                                              |
| -------------- | ---------------------------------------------------------------------------------------- |
| grade          | Score on building construction and design. Eg 7 is average level, the higher the better. |
| sqft\_above    | House interior area above ground level.                                                  |
| yr\_build      | Year house was built.                                                                    |
| yr\_renovated  | When house was renovated.                                                                |
| zipcode        | Zipcode.                                                                                 |
| lat            | Property latitude.                                                                       |
| lon            | Property lontitude.                                                                      |
| sqft\_living15 | Size in square foot of the nearest 15 neighbors.                                         |
| sqft\_lot15    | Size of the land of the nearest 15 neighbors.                                            |
| bathrooms      | Number of bathrooms.                                                                     |

</div>

</div>

</div>

<div class="col-4 col-12-medium">

### The objective

From the point of view of making an investment in a property thinking
about resell value with little knowlodge of the local market it was
developed a dashboard with a few insights to help the decision making
proccess.

</div>

<div class="col-4 col-12-medium">

### The methodology

Using the available database, it was done an exploratory analysis on the
data, in order to identify a good strategy for reselling.

The data provided only one year of transactions, which makes the
analysis more limited. However it was still possible to generate
interisting insights on the data.

</div>

<div class="col-4 col-12-medium">

### The data

<div class="col-4 col-12-medium">

<span class="image left">![](images/01%20-%20price%20density.png)</span>Price
Density

</div>

<div class="col-4 col-12-medium" style="float: left">

<span class="image left">![](images/02%20-%20numerical%20variables.png)</span>Price
Density

</div>

<div class="col-4 col-12-medium" style="float: left">

<span class="image left">![](images/02%20-%20numerical%20variables.png)</span>Price
Density

</div>

<div class="col-4 col-12-medium" style="float: left">

<span class="image left">![](images/02%20-%20numerical%20variables.png)</span>Price
Density

</div>

<div class="col-4 col-12-medium" style="float: left">

<span class="image left">![](images/02%20-%20numerical%20variables.png)</span>Price
Density

</div>

<div class="col-4 col-12-medium" style="float: left">

<span class="image left">![](images/02%20-%20numerical%20variables.png)</span>Price
Density

</div>

<div class="col-4 col-12-medium" style="float: left">

<span class="image left">![](images/02%20-%20numerical%20variables.png)</span>Price
Density

</div>

</div>

</div>

</div>

</div>

</div>

</div>
