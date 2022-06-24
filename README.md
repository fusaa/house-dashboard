
<html>
	<head>
		<title>Kings County Hose Sales</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="assets/css/main.css" />
	</head>
	<body class="is-preload">


		<!-- Wrapper -->
			<div id="wrapper">

				<!-- Main -->
					<div id="main">
						<div class="inner">

							<!-- Header -->
								<header id="header">
									<a href="index.html" class="logo"><strong>House Sales in King County, USA</strong> by Fulvio</a>
									<ul class="icons">
										<!-- <li><a href="#" class="icon brands fa-twitter"><span class="label">Twitter</span></a></li>
										<li><a href="#" class="icon brands fa-facebook-f"><span class="label">Facebook</span></a></li>
										<li><a href="#" class="icon brands fa-snapchat-ghost"><span class="label">Snapchat</span></a></li>
										<li><a href="#" class="icon brands fa-instagram"><span class="label">Instagram</span></a></li>
										<li><a href="#" class="icon brands fa-medium-m"><span class="label">Medium</span></a></li> -->
									</ul>
								</header>

							<!-- Banner -->
								<section id="banner">
									<div class="content">
										<header>
											<h1>Insights on real estate for purchase and resale</h1>
											<p>This project was carried out using data available on the <a href="https://www.kaggle.com/datasets/harlfoxem/housesalesprediction"> kaggle</a> website. The objective is to identify good deals on properties for purchase with subsequent profit.</p>
											<p>The dataset comprehends house sales prices  for King County, Seattle, USA. It includes homes sold between May 2014 and May 2015.</p>
											<p>If you want to jump right to the heroku dashboard with suggestions for deals, please click here..</p>
										</header>
										<p></p>
										<!--<ul class="actions">
											<li><a href="#" class="button big">Learn More</a></li>
										</ul>-->
									</div>
									<span class="image object">
										<img src="images/How-much-data-is-enough.jpg" alt="" />
									</span>
								</section>

								<section>
									<header class="main">

									</header>

									<!-- Content -->

										<p>The Insight Analysis was conducted in order to answer the question for potential investors, which houses should be bought and for what value they should be sold.</p>
										<p>It was done in Python using libraries like Pandas, Numpy, Streamlit, Folium, Seaborn. Also a dashboard to Heroku was deployed.
											<div class="col-4 col-12-medium">
												<h3>Data</h3>
												<p>Available data can be described according to the following table:</p>
												<div class="row">
													<div class="col-6 col-12-small">

														<div class="table-wrapper">
															<table class="alt">
																<thead>
																	<tr>
																		<th>Name</th>
																		<th>Description</th>

																	</tr>
																</thead>
																<tbody>
																	<tr>
																		<td>id</td>
																		<td>Unique ID for each transaction.</td>

																	</tr>
																	<tr>
																		<td>date</td>
																		<td>Transaction Date.</td>

																	</tr>
																	<tr>
																		<td>price</td>
																		<td>Transaction ammount.</td>

																	</tr>
																	<tr>
																		<td>bedrooms</td>
																		<td>Number of bedrooms.</td>

																	</tr>
																	<tr>
																		<td>bathrooms</td>
																		<td>Number of bathrooms. '.5' accounts for toilet.</td>
																	</tr>
																	<tr>
																		<td>sqft_living</td>
																		<td>Square footage living area.</td>
																	</tr>

																	<tr>
																		<td>sqft_lot</td>
																		<td>Lot size.</td>
																	</tr>

																	<tr>
																		<td>floors</td>
																		<td>Number of pavements.</td>
																	</tr>

																	<tr>
																		<td>waterfront</td>
																		<td>Means house has a view to waterfront.</td>
																	</tr>

																	<tr>
																		<td>view</td>
																		<td>Score 1-4 on how good view is.</td>
																	</tr>




																</tbody>

															</table>
														</div>
													</div>
													<div class="col-6 col-12-small">

														<div class="table-wrapper">
															<table class="alt">
																<thead>
																	<tr>
																		<th>Name</th>
																		<th>Description</th>

																	</tr>
																</thead>
																<tbody>


																	<tr>
																		<td>grade</td>
																		<td>Score on building construction and design. Eg 7 is average level, the higher the better.</td>
																	</tr>

																	<tr>
																		<td>sqft_above</td>
																		<td>House interior area above ground level.</td>
																	</tr>

																	<tr>
																		<td>yr_build</td>
																		<td>Year house was built.</td>
																	</tr>

																	<tr>
																		<td>yr_renovated</td>
																		<td>When house was renovated.</td>
																	</tr>

																	<tr>
																		<td>zipcode</td>
																		<td>Zipcode.</td>
																	</tr>

																	<tr>
																		<td>lat</td>
																		<td>Property latitude.</td>
																	</tr>

																	<tr>
																		<td>lon</td>
																		<td>Property lontitude.</td>
																	</tr>

																	<tr>
																		<td>sqft_living15</td>
																		<td>Size in square foot of the nearest 15 neighbors.</td>
																	</tr>

																	<tr>
																		<td>sqft_lot15</td>
																		<td>Size of the land of the nearest 15 neighbors.</td>
																	</tr>

																	<tr>
																		<td>bathrooms</td>
																		<td>Number of bathrooms.</td>
																	</tr>



																</tbody>

															</table>
														</div>
													</div>


											</div>
											<div class="col-4 col-12-medium">
												<h3>The objective</h3>
												<p>From the point of view of making an investment in a property thinking about resell value with little knowlodge of the local market it was developed a dashboard with a few insights to help the decision making proccess.</p>
											</div>
											<div class="col-4 col-12-medium">
												<h3>The methodology</h3>
												<p>Using the available database, it was done an exploratory analysis on the data,  in order to identify a good strategy for reselling.</p>
												<p>The data provided only one year of transactions, which makes the analysis more limited. However it was still possible to generate interisting insights on the data.</p>
											</div>
											<div class="col-4 col-12-medium">
												<h3>The data</h3>
												<div class="col-4 col-12-medium">
												<p><span class="image left"><img src="images/01 - price density.png" alt="" /></span>Price Density</p></div>
												<div style="float: left" class="col-4 col-12-medium">
												<p><span class="image left"><img src="images/02 - numerical variables.png" alt="" /></span>Price Density</p></div>
												<div style="float: left" class="col-4 col-12-medium">
												<p><span class="image left"><img src="images/02 - numerical variables.png" alt="" /></span>Price Density</p></div>
												<div style="float: left" class="col-4 col-12-medium">
												<p><span class="image left"><img src="images/02 - numerical variables.png" alt="" /></span>Price Density</p></div>
												<div style="float: left" class="col-4 col-12-medium">
												<p><span class="image left"><img src="images/02 - numerical variables.png" alt="" /></span>Price Density</p></div>
												<div style="float: left" class="col-4 col-12-medium">
												<p><span class="image left"><img src="images/02 - numerical variables.png" alt="" /></span>Price Density</p></div>
												<div style="float: left" class="col-4 col-12-medium">
												<p><span class="image left"><img src="images/02 - numerical variables.png" alt="" /></span>Price Density</p></div>


												<!--
												<div>
												<div style="float: left">
												<img src="https://loremflickr.com/320/240" />
												</div>
												<div>
												Text content goes here
												</div>
											</div> -->


											</div>

										</div>
									</section>



						</div>
					</div>

						</div>
					</div>

			</div>

		<!-- Scripts -->
			<script src="assets/js/jquery.min.js"></script>
			<script src="assets/js/browser.min.js"></script>
			<script src="assets/js/breakpoints.min.js"></script>
			<script src="assets/js/util.js"></script>
			<script src="assets/js/main.js"></script>

	</body>
</html>
