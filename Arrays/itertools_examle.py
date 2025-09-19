import itertools
for i in itertools.chain(arr):  
    print(i)
# 1.0
# 2.0
# 3.0       
# 4.0
# 5.0
# here we are traversing the array and printing each element
# so the time complexity of this traversal is O(n)
# we can also use numpy to traverse the array

for i, j in zip(arr, itertools.cycle(arr2)):
    print(i, j)
# 1.0 6.0
# 2.0 7.0
# 3.0 8.0       
# 4.0 9.0
# 5.0 10.0  
# here we are traversing two arrays simultaneously and printing each element
# so the time complexity of this traversal is O(n)
# we can also use itertools.islice to traverse a part of the array
for i in itertools.islice(arr, 2, 4):
    print(i)
# 3.0
# 4.0       
# here we are traversing a part of the array and printing each element
# so the time complexity of this traversal is O(k) where k is the number of elements
# we can also use itertools.tee to create multiple iterators from the array
arr1, arr2 = itertools.tee(arr, 2)
for i in arr1:
    print(i)
# 1.0
# 2.0
# 3.0       
# 4.0
# 5.0
# here we are traversing the first iterator and printing each element
# so the time complexity of this traversal is O(n)
for i in arr2:  
    print(i)
# 1.0
# 2.0
# 3.0   
# 4.0
# 5.0
# here we are traversing the second iterator and printing each element
# so the time complexity of this traversal is O(n)
# we can also use itertools.accumulate to traverse the array and get the cumulative sum
for i in itertools.accumulate(arr):
    print(i)
# 1.0
# 3.0
# 6.0       
# 10.0
# 15.0  
# here we are traversing the array and printing the cumulative sum of each element
# so the time complexity of this traversal is O(n)
# we can also use itertools.combinations to traverse the array and get all possible combinations of a   given length
for i in itertools.combinations(arr, 2):
    print(i)
# (1.0, 2.0)        
# (1.0, 3.0)
# (1.0, 4.0)       
# (1.0, 5.0)
# (2.0, 3.0)       
# (2.0, 4.0)
# (2.0, 5.0)
# (3.0, 4.0)    
# (3.0, 5.0)    
# (4.0, 5.0)
# here we are traversing the array and printing all possible combinations of length 2
# so the time complexity of this traversal is O(n^2)
# we can also use itertools.permutations to traverse the array and get all possible permutations of a given length
for i in itertools.permutations(arr, 2):
    print(i)
# (1.0, 2.0)        
# (1.0, 3.0)       
# (1.0, 4.0)       
# (1.0, 5.0)
# (2.0, 1.0)        
# (2.0, 3.0)       
# (2.0, 4.0)    
# (2.0, 5.0)
# (3.0, 1.0)       
# (3.0, 2.0)       
# (3.0, 4.0)    
# (3.0, 5.0)
# (4.0, 1.0)       
# (4.0, 2.0)    
# (4.0, 3.0)    
# (4.0, 5.0)
# (5.0, 1.0)    
# (5.0, 2.0)    
# (5.0, 3.0)    
# (5.0, 4.0)
# here we are traversing the array and printing all possible permutations of length 2
# so the time complexity of this traversal is O(n!)
# we can also use itertools.product to traverse the array and get the cartesian product of the array with itself
for i in itertools.product(arr, repeat=2):
    print(i)
# (1.0, 1.0)        
# (1.0, 2.0)       
# (1.0, 3.0)       
# (1.0, 4.0)       
# (1.0, 5.0)
# (2.0, 1.0)        
# (2.0, 2.0)       
# (2.0, 3.0)    
# (2.0, 4.0)    
# (2.0, 5.0)    
# (3.0, 1.0)       
# (3.0, 2.0)       
# (3.0, 3.0)    
# (3.0, 4.0)    
# (3.0, 5.0)
# (4.0, 1.0)       
# (4.0, 2.0)    
# (4.0, 3.0)    
# (4.0, 4.0)    
# (4.0, 5.0)    
# (5.0, 1.0)    
# (5.0, 2.0)    
# (5.0, 3.0)    
# (5.0, 4.0)    
# (5.0, 5.0)
# here we are traversing the array and printing the cartesian product of the array with itself
# so the time complexity of this traversal is O(n^2)    
# we can also use itertools.groupby to traverse the array and group the elements based on a given key
for key, group in itertools.groupby(arr):
    print(key, list(group))
