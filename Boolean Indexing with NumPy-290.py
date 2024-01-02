## 1. Reading CSV files with NumPy ##

import numpy as np
taxi = np.genfromtxt('nyc_taxis.csv', delimiter=',')
taxi_shape = taxi.shape

## 2. Reading CSV Files with NumPy Continued ##

import numpy as np

# read file into numpy
taxi = np.genfromtxt('nyc_taxis.csv', delimiter=',', skip_header=1)
taxi_shape = taxi.shape

## 3. Boolean Arrays ##

a = np.array([1, 2, 3, 4, 5])
b = np.array(["blue", "blue", "red", "blue"])
c = np.array([80.0, 103.4, 96.9, 200.3])

# do some vectorized Boolean to compare values
a_bool = a < 3
b_bool = b == "blue"
c_bool = c > 100

## 4. Boolean Indexing with 1D ndarrays ##

pickup_month = taxi[:,1]

january_bool = pickup_month == 1
january = pickup_month[january_bool]
january_rides = january.shape[0]

# determine the number of rides in our data set for February using Boolean indexing
february_bool = pickup_month == 2
february = pickup_month[february_bool]
february_rides = february.shape[0]

## 5. Boolean Indexing with 2D ndarrays ##

tip_amount = taxi[:,12]
# xamine the rows that have the highest values for the tip_amount column
tip_bool = tip_amount > 50
top_tips = taxi[tip_bool, 5:14]
print(top_tips)

## 6. Assigning Values in ndarrays ##

# this creates a copy of our taxi ndarray
taxi_modified = taxi.copy()

#################################
# practice some array assignments with our taxi dataset
# practice without making changes to our original array, we have used the ndarray.copy() method to make taxi_modified, a copy of our original for these exercises. 
#################################

taxi_modified[1066,5] = 1
taxi_modified[:,0] = 16
taxi_modified[550:552,7] = taxi_modified[:,7].mean()

## 7. Assignment Using Boolean Arrays ##

# this creates a copy of our taxi ndarray
taxi_copy = taxi.copy()

# boolean assignment
total_amount = taxi_copy[:,13]
taxi_copy[total_amount < 0] = 0

## 8. Assignment Using Boolean Arrays Continued ##

# create a new column filled with `0`.
zeros = np.zeros([taxi.shape[0], 1])
taxi_modified = np.concatenate([taxi, zeros], axis=1)
print(taxi_modified)
# assignment using boolean arrays

taxi_modified[taxi_modified[:, 5] == 2, 15] = 1
taxi_modified[taxi_modified[:, 5] == 3, 15] = 1
taxi_modified[taxi_modified[:, 5] == 5, 15] = 1

## 9. Challenge: Which Is the Most Popular Airport? ##

##############
# use Boolean indexing to create three filtered arrays and then look at how many rows are in each array.
#############

"""
check if the dropoff_location_code column (column index 6) is equal to one of the following values:

2: JFK Airport
3: LaGuardia Airport
5: Newark Airport.
"""
## array[array[:, column_for_comparison] == value_for_comparison, column_for_assignment] = new_value ##

jfk = taxi[taxi[:,6] == 2]
jfk_count = jfk.shape[0]
laguardia = taxi[taxi[:,6] == 3]
laguardia_count = laguardia.shape[0]
newark = taxi[taxi[:,6] == 5]
newark_count = newark.shape[0]

## 10. Challenge: Calculating Statistics for Trips on Clean Data ##

trip_mph = taxi[:,7] / (taxi[:,8] / 3600)
##
# removing potentially bad data from our data set, and then calculating some descriptive statistics on the remaining "clean" data.
##

#############################
# using Boolean indexing to remove any rows that have an average speed for the trip greater than 100 mph (160 kph) which should remove any questionable data. Then, we'll use array methods to calculate the mean for specific columns of the remaining data. Here are the columns we're interested in:

# trip_distance, at column index 7
# trip_length, at column index 8
# total_amount, at column index 13

######################

# use Boolean indexing to filter out/clean data.
# Rid the dataset of trip speed > 100
cleaned_taxi = taxi[trip_mph < 100]
mean_distance = cleaned_taxi[:,7].mean()
mean_length = cleaned_taxi[:,8].mean()
mean_total_amount = cleaned_taxi[:,13].mean()