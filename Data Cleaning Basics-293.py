## 1. Reading CSV Files with Encodings ##

#  try to read the file with the most popular encoding.
# UTF-8 has failed
import pandas as pd
laptops = pd.read_csv("laptops.csv", encoding="Latin-1")
laptops.info()

## 2. Cleaning Column Names ##

## se the DataFrame.columns attribute to remove whitespaces from the column names.

new_columns = []
for col in laptops.columns:
    # remove whitespace from the start and end of the string using str.strip() method
    # Append the updated column name to the new_columns list.
    cleaned_col = col.strip(" ")
    new_columns.append(cleaned_col)
    
# Assign the updated column names to the DataFrame.columns attribute.    
laptops.columns = new_columns
    

## 3. Cleaning Column Names Continued ##

import pandas as pd
laptops = pd.read_csv('laptops.csv', encoding='Latin-1')
## clean the column labels in our dataframe, adding a few extra cleaning 'chores' along the way.
def clean_col(col):
    col = col.strip()
    col = col.replace("Operating System","os")
    col = col.replace(" ","_")
    col = col.replace("(","")
    col = col.replace(")","")
    col = col.lower()
    return col

## loop through the columns to clean strings
new_columns = []
for c in laptops.columns:
    clean_c = clean_col(c)
    new_columns.append(clean_c)

laptops.columns = new_columns
print(laptops.columns)

## 4. Converting String Columns to Numeric ##

# Converting String Columns to Numeric
# identify the unique values in the ram column of the laptops dataframe
unique_ram = laptops["ram"].unique()

## 5. Removing Non-Digit Characters ##

# 5. Removing Non-Digit Characters
#The pandas library contains dozens of vectorized string methods we can use to manipulate text data, many of which perform the same operations as Python string methods. Most vectorized string methods are available using the Series.str accessor, which means we can access them by adding str between the series name and the method name:
#    we can use the Series.str.replace() method, which is a vectorized version of the Python str.replace() method we used in the previous screen, to remove all the quote characters from every string

laptops["ram"] = laptops["ram"].str.replace("GB","")
unique_ram = laptops["ram"].unique()

## 6. Converting Columns to Numeric Dtypes ##

laptops["ram"] = laptops["ram"].str.replace('GB','')

## 6. Converting Columns to Numeric dtypes
## Now, we can convert (or cast) the columns to a numeric dtype.
## To do this, we use the Series.astype() method. To convert the column to a numeric dtype, we can use either int or float as the parameter for the method.
## Use the Series.astype() method to change the ram column to an integer dtype.
laptops["ram"] = laptops["ram"].astype(int)
dtypes = laptops.dtypes

## 7. Renaming Columns ##

laptops["ram"] = laptops["ram"].str.replace('GB','').astype(int)

# To stop us from losing information that helps us understand the data, we can use the DataFrame.rename() method to rename the column from screen_size to screen_size_inches
# specify the axis=1 parameter so pandas knows that we want to rename labels in the column axis:
# e.g. laptops.rename({"screen_size": "screen_size_inches"}, axis=1, inplace=True)
## Note that we can either use inplace=True or assign the result back to the dataframe - both will give us the same results.

# rename the ram column next and analyze the results.
laptops.rename({"ram": "ram_gb"}, axis=1, inplace=True)
ram_gb_desc = laptops["ram_gb"].describe()

## 8. Extracting Values from Strings ##

laptops["gpu_manufacturer"] = (laptops["gpu"]
                                       .str.split()
                                       .str[0]
                              )
laptops["cpu_manufacturer"] = (laptops["cpu"]
                                       .str.split()
                                       .str[0]
                               )
cpu_manufacturer_counts = laptops["cpu_manufacturer"].value_counts()

## 9. Correcting Bad Values ##

# WE can fix inconsistent data issues which may result from manual data entry or if data was scraped from the web.
## To fix this inconsistency: 
## One way we can fix this is with the Series.map() method. The Series.map() method is ideal when we want to change multiple values in a column, but we'll use it now as an opportunity to learn how the method works.

# The most common way to use Series.map() is with a dictionary.

mapping_dict = {
    'Android': 'Android',
    'Chrome OS': 'Chrome OS',
    'Linux': 'Linux',
    'Mac OS': 'macOS',
    'No OS': 'No OS',
    'Windows': 'Windows',
    'macOS': 'macOS'
}

laptops["os"] = laptops["os"].map(mapping_dict)

## 10. Dropping Missing Values ##

# 10. Dropping Missing Values
## we can use the DataFrame.isnull() method to identify missing values, which returns a boolean dataframe. We can then use the DataFrame.sum() method to give us a count of the True values for each column:
# print(laptops.isnull().sum())
## The DataFrame.dropna() method accepts an axis parameter, which indicates whether we want to drop along the column or index axis

laptops_no_null_rows = laptops.dropna(axis=0)
laptops_no_null_cols = laptops.dropna(axis=1)

## 11. Filling Missing Values ##

value_counts_before = laptops.loc[laptops["os_version"].isnull(), "os"].value_counts()
laptops.loc[laptops["os"] == "macOS", "os_version"] = "X"
laptops.loc[laptops["os"] == "No OS", "os_version"] = "Version Unknown"
value_counts_after = laptops.loc[laptops["os_version"].isnull(), "os"].value_counts()

## 12. Challenge: Clean a String Column ##

# Explore the data
#Identify patterns and special cases
# print(laptops["weight"].unique())

# Remove non-digit characters
# convert the column to a numeric dtype
laptops["weight"] = laptops["weight"].str.replace("kgs","").str.replace("kg","").astype(float)

#Rename the weight column to weight_kg.
laptops.rename({"weight": "weight_kg"}, axis=1, inplace=True)

#Use the DataFrame.to_csv() method to save the laptops dataframe to a CSV file laptops_cleaned.csv without index labels.
laptops.to_csv('laptops_cleaned.csv',index=False)