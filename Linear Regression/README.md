# " LINEAR REGRESSION "

  * Objective is to try solving a regression problem on real data.
> **The most important is to perform processes correctly: the splitting of the dataset, hyperparameter tuning, evaluation of the results, etc.**
  
## Dataset

  * Dataset is in the file `LifeExpectancyData.csv` from course pages (original: https://www.kaggle.com/kumarajarshi/life-expectancy-who).
  * You can find the description of the dataset at its Kaggle page.
  * Target variable is `Life expectancy`.
  
## Instructions
**Tasks of the assignment:**
  1. Remove data points with the unknown target variable.
  1. Split data into training and test set.
  1. Look into the data and react to issues in it (missing values, etc.).
  1. Apply Linear Regression and Ridge Regression and adequately evaluate the results:
    * Use `mean_absolute_error` for performance measurements.
    * Experiment with the creation of new features (based on the available ones).
    * Experiment with standardization/normalization of the data.
    * Choose hyperparameters for tuning and find their best values.
  1. Use another model, other than Linear and Ridge Regression, as well.
  1. Compare performances of all of the models, choose the one you would use for prediction on new real-world data and estimate it's performance.
  
