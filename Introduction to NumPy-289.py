## 2. Introduction to Ndarrays ##

import numpy as np
data_ndarray = np.array([10, 20, 30])

## 4. NYC Taxi-Airport Data ##

import csv
import numpy as np

# import nyc_taxi.csv as a list of lists
f = open("nyc_taxis.csv", "r")
taxi_list = list(csv.reader(f))

# remove the header row
taxi_list = taxi_list[1:]

# convert all values to floats
converted_taxi_list = []
for row in taxi_list:
    converted_row = []
    for item in row:
        converted_row.append(float(item))
    converted_taxi_list.append(converted_row)

# start writing your code below this comment
# use the numpy.array() constructor to convert the lists
taxi = np.array(converted_taxi_list)

## 5. Array Shapes ##

taxi_shape = taxi.shape
print(taxi_shape)

## 6. Selecting and Slicing Rows and Items from Ndarrays ##

# using the ndarray to select row or column in the data table

row_0 = taxi[0]

# slicing in ndarray is like lists
## takes the first specified item but does not include the last
## columns for the rows at indices 391 to 500 inclusive
rows_391_to_500 = taxi[391:501]

# item at row index 21 and column index 5
row_21_column_5 = taxi[21,5]

## 7. Selecting Columns and Custom Slicing Ndarrays ##

## practising selecting columns using numpy ndarray
colns = [1,4,7]
columns_1_4_7 = taxi[:,colns]


row_99_columns_5_to_8 = taxi[99,5:9]

rows_100_to_200_column_14 = taxi[100:201,14]

## 8. Vector Math ##

fare_amount = taxi[:,9]
fees_amount = taxi[:,10]

# use vector to add fare amount and fees_amount

fare_and_fees = fare_amount + fees_amount

## 9. Vector Math (Continued) ##

trip_distance_miles = taxi[:,7]
trip_length_seconds = taxi[:,8]

trip_length_hours = trip_length_seconds / 3600 # 3600 seconds is one hour

# perform vector division again to calculate the miles per hour.
trip_mph = trip_distance_miles / trip_length_hours

## 10. Calculating Statistics for 1D Ndarrays ##

mph_min = trip_mph.min()

# calculate the maximum and mean (average) speed from our trip_mph ndarray
mph_max = trip_mph.max()
mph_mean = trip_mph.mean()

## 12. Calculating Statistics for 2D Ndarrays ##

# we'll compare against the first 5 rows only
taxi_first_five = taxi[:5]
# select these columns: fare_amount, fees_amount, tolls_amount, tip_amount
fare_components = taxi_first_five[:,9:13]

# Check if the sum of each row in fare_components equals the value in the total_amount column.
fare_sums = fare_components.sum(axis=1)

# Extract the 14th column in the taxi_first_five
fare_totals = taxi_first_five[:,13]

print(fare_totals, fare_sums)