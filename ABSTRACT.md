# Abstract
- visualizations
- What is the so-what?  What about your findings is actionable?
- Supervised learning
- Sentiment analysis

- A well-defined question with a well-defined answer
- 
Abstract section that briefly explains your problem, your methodology, and your findings, and business recommendations as a result of your findings.

## Purpose

Coffee is the second most consumed beverage IN THE WORLD (behind tea, but ahead of soda and beer), at a rate of about 2.25 billion cups a day (https://www.statista.com/statistics/292595/global-coffee-consumption/).  There are a variety of factors that make up the differences between coffee beans.  A non-exhaustive list of factors includes:
 - Ratings for aroma, acidity, flavor, aftertaste, body, 
 - Agtron score (an agtron machine reflects light on a sample of coffee to objectively assign a number for roast color)  
 - price
 - coffee bean origin
 - roaster location
 - altitude
 - roast level
 
The goal of this project is to examine what makes a coffee bean great (highly rated) and makes it stand out from the crowd.  This knowledge is relevant to everyday people searching for a great coffee bean for their morning brew, for restuarants and coffee bars delivering product that the consumer wants and developing global strategies for growers/roasters/distributors as they deal with complex environmental issues impacting this $100 billion dollar industry, second only to oil (https://globaledge.msu.edu/blog/post/55607/the-global-coffee-industry). 
  
 
## Methodology

The OSEMN (Obtain, Scrub, Explore, Model, iNterpret) framework was followed in the creation of this project.  Data was sourced from www.coffeereviews.com and scraped using BeautifulSoup. The dataset was cleaned using pandas, NumPy, regex.  Visualizations were created using Matplotlib, Seaborn and Geopandas.  Machine learning (supervised) models were created using scikit-learn logistic regression, random forest, random forest with SMOTE and GridSearchCV and xgboost.  Additional neural network models using MLP were created to corroborate the findings from the one-layer classification models.  Interpretaion was completed by using the feature importance returned by the modeling.  The intrepreation - the top features comtributing to highly rated coffee beans - can be used by individual coffee drinkers wanting knowledge about the product they consume, by restuarants and coffee bars wanting the knowledge so as to serve coffee that is pleasing to their customers and for roasters, growers, distributors and buyers interested in navigating a highly lucrative industry into the 21st century with new environmental and social issues arising.

## Findings

Five thousand, five hundred and fifteen coffee reviews were scraped from the coffee review website.  Every coffee was assigned a rating by a coffee reviewer. The ratings started at 68 and increased all the way to 97.  One first glance, it would seem that the rating would simply be attributed to price per oz.  <coffee_rating_price.png here>  The growers per country was plotted on a world map using geopandas.  



## Significance

The xgboost (one-layer classificiaton model) predicted with 98.18% accuracy that highly rated coffees (95, 96 or 97) owe their rating to the coffee's aroma score, flavor score, body score, aftertaste score and acidity score.  The important features were corroborated with the multi-layer neural network model (MLP) in accuracy of 98.18% and the same important features but in a different order (body-flavor-aftertaste-acidity-aroma.)  Interestingly, the country with the greatest number of growers in this set, Ethiopia wihth 441 and Kenya with 272, did not make the top 5 and price per oz was 6th place adn 10th place, xgboost and mlp respectively. 

## Conclusions
With the use of machine learning models xgboost and nueral network MLP, models were created that have a very high accuracy of 98.18% to predict the top 5 features - body, flavor, aftertaste,acidity,aroma -  that contribute to a highly rated coffee bean. Of lesser importance, but still in the top 10, was price per ounce and the two top producing coffee countries, Ethiopia and Kenya. 
