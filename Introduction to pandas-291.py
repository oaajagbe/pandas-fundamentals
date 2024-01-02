## 2. Introduction to the Data ##

import pandas as pd
f500 = pd.read_csv('f500.csv',index_col=0)
f500.index.name = None
f500_type = type(f500)
f500_shape = f500.shape

## 3. Introducing DataFrames ##

# select rows in the f500 dataframe
f500_head = f500.head(6) # first 6 rows
f500_tail = f500.tail(8) # last 8 rows

## 4. Introducing DataFrames Continued ##

f500.info()

## 5. Selecting a Column from a DataFrame by Label ##

##########
# Because our axes in pandas have labels, we can select data using those labels — unlike in NumPy, where we needed to know the exact index location. To do this, we can use the DataFrame.loc[] attribute. The syntax for DataFrame.loc[] is:

# df.loc[row_label, column_label]

# We can also use the following shortcut to select a single column:

## col_var = dataset_name["column_label"]
############

industries = f500["industry"]
industries_type = type(industries)

## 7. Selecting Columns from a DataFrame by Label Continued ##

##### instead of df.loc[:,["col1","col2"]], you can also use df[["col1", "col2"]] to select specific columns.
#############

countries = f500["country"]
revenues_years = f500[["revenues", "years_on_global_500_list"]]
ceo_to_sector = f500.loc[:,"ceo":"sector"]

## 8. Selecting Rows from a DataFrame by Label ##

toyota = f500.loc["Toyota Motor"]
drink_companies = f500.loc[["Anheuser-Busch InBev", "Coca-Cola", "Heineken Holding"]]
middle_companies = f500.loc["Tata Motors":"Nationwide", "rank":"country"]

## 10. Value Counts Method ##

## series and dataframes are two distinct objects, they have their own unique methods.
## Series.value_counts() method. This method displays each unique non-null value in a column and their counts in order.
## where series is the variable name of the series assignment
## e.g sectors = f500["sector"]
## sectors_value_counts = sectors.value_counts()
## print(sectors_value_counts)

countries = f500_sel["country"]
country_counts = countries.value_counts()

## 11. Selecting Items from a Series by Label ##

countries = f500['country']
countries_counts = countries.value_counts()

india = countries_counts["India"]
north_america = countries_counts[["USA", "Canada", "Mexico"]]

## 12. Summary Challenge ##

big_movers = f500.loc[["Aviva", "HP", "JD.com", "BHP Billiton"], ["rank","previous_rank"]]
bottom_companies = f500.loc["National Grid":"AutoNation", ["rank","sector","country"]]