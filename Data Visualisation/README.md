# " DATA VISUALISATION & WEB SCRAPPING "

  * Download (*scrape*) data from the web, process it and visualise.
  * The objective is to download data from server https://www.psp.cz/en/sqw/hlasovani.sqw?o=8 regarding voting in the Chamber of Deputies of the Parliament of the Czech Republic, save it in a tabular form and create visualisations, which make exploration of the data easier and show interesting information about it.

## Data

 * Download data from all votings of the current Chamber of Deputies (since 2017). Download details of voting of particular deputies.
 * Data should contain basic information about the voting - number of meeting, number of voting, point of the meeting and date.

## Instructions


**Basic points of the assignment**:
  * Write Python script for downloading data. Download the data and save it in a suitable machine-readable format.
  * **Wait at least 1 second between two consecutive requests to the server, to not overload it.**
  * In the second part of the notebook, work with the data loaded from a local file. File(s) with downloaded data should be submitted as well (so the reviewer do not have to download the data again).
  * Create visualisations to show the following:
    * Deputies changing their parliamentary clubs.
    * Attendance of individual deputies in the votings. Attendance of parliamentary clubs in the votings.
    * How often individual parliamentary clubs vote the same and different.
    * Are deputies in the same parliamentary club voting the same? Who are the biggest rebels?

**Further points of assignment**:
  * Visualise some time development in the data (e.g. attendance, change of agreement in voting among individual parliamentary clubs, etc.)
  * Find individual deputies who have the most similar voting or attendance.
  * Try to find particular voting, where deputies voted the most differently than traditionally.
  
## Tips and tricks
  * Import libraries at the beginning of the notebook, or the beginning of scraping and visualisation parts.
  * Use markdown cells (like this one) and headings to make orientation in the notebook easier.
  * Select plots and visualisation matching the information you want to show. You can see galleries of libraries `matplotlib` and `seaborn` for inspiration.
