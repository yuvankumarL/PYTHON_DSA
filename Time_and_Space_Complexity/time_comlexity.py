

#O(1)
print('hi')

#O(2)
print('hi')
print('Hello')

# O(10)
print('hi')
print('Hello')
print('hi')
print('Hello')
print('hi')
print('Hello')
print('hi')
print('Hello')
print('hi')
print('Hello')

"""still the above example is O(1) because we drop the constants"""

a = 10
b = 20
print(a + b)  # O(1)
print(a)  # O(1)

"""in the above example we have 3 O(1) operations so it is O(1) + O(1) = O() but we drop the constants so it is O(1)"""

# --------------------------------------------------------------------------------------------------------------------------------------------------

# O(n)
l = [1, 2, 3, 4, 5]
for i in l:
    print(i)
# Here we have O(n) operation because it depends on the size of the list, 
# if the size of the list increases the number of operations will also increase.
# O(n) + O(1) = O(n)

a=2
for i in l:
    if i==a:
        print('found')
        break

# here the operation breaks in second iteration so it is O(2) + O(1) = O(2) but we drop the constants so it is O(1)
# the above statement is wrong because in worst case the element may be at the end of the list or may not be present in the list

"""there are 3 cases in time complexity
1. Best Case: The best case is when the element is present at the first position of the list. 
    So the time complexity is O(1)
2. Average Case: The average case is when the element is present at the middle of the list. 
    So the time complexity is O(n/2) but we drop the constants so it is O(n)
3. Worst Case: The worst case is when the element is present at the last position of the list 
    or not present in the list. So the time complexity is O(n)"""

# So the time complexity of the above code is O(n)
# --------------------------------------------------------------------------------------------------------------------------------------------------

# O(log n)

# the programs solved using two pointer approach or binary search approach have time complexity of O(log n)
# and merge sort and quick sort also have time complexity of O(log n)

# binary search
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = 7
start = 0
end = len(l) - 1
while start <= end:  
    mid = (start + end) // 2
    if l[mid] == a:
        print('found')
        break
    elif l[mid] < a:
        start = mid + 1
    else:
        end = mid - 1
# Here the time complexity is O(log n) because in each iteration the size of the list is reduced to half.
# O(log n) + O(1) = O(log n)
# --------------------------------------------------------------------------------------------------------------------------------------------------

# O(n^2)
l = [1, 2, 3, 4, 5]
for i in l:
    for j in l:
        print(i, j)

# 5 the length of the list
# 5 * 5 = 25 operations
# Here the time complexity is O(n^2) because we have two nested loops.
# O(n^2) + O(1) = O(n^2)
# --------------------------------------------------------------------------------------------------------------------------------------------------


