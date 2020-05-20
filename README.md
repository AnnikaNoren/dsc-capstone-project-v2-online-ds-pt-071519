

# Finding the Perfect Cup of Coffee



## Project Movitation
 
A hot cup of coffee is a pretty wonderful way to start my day. It’s a small slice of heaven in a crazy, unpredictable world. Wouldn’t it be great to know what makes a cup of coffee <i>sublime</i> so as to never be disappointed?  Therein lies the beauty of machine learning to be able to figure out which features make a coffee great (highly rated) and stand out from the crowd. This is useful information on a personal level and can also be used by coffee shops, baristas, restuarants and other coffee enthusiasts.



<img src='https://media.giphy.com/media/cMPTAogPBRTIQ/giphy.gif'>


## Data Source

Coffee is the second most consumed beverage IN THE WORLD (behind tea, but ahead of soda and beer), at a rate of about 2.25 billion cups a day (footnote 1).  There are a variety of factors that make up the differences between coffee beans.  A non-exhaustive list of factors includes:
 - Ratings for aroma, acidity, flavor, aftertaste, body, 
 - Agtron score (an agtron machine reflects light on a sample of coffee to objectively assign a number for roast color)  
 - price
 - coffee bean origin
 - roaster location
 - altitude
 - roast level
 
The dataset for my project scraped by me from the website www.coffeereviews.com. 
 

## Methodology

The OSEMN (Obtain, Scrub, Explore, Model, iNterpret) framework was followed for this project.  Data was scraped using BeautifulSoup and cleaned using pandas, NumPy and regex.  Visualizations were created using Matplotlib, Seaborn, Geopandas and Dash.  Machine learning (supervised) models were created using scikit-learn's logistic regression, random forest, random forest with SMOTE and GridSearchCV, and xgboost.  Additionally, neural network models using MLP were created to corroborate the findings from the one-layer classification models.  Interpretaion was completed by using the feature importance function returned by the model.  The results from feature importance - the top 6 features contributing to highly rated coffee beans - can be used by individual coffee drinkers wanting knowledge about the product they consume, by restuarants and coffee bars wanting the knowledge so as to serve coffee that is pleasing to their customers and for roasters, growers, distributors and buyers interested in navigating a highly lucrative industry into the 21st century with new environmental and social issues arising.  Finally, an interactive plot was produced using a DASH app on Visual Studio Code.



![](DASH.png)





## Findings

Five thousand, five hundred and fifteen coffee reviews were scraped from the coffee review website.  Every coffee was assigned a rating by a coffee reviewer. The ratings started at 68 and increased all the way to 97.  One first glance, it would seem that the rating would simply be attributed to price per oz.  <coffee_rating_price.png here>  The growers per country was plotted on a world map using geopandas.  

The XGboost model turned out to be the most accurate at 98.2% accuracy for the test data and 99.76% accurate for the train data. The small difference between the two accuracies indicates a small overfitting of the model. The top 6 features of a highly rated coffee (the top 8% of the data set with a rating of 95, 96 or 97) were:
 1. Aroma
 2. Flavor
 3. Body
 4. Aftertaste
 5. Acidity
 6. Price per ounce
 
 
 ![](coffee_xgb.png)
 
 

Interestingly, when the dataset was modeled using MLP (the python library Kera's multi-layer perceptron) it resulted in a accuracy of 98.18% and the top 6 features as follows:
 1. Body
 2. Flavor
 3. Aftertaste
 4. Acidity
 5. Aroma
 6. Ethiopia
 
Here is the resulting confusion matrix: 


![](cm_great.png)


The highest number of coffee growers were located in Ethiopia and Kenya, these two countries arrived in spot 11 and 9 on the list of important features.



![](coffee_country_plot.png)




### Success Criteria

The xgboost model and MLP model both delivered a high test and train accuracy of 98.2%, which is better than all the other models.  Here is a chart comparing the classification models test and train accuracies to each other: 


 
![](class_accuracy.png)



And here is the results of MLP:


![](mlp.accuracy.png)



## Business Recommendations

Two machine learning algorithms (xgboost and mlp) applied to a unique dataset of coffee reviews generate a model to predict with 98.2% accuracy the 5 important features in determining if a coffee bean is great or not.  The top five features were indentica in both models only differeing in the order: acidity, aftertaste, aroma, body and flavor. 

This knowledge is relevant and useful to individal coffee drinkers looking for high quality product, as well as, hotel/resturant/coffee show owners and baristas.  The information gleaned from machine learning models can be used to provide high quality coffee to customers that they will love to keep them coming back and to continue to grow your business. This is especially useful as the world grapples with affects of global warming on crops. 



## Applicable Files

The applicable files in this repository for this project are:

- README.md is this file
### Data
- AN_coffee_reviews.csv is the data scraped from www.coffeereviews.com
- part1_cleaned_coffee_reviews.csv is the first of three phases of cleaning
- part2_cleaned_coffee_reviews.csv is the second of three phases of cleaning
- cleaned_coffee_reviews.csv is the final cleaned dataset used to work with
### Scraping, Cleaning, Modeling, Visualizing, Applying Neural Network and Sentiment Analysis
- scraping_coffee_reviews.ipynb contains the code used to scrape the website for coffee reviews
- cleaning_coffee_reviews.ipynb contains the code used to clean the dataset
- modeling_coffee_reviews.ipynb contains the code used to model the dataset
- visualizing_coffee_reviews.ipynb contains the code used to visualize the dataset
- neural_network_modeling_coffee_reviews.ipynb contains the code used to model using neural networks
- sentiment_analysis_coffee_reviews.ipynb contains the code used to perform sentiment analysis on the data
### Resources
- AK_scraping_demo.ipynb is a demo file from Abhineet Kulkarni
- playground.ipynb is a scratch pad file
- kaggle_coffee_modified.csv is another coffee review dataset from Kaggle, it is NOT used in the analysis
- Restuarant_Reviews.tsv is the file used for sentiment analysis
### Graphs and Plots
- cm_awful.png and cm_great.png are confusion matrix images
- Countries_WGS84.shx is the file used for geopandas
- Countries_WGS84.shp is the file used for geopandas
- coffee_country_plot.png is my country map
- coffee_xgb.png is my feature importance graph from the XGBoost model
- dash_test.py is my Dash app with interactive visuals


## My Additional Resources
Here is a link to my blog which describes my project journey:  https://annikanoren.blogspot.com/2020/05/using-data-science-to-find-my-perfect.html

Here is a link to my youtube business presentation: https://www.youtube.com/watch?v=-ULFdzGPJWM&feature=youtu.be


## Libraries

- NumPy and pandas
- Seaborn and matplotlib for plotting
- Scikit.learn classification models, metrics, confusion matrix, classification report, PCA
- Scikit.learn StandardScaler(), train_test_split
- Time
- BeautifulSoup 
- Regex
- keras, keras.models and .layers for neural network modeling
- Dash app via Visual Studio Code


## Footnote
1. (https://www.statista.com/statistics/292595/global-coffee-consumption/)