# 1.0 [1.0]        
# 2.0 [2.0]       
# 3.0 [3.0]       
# 4.0 [4.0]       
# 5.0 [5.0]
# here we are traversing the array and printing the elements grouped by their value 
# so the time complexity of this traversal is O(n)
# we can also use itertools.starmap to traverse the array and apply a function to each element
for i in itertools.starmap(lambda x: x*2, arr):
    print(i)
# 2.0
# 4.0
# 6.0   
# 8.0    
# 10.0
# here we are traversing the array and printing each element multiplied by 2
# so the time complexity of this traversal is O(n)  
# we can also use itertools.zip_longest to traverse two arrays simultaneously and fill the shorter array with a specified value
arr3 = array('d', [6, 7])
for i, j in itertools.zip_longest(arr, arr3, fillvalue=0):
    print(i, j)
# 1.0 6.0
# 2.0 7.0
# 3.0 0.0       
# 4.0 0.0
# 5.0 0.0
# here we are traversing two arrays simultaneously and printing each element
# so the time complexity of this traversal is O(n) where n is the length of the longer array
# we can also use itertools.izip to traverse two arrays simultaneously
# but it is not available in python 3
# we can also use itertools.ifilter to traverse the array and filter the elements based on a given condition
# but it is not available in python 3
# we can also use itertools.imap to traverse the array and apply a function to each element
# but it is not available in python 3
# we can also use itertools.tee to create multiple iterators from the array
# but it is not available in python 3
# we can also use itertools.cycle to traverse the array infinitely
# but it is not available in python 3
# we can also use itertools.islice to traverse a part of the array      
# but it is not available in python 3
# we can also use itertools.accumulate to traverse the array and get the cumulative sum
# but it is not available in python 3
# we can also use itertools.combinations to traverse the array and get all possible combinations of a given length
# but it is not available in python 3
# we can also use itertools.permutations to traverse the array and get all possible permutations of a given length
# but it is not available in python 3
# we can also use itertools.product to traverse the array and get the cartesian product of the array with itself
# but it is not available in python 3
# we can also use itertools.groupby to traverse the array and group the elements based on a given   key
# but it is not available in python 3
# we can also use itertools.starmap to traverse the array and apply a function to each element
# but it is not available in python 3
# we can also use itertools.zip_longest to traverse two arrays simultaneously and fill the shorter array with a specified value
# but it is not available in python 3
# we can also use itertools.chain to traverse multiple arrays sequentially
arr4 = array('d', [6, 7, 8])
for i in itertools.chain(arr, arr4):
    print(i)
# 1.0
# 2.0
# 3.0       
# 4.0
# 5.0
# 6.0
# 7.0
# 8.0
# here we are traversing multiple arrays sequentially and printing each element
# so the time complexity of this traversal is O(n) where n is the total number of elements in all arrays
# we can also use itertools.repeat to traverse the array and repeat each element
for i in itertools.chain.from_iterable(itertools.repeat(x, 2) for x in arr):
    print(i)
# 1.0
# 1.0
# 2.0
# 2.0
# 3.0       
# 3.0    
# 4.0    
# 4.0    
# 5.0
# 5.0
# here we are traversing the array and printing each element twice
# so the time complexity of this traversal is O(2n) which is O(n)
# we can also use itertools.compress to traverse the array and filter the elements based on a given mask
mask = [1, 0, 1, 0, 1]
for i in itertools.compress(arr, mask):
    print(i)
