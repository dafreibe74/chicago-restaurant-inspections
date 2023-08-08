# Group 5
## Project 4 Proposal

* Our Data Source
https://www.kaggle.com/datasets/chicago/chicago-food-inspections?resource=download

And the source of this data can be found at the City of Chicago
https://data.cityofchicago.org/Health-Human-Services/Food-Inspections/4ijn-s7e5

* Our Group Members
  * Noah Bazis
  * Peter Ferguson
  * Dave Freiberg
  * Jesus Viloria Paolini
 
- Linear regression on a ten period of restaurants in chicgo by location to see if there are patterns in predicting their food safety (RISK) and results of their inspection.   
- Binary classification off of the "Results" column which is what the food inspector experienced when attempting to inspect a restaurant on a given date. 

# ORDER OF OPERATIONS
## Data Retrieval and Preprocessing:
* Retrieve the CSV, enrich it if possible from the Chicago site, and store in SQL.
* Place data into an AWS s3 Bucket for use (Github won't allow large file sizes)
* Clean the data by handling missing values and outliers.
* Normalize and standardize the data to ensure all features are on a similar scale. 

## Data Model Implementation:
* We will be doing both classification or regression).
* Split the data into training and testing sets.
* Initialize, train, and evaluate the model using the training and testing data.
* Measure the model's classification accuracy (for classification) or R-squared (for regression) to ensure meaningful predictive power.

## Data Model Optimization:
* Document the model optimization process by making iterative changes to the model and observing the resulting changes in performance.
* Keep a record of the hyperparameters you experimented with and their corresponding performance metrics (e.g., accuracy, R-squared) in a CSV/Excel table or within the Python script itself.
* Perform techniques like hyperparameter tuning, feature selection, or model selection to improve the model's performance.

## Final Evaluation and Display:
* Python script to print or display the overall model performance, including the final classification accuracy or R-squared.
* Visualize the model's performance through plots / graphs
