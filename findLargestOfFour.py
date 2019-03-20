# Returning an array consisting of the largest number from each provided sub-array. For simplicity, the provided array will contain exactly 4 sub-arrays.
from array import *


arr = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]

def largestOfFourSubArrays(arr):
    final_result = []

    for subArray in arr:    # looping through the sub arrays contained in the array
        largestNumber = 0
        for index in subArray:      # iterating through the sub array indices
            if index > largestNumber:
                largestNumber = index
        final_result.append(largestNumber)   # appending each of the largest no. contained in the sub array
    print(final_result)

largestOfFourSubArrays(arr)

