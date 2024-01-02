## 1. Introduction ##

import pandas as pd
# read the data set into a pandas dataframe
f500 = pd.read_csv("f500.csv", index_col=0)
f500.index.name = None

# replace 0 values in the "previous_rank" column with NaN
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

f500_selection = f500[["rank", "revenues", "revenue_change"]].head()

## 2. Reading CSV files with pandas ##

## see what the dataframe looks like if we use pandas.read_csv() without the index_col parameter
f500 = pandas.read_csv("f500.csv")
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

## 3. Using iloc to select by integer position ##


fifth_row = f500.iloc[4]
company_value = f500.iloc[0, 0]

## 4. Using iloc to select by integer position continued ##

## practice some DataFrame.iloc[] calls
# select the first 3 rows from the dataframe
first_three_rows = f500.iloc[0:3]

## Select the first and seventh rows and the first five columns of the f500 dataframe.
first_seventh_row_slice = f500.iloc[[0,6],:5]

## 5. Using pandas methods to create boolean masks ##

##There are also a number of pandas methods that return boolean masks useful for exploring data.

## Two examples are the Series.isnull() method and Series.notnull() method. These can be used to select either rows that contain null (or NaN) values or rows that do not contain null values for a certain column.

## TASK
## Use the Series.isnull() method to select all rows from f500 that have a null value for the previous_rank column. Select only the company, rank, and previous_rank columns

null_previous_rank = f500[f500["previous_rank"].isnull()][["company", "rank", "previous_rank"]]

## 6. Working with Integer Labels ##

null_previous_rank = f500[f500["previous_rank"].isnull()]
top5_null_prev_rank = null_previous_rank.iloc[:5]

## 7. Pandas Index Alignment ##

previously_ranked = f500[f500["previous_rank"].notnull()]
rank_change = previously_ranked["previous_rank"] - previously_ranked["rank"]
f500["rank_change"] = rank_change

## 8. Using Boolean Operators ##

## practice more complex selection using boolean operators.
# Select all companies with revenues over 100 billion and negative profits from the f500 dataframe
large_revenue = f500["revenues"] > 100000
negative_profits = f500["profits"] < 0
combined = large_revenue & negative_profits
big_rev_neg_profit = f500[combined]

## 9. Using Boolean Operators Continued ##

## Select all rows for companies whose country value is either Brazil or Venezuela
brazil_venezuela = f500[(f500["country"] == "Brazil") | (f500["country"] == "Venezuela")]

## Select the first five companies in the Technology sector for which the country is not the USA from the f500 dataframe
tech_outside_usa = f500[(f500["sector"] == "Technology") & ~(f500["country"] == "USA")].head()

## 10. Sorting Values ##

## Let's find the Japanese company with the most employees next.
# Find the company headquartered in Japan with the largest number of employees.
highest_employer_japan = f500[f500["country"] == "Japan"].sort_values("employees", ascending=False).iloc[0]
top_japanese_employer = highest_employer_japan["company"]

## 11. Using Loops with pandas ##

# Create an empty dictionary
top_employer_by_country = {}

# create an array of unique values from the country column.
countries = f500["country"].unique()

# Use a for loop to iterate over the array unique countries
for c in countries:
    # Use boolean comparison to select only rows that
    # correspond to a specific country
    selected_rows = f500[f500["country"] == c]
    
    ##  sort those rows by the employees column in descending order.
    sorted_rows = selected_rows.sort_values("employees",  ascending=False)
    
    # Select the first row from the sorted dataframe.
    top_employer = sorted_rows.iloc[0]
    
    # Extract the company name from the index label company from the first row.
    top_employer_name = top_employer["company"]
    
    ## Assign the results to the top_employer_by_country dictionary, using the country name as the key, and the company name as the value.
    top_employer_by_country[c] = top_employer_name

## 12. Challenge: Calculating Return on Assets by Sector ##

#################
## In this challenge we're going to add a new column to our dataframe, and then perform some aggregation using that new column.

## The column we create is going to contain a metric called return on assets (ROA). ROA is a business-specific metric which indicates a company's ability to make profit using their available assets.
#################

## Create a new column roa in the f500 dataframe, containing the return on assets metric for each company.
f500["roa"] = f500["profits"] / f500["assets"]

# Aggregate the data by the sector column, and create a dictionary top_roa_by_sector
top_roa_by_sector = {}
roa_sector = f500["sector"].unique()
for sector in f500["sector"].unique():
    is_sector = f500["sector"] == sector
    sector_companies = f500.loc[is_sector]
    top_company = sector_companies.sort_values("roa",ascending=False).iloc[0]
    company_name = top_company["company"]
    top_roa_by_sector[sector] = company_name