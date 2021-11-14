# " DATA PREPROCESSING & BINARY CLASSIFICATION "

  * Handle features of various data types.
  * The features should be preprocessed and transformed to numeric representation, before training an ML model on the data.
  
## Data source

Your task is to predict the survival of Titanic passengers. Training data is in file **data.csv** and validation data in **evaluation.csv**.

### Features
* survived - 0 = No, 1 = Yes, **target variable**, 
* pclass - passenger's class, 1 = first, 2 = second, 3 = third
* name
* sex
* age - in years
* sibsp	- number of siblings / spouses onboard
* parch - number of parents / children onboard
* ticket - ticket number
* fare - ticket fare
* cabin	- cabin number
* embarked	- place of embarkment, C = Cherbourg, Q = Queenstown, S = Southampton
* home.dest - Home/destination

## Instructions

**Basic points of the assignment**:
  * In the Jupyter notebook load **data.csv**. Split the data into subsets suitable for ML model training.
  * Explore and transform particular features into a format suitable for the selected classification method.
  * You can create new features (based on the existing ones), e.g. you can create a column with the length of the passenger's name. You can drop some features entirely too.
  * Handle the missing values in the dataset.
  * Select a suitable classification method from the lectures. Train it on the training set and tune the hyperparameters. Compute its accuracy on the training and validation set.
  * Load data from the file **evaluation.csv**. Compute predictions from these data (there are no target variable values in the file). Create a file **results.csv** and save your predictions into two columns - ID and the prediction of surviving. Upload this file alongside the Jupyter notebook to the repository.
  * Possible head of the file **results.csv**:
  
```
ID,survived
1000,0
1001,1
...
```
**Further points of assignment**:
  * Apply all of the classification methods discussed in the lectures to the problem. Select the best one based on the accuracy on the validation set. Use cross-validation to estimate the real accuracy of the best model. Use this model for prediction on the **evaluation.csv** data.
  * Try to use at least two advanced methods for filling missing values in the `age` feature. Explore the impact of these methods on the performance of the trained model. Use the method which you find to perform the best for the prediction on the **evaluation.csv** data.
  
