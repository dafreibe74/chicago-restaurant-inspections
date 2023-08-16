# Group 5
## Project 4 Final Write Up

Data Sources:
https://www.kaggle.com/datasets/chicago/chicago-food-inspections?resource=download
https://data.cityofchicago.org/Health-Human-Services/Food-Inspections/4ijn-s7e5

Rows: 200K 

Columns: 22 


Group Members
  * Noah Bazis
  * Peter Ferguson
  * Dave Freiberg
  * Jesus Viloria Paolini

 
# RESEARCH QUESTION
Is there any relationship between Chicago zip codes and a restaurant’s likelihood of failing its Health Inspection? To answer this question, we employed a Random Forest Classifier along with a normalized confusion matrix heatmap to predict the likelihood of receiving a High Risk rating from the Department of Public Health based on a restaurant's zipcode.

# ORDER OF OPERATIONS
## Database Creation & Data Retrieval:
We retrieved the CSV from the City of Chicago Data Portal and manipulated the dataset using Pandas to remove extraneous information and streamline processing. We then created a SQL database, uploaded the cleaned dataset, and produced a SQLite file for the team to establish a database connection.

## Data PreProcessing & Model Implementation:
First, the "Risk" column was converted to numerical values using LabelEncoder, and any missing values were labeled "Unknown."​ Next, the relevant features ("Results" and "zip") were selected for prediction and stored in the variables X (feature matrix) and y (target variable). The Results and zip features were then one-hot encoded and missing values in the feature matrix were imputed using the mean strategy with SimpleImputer​. The feature matrix and target variable were split into training and testing sets using train_test_split.

## Model Testing & Optimization:
A RandomForestClassifier model with 100 estimators was initialized and trained using the training data to predict the Risk levels for the testing data. The model was run 5 times and accuracy scores ranged between 74% and 76%.​ 

## Final Evaluation and Display:
Employing the confusion matrix, we identified a correlation with 76% accuracy correlating zip code to the level of risk in failed inspections, the highest accuracy score achieved. Furthermore, the distribution of High Risk ratings was more than double that of both the Medium Risk and Low Risk ratings combined. Given that most data points in the test data corresponded to the High Risk 1 category, the model tended toward predicting the High Risk 1 category resulting in a higher accuracy score.

## Limitations & Further Research:
Several attempts were made to produce a linear regression but were unsuccessful at achieving an acceptable accuracy score. The data was better suited for multi-categorical classification models and we would recommend using these models in future analyses of this data.   


