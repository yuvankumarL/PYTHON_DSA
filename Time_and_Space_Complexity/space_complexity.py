
# Space Complexity
# Space complexity refers to the amount of memory an algorithm uses in relation to the size of the input data.
# It is usually expressed using Big O notation, which describes the upper bound of the memory usage as the input size grows.    \
# Space complexity is important because it helps us understand how much memory an algorithm will require to run, which can be a limiting factor in some applications.

# O(1) Constant Space Complexity
# An algorithm has a space complexity of O(1) if the amount of memory it uses
a = 10
# here a takes constant space, because it is a type of integer and it takes 4 bytes of memory
# if we change the value of a it will still take 4 bytes of memory
# so it is O(1)
# if its changed to a string it will take more memory but still it is O(1) because it takes constant space

#---------------------------------------------------------------------------------------------------------------------------------------------------

# O(n) Linear Space Complexity
# An algorithm has a space complexity of O(n) if the amount of memory it uses grows linearly with the size of the input data.
# For example, if an algorithm takes an array of size n as input and creates a new array of the same size, it has a space complexity
# of O(n) because the amount of memory it uses grows linearly with the size of the input array.
l = [1, 2, 3, 4, 5]
# here l takes linear space because it takes space according to the size of the list
# if we increase the size of the list the memory used will also increase
# so it is O(n)

#---------------------------------------------------------------------------------------------------------------------------------------------------

# O(n^2) Quadratic Space Complexity
# An algorithm has a space complexity of O(n^2) if the amount of memory it uses grows quadratically with the size of the input data.
# For example, if an algorithm takes an array of size n as input and creates a new 2D array of size n x n      
# (i.e., a matrix), it has a space complexity of O(n^2) because the amount of memory it uses grows quadratically with the size of the input array.
n = 5
matrix = [[0] * n for _ in range(n)]
# or
matrix = [[1, 2, 3, 4, 5],
          [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5]]

# here matrix takes quadratic space because it takes space according to the size of the list
# if we increase the size of the list the memory used will increase quadratically
# so it is O(n^2)   

# it works mostly of recursive programs
# example: calculating factorial of a number using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# here the space complexity is O(n) because it takes space according to the size of the recursion stack 
# so it is O(n^2) because in each recursion call it takes O(n) space
print(factorial(5))

# diagram for recursion stack
# factorial(5)
#     |
# factorial(4)
#     | 
# factorial(3)
#     |
# factorial(2)
#     |
# factorial(1)
#     |
# factorial(0)
#     |
# return 1
#     | return 1
# return 1 * 1 = 1
#     | return 2 * 1 = 2
# return 3 * 2 = 6
#     | return 4 * 6 = 24
# return 5 * 24 = 120
#     | return 120
print(factorial(5))  # 120

#---------------------------------------------------------------------------------------------------------------------------------------------------

# O(log n) Logarithmic Space Complexity
# An algorithm has a space complexity of O(log n) if the amount of memory it uses grows logarithmically with the size of the input data.
# For example, if an algorithm takes an array of size n as input and creates a new array of size log n, it has a space complexity of O(log n)
# because the amount of memory it uses grows logarithmically with the size of the input array.
# Algorithms that use a divide-and-conquer approach, such as binary search, often have a space complexity of O(log n).
def binary_search(arr, target):     
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
# here the space complexity is O(1) because it takes constant space
# so it is O(log n) because in each iteration the size of the list is reduced to half
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result = binary_search(arr, target)
if result != -1:
    print("Element found at index", result)
else:
    print("Element not found in array") 

# diagram for binary search
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# target = 7
# left = 0, right = 9
# mid = 4
# arr[mid] = 5 < target
# left = mid + 1 = 5, right = 9
# mid = 7
# arr[mid] = 8 > target
# left = 5, right = mid - 1 = 6
# mid = 5
# arr[mid] = 6 < target
# left = mid + 1 = 6, right = 6
# mid = 6
# arr[mid] = 7 == target
# return mid = 6    
#---------------------------------------------------------------------------------------------------------------------------------------------------

# Note: The space complexity of an algorithm can be affected by various factors, such as the data structures used, the input size, and the algorithm's design.
# It is important to analyze the space complexity of an algorithm to ensure that it can run efficiently within the available memory constraints.    
# In general, algorithms with lower space complexity are preferred, as they can handle larger input sizes and run more efficiently.

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# auxiliary space
# Auxiliary space is the extra space or temporary space used by an algorithm to solve a problem,
# excluding the space used by the input data. It is a measure of the additional memory required
# by an algorithm to perform its computations.
# Auxiliary space is important because it helps us understand the memory requirements of an algorithm beyond the input data.
# It is usually expressed using Big O notation, which describes the upper bound of the auxiliary space usage as the input size grows.
# For example, if an algorithm takes an array of size n as input and creates a new array of size n, it has an auxiliary space complexity of O(n)
# because it requires additional memory proportional to the size of the input array.
# On the other hand, if an algorithm takes an array of size n as input and uses only a constant amount of additional memory,
# it has an auxiliary space complexity of O(1).
# Auxiliary space is often used in recursive algorithms, where each recursive call requires additional memory on the call stack.
# It is also used in algorithms that create temporary data structures, such as arrays or linked lists, to store intermediate results.
# In general, algorithms with lower auxiliary space complexity are preferred, as they can handle larger input sizes and run more efficiently.
# Example:
def sum_of_array(arr):
    total = 0  # O(1) auxiliary space
    for num in arr:
        total += num
    return total
# Here, the auxiliary space used by the algorithm is O(1) because it uses a constant amount of additional memory (the variable 'total')
# regardless of the size of the input array
# So the auxiliary space complexity is O(1)
arr = [1, 2, 3, 4, 5]
print(sum_of_array(arr))  # Output: 15  

# here the space complexity is O(n) because it takes space according to the size of the list
# but the auxiliary space is O(1) because it uses a constant amount of additional memory

# another example
l = 10
k = []
for i in range(l):
    k.append(i)
print(k)
# here the space complexity is O(n) because it takes space according to the size of the list
# but the auxiliary space is O(n) because it uses additional memory proportional to the size of the input list  
# so the auxiliary space complexity is O(n)
# In summary, space complexity refers to the total amount of memory used by an algorithm, while auxiliary space refers to the additional memory used by an algorithm beyond the input data.
# Both space complexity and auxiliary space are important considerations when analyzing the efficiency of an algorithm, as
# they can impact the algorithm's ability to handle large input sizes and run efficiently within memory constraints.
# Algorithms with lower space complexity and auxiliary space complexity are generally preferred, as they can handle larger input sizes and run more efficiently.
# --------------------------------------------------------------------------------------------------------------------------------------------------

