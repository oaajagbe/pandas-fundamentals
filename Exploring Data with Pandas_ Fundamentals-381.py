## 1. Introduction to the Data ##

## print the first 10 rows in the f500 dataframe
f500_head = f500.head(10)
f500_head.info()

## 2. Vectorized Operations ##

## use vectorized operations to calculate the changes in rank for each company.

rank_change = f500["previous_rank"] - f500["rank"]

## 3. Series Data Exploration Methods ##

rank_change =  f500["previous_rank"] - f500["rank"]

## Like NumPy, pandas supports many descriptive stats methods that can help us answer these questions. Here are a few of the most useful ones (with links to documentation):

# Series.max()
# Series.min()
# Series.mean()
# Series.median()
# Series.mode()
# Series.sum()

## Find the biggest increase and biggest decrease in rank!

rank_change_max = rank_change.max()
rank_change_min = rank_change.min()

## 4. Series Describe Method ##

## the Series.describe() method. This method tells us how many non-null values are contained in the series, along with the mean, minimum, maximum, and other statistics

# Return a series of descriptive statistics for the rank column in f500
rank = f500["rank"]
rank_desc = rank.describe()

# Return a series of descriptive statistics for the previous_rank column in f500
prev_rank = f500["previous_rank"]
prev_rank_desc = prev_rank.describe()

## 5. Method Chaining ##

# Use Series.value_counts() and Series.loc to return the number of companies with a value of 0 in the previous_rank column in the f500 dataframe

zero_previous_rank = f500["previous_rank"].value_counts().loc[0]

## 6. Dataframe Exploration Methods ##

import pandas as pd
f500 = pd.read_csv('f500.csv',index_col=0)
f500.index.name = None

# Use the DataFrame.max() method to find the maximum value for only the numeric columns from f500
max_f500 = f500.max(axis=0, numeric_only=True)

## 7. Dataframe Describe Method ##

## Return a dataframe of descriptive statistics for all of the numeric columns in f500
f500_desc = f500.describe()

## 8. Assignment with pandas ##

# Assigning values in pandas
## assignmet coukld be by either Perform assignment in pandas or  Boolean indexing in pandas.

# assigning values using our full Fortune 500 dataframe

f500.loc["Dow Chemical", "ceo"] = "Jim Fitterling"

## 9. Using Boolean Indexing with pandas Objects ##

## use boolean indexing to identify companies belonging to the "Motor Vehicles and Parts" industry in our Fortune 500 dataset.
motor_bool = f500["industry"] == "Motor Vehicles and Parts"

# Use the motor_bool boolean series to index the country column.
motor_countries = f500.loc[motor_bool, "country"]

## 10. Using Boolean Arrays to Assign Values ##

## Use boolean indexing to update values in the previous_rank column of the f500 dataframeimport

import numpy as np

prev_rank_before = f500["previous_rank"].value_counts(dropna=False).head()

f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan
prev_rank_after = f500["previous_rank"].value_counts(dropna=False).head()

## 11. Creating New Columns ##

# create a rank_change column in our f500 dataframe next.
f500["rank_change"] = f500["previous_rank"] - f500["rank"]
rank_change_desc = f500["rank_change"].describe()

## 12. Challenge: Top Performers by Country ##

industry_usa = f500["industry"][f500["country"] == "USA"].value_counts().head(2)
sector_china = f500["sector"][f500["country"] == "China"].value_counts().head(3)

## 12. Challenge: Top Performers by Country ##

industry_usa = f500["industry"][f500["country"] == "USA"].value_counts().head(2)
sector_china = f500["sector"][f500["country"] == "China"].value_counts().head(3)