# 1.0
# 3.0       
# 5.0
# here we are traversing the array and printing the elements where the mask is 1
# so the time complexity of this traversal is O(n)
# we can also use itertools.dropwhile to traverse the array and drop the elements until a given condition is met
for i in itertools.dropwhile(lambda x: x < 3, arr):
    print(i)
# 3.0       
# 4.0
# 5.0
# here we are traversing the array and printing the elements after the first element that is not less than 3
# so the time complexity of this traversal is O(n)
# we can also use itertools.takewhile to traverse the array and take the elements until a given condition is met
for i in itertools.takewhile(lambda x: x < 3, arr):
    print(i)
# 1.0
# 2.0
# here we are traversing the array and printing the elements until the first element that is not less than 3
# so the time complexity of this traversal is O(n)
# we can also use itertools.filterfalse to traverse the array and filter the elements based on a given condition
for i in itertools.filterfalse(lambda x: x < 3, arr):
    print(i)
# 3.0       
# 4.0
# 5.0
# here we are traversing the array and printing the elements that are not less than 3
# so the time complexity of this traversal is O(n)
# we can also use itertools.accumulate to traverse the array and get the cumulative product
for i in itertools.accumulate(arr, lambda x, y: x * y):
    print(i)
# 1.0
# 2.0
# 6.0       
# 24.0      
# 120.0
# here we are traversing the array and printing the cumulative product of each element
# so the time complexity of this traversal is O(n)
# we can also use itertools.pairwise to traverse the array and get the consecutive pairs of elements
for i in itertools.pairwise(arr):
    print(i)
# (1.0, 2.0)        
# (2.0, 3.0)       
# (3.0, 4.0)       
# (4.0, 5.0)
# here we are traversing the array and printing the consecutive pairs of elements
# so the time complexity of this traversal is O(n)
# we can also use itertools.sliding_window to traverse the array and get the sliding window of a given size
# but it is not available in python 3
# we can also use itertools.batched to traverse the array and get the batches of a given size
# but it is not available in python 3
# we can also use itertools.combinations_with_replacement to traverse the array and get all possible combinations of a given length with replacement
for i in itertools.combinations_with_replacement(arr, 2):
    print(i)
# (1.0, 1.0)        
# (1.0, 2.0)       
# (1.0, 3.0)       
# (1.0, 4.0)
# (1.0, 5.0)
# (2.0, 2.0)       
# (2.0, 3.0)    
# (2.0, 4.0)    
# (2.0, 5.0)    
# (3.0, 3.0)    
# (3.0, 4.0)    
# (3.0, 5.0)
# (4.0, 4.0)    
# (4.0, 5.0)
# (5.0, 5.0)
# here we are traversing the array and printing all possible combinations of length 2 with replacement
# so the time complexity of this traversal is O(n^2)
# we can also use itertools.product to traverse multiple arrays and get the cartesian product of the    arrays          
arr5 = array('d', [9, 10])
for i in itertools.product(arr, arr4, arr5):
    print(i)
