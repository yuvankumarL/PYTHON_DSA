# Array
# Syntax -> array.array(typecode, [initializer])
# Typecode -> 'i' for integer, 'f' for float, 'd' for double, 'u' for unicode character
# Initializer -> optional, it is a list of initial values
from array import array

arr = array('i', [1, 2, 3, 4, 5]) # integer array
print(arr)  # array('i', [1, 2, 3, 4, 5])

arr = array('f', [1, 2, 3, 4, 5]) # float array
print(arr)  # array('f', [1.0, 2.0, 3.0, 4.0, 5.0])

arr = array('u', ['a', 'b', 'c', 'd', 'e']) # character array
print(arr)  # array('u', 'abcde')
# the ouput is in single quotes because it is a string

arr = array('d', [1, 2, 3, 4, 5]) # double array
print(arr)  # array('d', [1.0, 2.0, 3.0, 4.0, 5.0])
# double is same as float in python
# but in other languages like C, C++ double takes more memory than float
# so it is more precise than float

# Accessing elements
print(arr[0])  # 1.0
print(arr[1])  # 2.0
print(arr[2])  # 3.0
print(arr[3])  # 4.0
print(arr[4])  # 5.0    

# Inserting elements
arr.append(6)  # append adds element at the end
print(arr)  # array('d', [1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
arr.insert(0, 0)  # insert adds element at the specified index
print(arr)  # array('d', [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
arr.extend([7, 8, 9])  # extend adds multiple elements at the end
print(arr)  # array('d', [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])    
arr.fromlist([10, 11, 12])  # fromlist adds multiple elements at the end from a list
print(arr)  # array('d', [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0])

# Removing elements
arr.remove(0)  # remove removes the first occurrence of the specified value
print(arr)  # array('d', [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0])
arr.pop()  # pop removes the last element
print(arr)  # array('d', [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0])
arr.pop(0)  # pop removes the element at the specified index
print(arr)  # array('d', [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0])
arr.clear()  # clear removes all elements
print(arr)  # array('d')        

arr = array('d', [1, 2, 3, 4, 5]) # double array

# Searching elements
print(arr.index(1))  # 0
print(arr.index(2))  # 1
print(arr.index(3))  # 2
print(arr.index(4))  # 3    
print(arr.index(5))  # 4    
print(arr.count(1))  # 1
print(arr.count(2))  # 1
print(arr.count(3))  # 1
print(arr.count(4))  # 1
print(arr.count(5))  # 1
print(arr.count(6))  # 0   
# count returns the number of occurrences of the specified value
# if the value is not present it returns 0
# index returns the index of the first occurrence of the specified value
# if the value is not present it raises a ValueError
# so we can use try and except to handle the error
try:
    print(arr.index(6))  # ValueError
except ValueError:
    print("Value not found")  # Value not found 

for i in range(len(arr)):
    if arr[i] == 3:
        print("Found at index", i)  # Found at index 2
        break
# here we are searching for the value 3 in the array
# if we find it we print the index and break the loop
# if we don't find it the loop will run till the end
# so the time complexity of this search is O(n)


# Traversing elements
for i in arr:
    print(i)    
# 1.0
# 2.0
# 3.0       
# 4.0
# 5.0
# here we are traversing the array and printing each element
# so the time complexity of this traversal is O(n)
# we can also use while loop to traverse the array
i = 0
while i < len(arr):
    print(arr[i])
    i += 1
# 1.0
# 2.0
# 3.0       
# 4.0
# 5.0
# here we are traversing the array and printing each element
# so the time complexity of this traversal is O(n)  
# we can also use list comprehension to traverse the array
[print(i) for i in arr]
# 1.0
# 2.0
# 3.0       
# 4.0   
# 5.0
# here we are traversing the array and printing each element
# so the time complexity of this traversal is O(n)
# we can also convert the array to a list and then traverse the list
l = arr.tolist()
for i in l:
    print(i)
# 1.0   
# 2.0
# 3.0       
# 4.0
# 5.0
# here we are traversing the list and printing each element
# so the time complexity of this traversal is O(n)
# we can also use enumerate to traverse the array
for index, value in enumerate(arr):
    print(index, value)
# 0 1.0     
# 1 2.0
# 2 3.0       
# 3 4.0
# 4 5.0
# here we are traversing the array and printing the index and value of each element
# so the time complexity of this traversal is O(n)
# we can also use map to traverse the array 
list(map(print, arr))
# 1.0
# 2.0
# 3.0       
# 4.0       
# 5.0
# here we are traversing the array and printing each element
# so the time complexity of this traversal is O(n)
# we can also use filter to traverse the array
list(filter(lambda x: print(x), arr))
# 1.0
# 2.0
# 3.0       
# 4.0       
# 5.0   
# here we are traversing the array and printing each element
# so the time complexity of this traversal is O(n)
# we can also use reduce to traverse the array
from functools import reduce
reduce(lambda x, y: print(y) or y, arr)
# 1.0
# 2.0
# 3.0    
# 4.0 
# 5.0  
# here we are traversing the array and printing each element
# so the time complexity of this traversal is O(n)
# we can also use slicing to traverse the array
for i in arr[:]:
    print(i)
# 1.0
# 2.0
# 3.0   
# 4.0    
# 5.0
# here we are traversing the array and printing each element
# so the time complexity of this traversal is O(n)
# we can also use reversed to traverse the array in reverse order
for i in reversed(arr):
    print(i)
# 5.0
# 4.0
# 3.0       
# 2.0
# 1.0
# here we are traversing the array in reverse order and printing each element
# so the time complexity of this traversal is O(n)
# we can also use negative indexing to traverse the array in reverse order
for i in range(-1, -len(arr)-1, -1):
    print(arr[i])
# 5.0
# 4.0
# 3.0       
# 2.0
# 1.0
# here we are traversing the array in reverse order and printing each element
# so the time complexity of this traversal is O(n)  
# we can also use zip to traverse two arrays simultaneously
arr2 = array('d', [6, 7, 8, 9, 10])
for i, j in zip(arr, arr2): 
    print(i, j)
# 1.0 6.0
# 2.0 7.0
# 3.0 8.0    
# 4.0 9.0
# 5.0 10.0
# here we are traversing two arrays simultaneously and printing each element
# so the time complexity of this traversal is O(n)
# we can also use itertools to traverse the array

import numpy as np
np_arr = np.array(arr)
for i in np_arr:
    print(i)    

# 1.0
# 2.0
# 3.0       
# 4.0
# 5.0
# here we are traversing the numpy array and printing each element  
# so the time complexity of this traversal is O(n)
# we can also use pandas to traverse the array
import pandas as pd
pd_arr = pd.Series(arr)
for i in pd_arr:    
    print(i)
# 1.0
# 2.0
# 3.0       
# 4.0   
# 5.0
# here we are traversing the pandas series and printing each element
# so the time complexity of this traversal is O(n)
# we can also use itertools.cycle to traverse the array infinitely
# but we will limit the number of iterations to avoid infinite loop 
