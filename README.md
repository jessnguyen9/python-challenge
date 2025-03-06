# Election and Budget Analysis Using Python

## Overview
Conducted financial and election data analysis using Python to surface key insights into budgeting trends and voter distribution. The project involved extracting, cleaning, and analyzing financial and election data to provide actionable recommendations.

## Data Acquisition & Preparation
### Data Sources
* **Budget Analysis** (budget_data.csv): Contains financial data with monthly profit/loss records.
* **Election Analysis** (election_data.csv): Records votes for different candidates across multiple regions.

### Data Cleaning & Manipultion Techniques:
* Handled missing and inconsistent values by ensuring data integrity before analysis.
* Converted financial data types for accurate mathematical operations.
* Aggregated voting data to determine candidate vote shares.
* Performed transformations such as calculating month-over-month financial changes and percentage of votes per candidate.

## Data Analytics
### Budget Analysis
1. Sample Output
```python
Financial Analysis
-------------------------
Total Months: 85
Total: $21475215
Average Change: $-8410.05
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
```
2. Insights & Recommendations
- The data spans 85 months with a total revenue of $21,475,215. This indicates a long-term financial tracking across multiple years, reflecting steady revenue over time.
- The average monthly change in profit is -$8,410.05, showing that on average, there are more losses than gains month-over-month.
- There was a large spike in profits in August 2016, suggesting a potential event, marketing campaign, or special promotion led to this jump. Identify key factors that drove this success. Analyzing similar months for recurring factors could help pinpoint replicable success strategies.
- A significant decrease in profits occurred in February 2014. Investigate reasons for the downturn in February 2014. Understanding the exact cause can help prevent or mitigate similar future declines
### Election Analysis
1. Sameple Output
```python
Election Results
-------------------------
Total Vote: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
```
2. Recommendations

## Technologies & Tools Used
* **Python** (CSV handling, dictionary operations, data transformation)
* **Panda & Numpy**
* **Data Visualization**