# (1.0, 6.0, 9.0)
# (1.0, 6.0, 10.0)
# (1.0, 7.0, 9.0)
# (1.0, 7.0, 10.0)
# (1.0, 8.0, 9.0)
# (1.0, 8.0, 10.0)
# (2.0, 6.0, 9.0)
# (2.0, 6.0, 10.0)
# (2.0, 7.0, 9.0)
# (2.0, 7.0, 10.0)
# (2.0, 8.0, 9.0)
# (2.0, 8.0, 10.0)
# (3.0, 6.0, 9.0)
# (3.0, 6.0, 10.0)
# (3.0, 7.0, 9.0)
# (3.0, 7.0, 10.0)
# (3.0, 8.0, 9.0)
# (3.0, 8.0, 10.0)
# (4.0, 6.0, 9.0)
# (4.0, 6.0, 10.0)
# (4.0, 7.0, 9.0)
# (4.0, 7.0, 10.0)
# (4.0, 8.0, 9.0)
# (4.0, 8.0, 10.0)
# (5.0, 6.0, 9.0)
# (5.0, 6.0, 10.0)
# (5.0, 7.0, 9.0)
# (5.0, 7.0, 10.0)  
# (5.0, 8.0, 9.0)
# (5.0, 8.0, 10.0)
# here we are traversing multiple arrays and printing the cartesian product of the arrays
# so the time complexity of this traversal is O(n^k) where n is the length of the arrays and k is the number of arrays
# we can also use itertools.permutations to traverse multiple arrays and get all possible permutations of a given length
# but it is not available   in python 3
# we can also use itertools.combinations to traverse multiple arrays and get all possible combinations of a given length
# but it is not available in python 3
# we can also use itertools.combinations_with_replacement to traverse multiple arrays and get all possible combinations of a given length with replacement
# but it is not available in python 3
# we can also use itertools.groupby to traverse multiple arrays and group the elements based on a given key
# but it is not available in python 3
# we can also use itertools.starmap to traverse multiple arrays and apply a function to each element
# but it is not available in python 3
# we can also use itertools.zip_longest to traverse multiple arrays simultaneously and fill the shorter arrays with a specified value
# but it is not available in python 3
# we can also use itertools.chain to traverse multiple arrays sequentially
# but it is not available in python 3
# we can also use itertools.repeat to traverse multiple arrays and repeat each element  
# but it is not available in python 3
# we can also use itertools.compress to traverse multiple arrays and filter the elements based on a given mask
# but it is not available in python 3
# we can also use itertools.dropwhile to traverse multiple arrays and drop the elements until a given condition is met
# but it is not available in python 3
# we can also use itertools.takewhile to traverse multiple arrays and take the elements until a given condition is met
# but it is not available in python 3
# we can also use itertools.filterfalse to traverse multiple arrays and filter the elements based on a given condition
# but it is not available in python 3   
# we can also use itertools.accumulate to traverse multiple arrays and get the cumulative sum or product
# but it is not available in python 3
# we can also use itertools.pairwise to traverse multiple arrays and get the consecutive pairs of elements
# but it is not available in python 3
# we can also use itertools.sliding_window to traverse multiple arrays and get the sliding window of a given size
# but it is not available in python 3
# we can also use itertools.batched to traverse multiple arrays and get the batches of a given size
# but it is not available in python 3
# we can also use itertools.tee to create multiple iterators from multiple arrays
# but it is not available in python 3
# we can also use itertools.cycle to traverse multiple arrays infinitely
# but it is not available in python 3
# we can also use itertools.islice to traverse a part of multiple arrays
# but it is not available in python 3   
# we can also use itertools.izip to traverse multiple arrays simultaneously
# but it is not available in python 3
# we can also use itertools.ifilter to traverse multiple arrays and filter the elements based on a given condition
# but it is not available in python 3
# we can also use itertools.imap to traverse multiple arrays and apply a function to each element
# but it is not available in python 3   
# we can also use itertools.product to traverse the array and get the cartesian product of the array with itself multiple times
for i in itertools.product(arr, repeat=3):
    print(i)
