# " CLUSTERING OF E-SHOP CUSTOMERS "

An essential application of clustering is **customer segmentation**. 

Given transactional data of the form:

>TransactionID, CustomerID, Date (of the purchase), Subtotal (the price of the purchase)

we want to find segments of customers with similar behaviour. For this, we need to aggregate the transactions and have **one row as one customer**.

A popular framework to do that is **RFM**, which means:

- **R**ecency: Day since last purchase (last date in the data set - last purchase date set of a given customer)
- **F**requency: Number of purchases. Customers with only one purchase are sometimes excluded; let's leave them in the dataset for simplicity.
- **M**onetary: Total amount spent by the customer.

## Data source

Data about purchases of an (almost) fake e-shop are in the file `eshop.csv`.

## Instructions

Take the date of the last transaction (19. 12. 2015) as the actual date of the analysis - to simulate that the data is current.

**Basic points of the assignment**:
  * Create an `rfm` data frame that has as many rows as customers, where each row is a customer, and the other columns are calculated as described above.
  * Use `k-means` for clustering. Find the optimal number of clusters (explain why you have chosen it).
  * Work with scaling and standardization of the data. Is it needed? Do it if yes.
  * Give an interpretation for the clusters. Can the clusters help you identify some superstar customers (high monetary, high frequency, low recency) from lousy ones (high recency, low frequency, low monetary)? Identify them.

**Further points of assignment**:
  * Use the method Silhouette to analyze the found clusters (https://en.wikipedia.org/wiki/Silhouette_(clustering)).
  * Do the clustering with a modified version of **RFM** where
    * Recency: a maximum of the number of months since the last purchase and number 1.
    * Frequency: a maximum of the number of purchases during last 12 months and number 1.
    * Monetary: the highest price of a single purchase of the given customer.
    
    Compare results with the original approach.