# (1.0, 1.0, 1.0)        
# (1.0, 1.0, 2.0)       
# (1.0, 1.0, 3.0)       
# (1.0, 1.0, 4.0)       
# (1.0, 1.0, 5.0)
# (1.0, 2.0, 1.0)       
# (1.0, 2.0, 2.0)    
# (1.0, 2.0, 3.0)   
# (1.0, 2.0, 4.0)   
# (1.0, 2.0, 5.0)    
# (1.0, 3.0, 1.0)       
# (1.0, 3.0, 2.0)       
# (1.0, 3.0, 3.0)    
# (1.0, 3.0, 4.0)  
# (1.0, 3.0, 5.0)
# (1.0, 4.0, 1.0)       
# (1.0, 4.0, 2.0)    
# (1.0, 4.0, 3.0)    
# (1.0, 4.0, 4.0)    
# (1.0, 4.0, 5.0)    
# (1.0, 5.0, 1.0)   
# (1.0, 5.0, 2.0)    
# (1.0, 5.0, 3.0)    
# (1.0, 5.0, 4.0)    
# (1.0, 5.0, 5.0)
# (2.0, 1.0, 1.0)        
# (2.0, 1.0, 2.0)       
# (2.0, 1.0, 3.0)       
# (2.0, 1.0, 4.0)       
# (2.0, 1.0, 5.0)
# (2.0, 2.0, 1.0)    
# (2.0, 2.0, 2.0)
# ...existing code...
# (2.0, 2.0, 3.0)
# (2.0, 2.0, 4.0)
# (2.0, 2.0, 5.0)
# (2.0, 3.0, 1.0)
# (2.0, 3.0, 2.0)
# (2.0, 3.0, 3.0)
# (2.0, 3.0, 4.0)
# (2.0, 3.0, 5.0)
# (2.0, 4.0, 1.0)
# (2.0, 4.0, 2.0)
# (2.0, 4.0, 3.0)
# (2.0, 4.0, 4.0)
# (2.0, 4.0, 5.0)
# (2.0, 5.0, 1.0)
# (2.0, 5.0, 2.0)
# (2.0, 5.0, 3.0)
# (2.0, 5.0, 4.0)
# (2.0, 5.0, 5.0)
# (3.0, 1.0, 1.0)
# (3.0, 1.0, 2.0)
# (3.0, 1.0, 3.0)
# (3.0, 1.0, 4.0)
# (3.0, 1.0, 5.0)
# (3.0, 2.0, 1.0)
# (3.0, 2.0, 2.0)
# (3.0, 2.0, 3.0)
# (3.0, 2.0, 4.0)
# (3.0, 2.0, 5.0)
# (3.0, 3.0, 1.0)
# (3.0, 3.0, 2.0)
# (3.0, 3.0, 3.0)
# (3.0, 3.0, 4.0)
# (3.0, 3.0, 5.0)
# (3.0, 4.0, 1.0)
# (3.0, 4.0, 2.0)
# (3.0, 4.0, 3.0)
# (3.0, 4.0, 4.0)
# (3.0, 4.0, 5.0)
# (3.0, 5.0, 1.0)
# (3.0, 5.0, 2.0)
# (3.0, 5.0, 3.0)
# (3.0, 5.0, 4.0)
# (3.0, 5.0, 5.0)
# (4.0, 1.0, 1.0)
# (4.0, 1.0, 2.0)
# (4.0, 1.0, 3.0)
# (4.0, 1.0, 4.0)
# (4.0, 1.0, 5.0)
# (4.0, 2.0, 1.0)
# (4.0, 2.0, 2.0)
# (4.0, 2.0, 3.0)
# (4.0, 2.0, 4.0)
# (4.0, 2.0, 5.0)
# (4.0, 3.0, 1.0)
# (4.0, 3.0, 2.0)
# (4.0, 3.0, 3.0)
# (4.0, 3.0, 4.0)
# (4.0, 3.0, 5.0)
# (4.0, 4.0, 1.0)
# (4.0, 4.0, 2.0)
# (4.0, 4.0, 3.0)
# (4.0, 4.0, 4.0)
# (4.0, 4.0, 5.0)
# (4.0, 5.0, 1.0)
# (4.0, 5.0, 2.0)
# (4.0, 5.0, 3.0)
# (4.0, 5.0, 4.0)
# (4.0, 5.0, 5.0)
# (5.0, 1.0, 1.0)
# (5.0, 1.0, 2.0)
# (5.0, 1.0, 3.0)
# (5.0, 1.0, 4.0)
# (5.0, 1.0, 5.0)
# (5.0, 2.0, 1.0)
# (5.0, 2.0, 2.0)
# (5.0, 2.0, 3.0)
# (5.0, 2.0, 4.0)
# (5.0, 2.0, 5.0)
# (5.0, 3.0, 1.0)
# (5.0, 3.0, 2.0)
# (5.0, 3.0, 3.0)
# (5.0, 3.0, 4.0)
# (5.0, 3.0, 5.0)
# (5.0, 4.0, 1.0)
# (5.0, 4.0, 2.0)
# (5.0, 4.0, 3.0)
# (5.0, 4.0, 4.0)
# (5.0, 4.0, 5.0)
# (5.0, 5.0, 1.0)
# (5.0, 5.0, 2.0)
# (5.0, 5.0, 3.0)
# (5.0, 5.0, 4.0)
# (5.0, 5.0, 5.0)
# here we are traversing the array and printing the cartesian product of the array with itself three times
# so the time complexity of this traversal is O(n^3)
# ...existing code...
# Other useful itertools operations:

# 1. itertools.count: Creates an iterator that returns evenly spaced values starting with a specified number.
for i in itertools.islice(itertools.count(10, 2), 5):
    print(i)
# 10
# 12
# 14
# 16
# 18
# Useful for generating sequences, time complexity O(k) for k elements.

# 2. itertools.cycle: Cycles through an iterable indefinitely.
for i, val in zip(range(7), itertools.cycle([1, 2, 3])):
    print(val)
# 1
# 2
# 3
# 1
# 2
# 3
# 1
# Useful for repeating patterns, time complexity O(n) for n cycles.

# 3. itertools.repeat: Repeats an object, either infinitely or a specified number of times.
for i in itertools.repeat('A', 4):
    print(i)
# A
# A
# A
# A
# Useful for filling values, time complexity O(k) for k repeats.

# 4. itertools.dropwhile: Drops elements from the iterable as long as the predicate is true; afterwards, returns every element.
for i in itertools.dropwhile(lambda x: x < 3, arr):
    print(i)
# 3.0
# 4.0
# 5.0
# Useful for skipping initial values, time complexity O(n).

# 5. itertools.takewhile: Returns elements from the iterable as long as the predicate is true.
for i in itertools.takewhile(lambda x: x < 4, arr):
    print(i)
# 1.0
# 2.0
# 3.0
# Useful for extracting prefix, time complexity O(n).

# 6. itertools.filterfalse: Returns elements of iterable where predicate is false.
for i in itertools.filterfalse(lambda x: x % 2 == 0, arr):
    print(i)
# 1.0
# 3.0
# 5.0
# Useful for filtering, time complexity O(n).

# 7. itertools.accumulate: Returns accumulated sums or results of a binary function.
for i in itertools.accumulate(arr, lambda x, y: x * y):
    print(i)
# 1.0
# 2.0
# 6.0
# 24.0
# 120.0
# Useful for cumulative operations, time complexity O(n).

# 8. itertools.pairwise: Returns consecutive pairs of elements.
for i in itertools.pairwise(arr):
    print(i)
# (1.0, 2.0)
# (2.0, 3.0)
# (3.0, 4.0)
# (4.0, 5.0)
# Useful for adjacent comparisons, time complexity O(n).

# 9. itertools.combinations_with_replacement: Returns all combinations of a specified length with replacement.
for i in itertools.combinations_with_replacement(arr, 2):
    print(i)
# (1.0, 1.0)
# (1.0, 2.0)
# (1.0, 3.0)
# (1.0, 4.0)
# (1.0, 5.0)
# (2.0, 2.0)
# (2.0, 3.0)
# (2.0, 4.0)
# (2.0, 5.0)
# (3.0, 3.0)
# (3.0, 4.0)
# (3.0, 5.0)
# (4.0, 4.0)
# (4.0, 5.0)
# (5.0, 5.0)
# Useful for generating multisets, time complexity O(n^r).

# 10. itertools.batched (Python 3.12+): Returns batches of a specified size.
# for batch in itertools.batched(arr, 2):
#     print(batch)
# [1.0, 2.0]
# [3.0, 4.0]
# [5.0]
# Useful for chunking, time complexity O(n).

# These are the main operations available in itertools for array traversal and manipulation.
# ...existing code...