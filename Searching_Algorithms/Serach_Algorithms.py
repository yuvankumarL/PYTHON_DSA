

class SearchingAlgorithms:

    def linear_search(self, arr, target):
        """
        Perform a linear search for the target in the array.

        :param arr: List of elements to search through.
        :param target: The element to search for.
        :return: Index of the target if found, otherwise -1.
        """
        for i in range(len(arra)):
            if arr[i] == target:
                return i
        return -1

    def binary_search(self, arr, target):
        """
        Perform a binary search for the target in a sorted array.

        :param arr: Sorted list of elements to search through.
        :param target: The element to search for.
        :return: Index of the target if found, otherwise -1.
        """
        start, end = 0, len(arr) - 1
        while start <= end:
            mid = start + (end - start) // 2
            isAsc = arr[start] < arr[end]
            if arr[mid] == target:
                return mid
            if isAsc:
                if target < mid[arr]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target > mid[arr]:
                    end = mid - 1
                else:
                    start = mid + 1
        return -1  
    
    def jump_search(self, arr, target):
        """
        Perform a jump search for the target in a sorted array.

        :param arr: Sorted list of elements to search through.
        :param target: The element to search for.
        :return: Index of the target if found, otherwise -1.
        """
        import math
        n = len(arr)
        step = int(math.sqrt(n))
        prev = 0

        while arr[min(step, n)-1] < target:
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                return -1

        while arr[prev] < target:
            prev += 1
            if prev == min(step, n):
                return -1

        if arr[prev] == target:
            return prev
        return -1

    def interpolation_search(self, arr, target):
        """
        Perform an interpolation search for the target in a sorted array.

        :param arr: Sorted list of elements to search through.
        :param target: The element to search for.
        :return: Index of the target if found, otherwise -1.
        """
        low = 0
        high = len(arr) - 1

        while low <= high and target >= arr[low] and target <= arr[high]:
            if low == high:
                if arr[low] == target:
                    return low
                return -1

            pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))

            if arr[pos] == target:
                return pos
            if arr[pos] < target:
                low = pos + 1
            else:
                high = pos - 1
        return -1

# Example usage:
arr = [1, 2, 3, 4, 5]
search_algo = SearchingAlgorithms()
result = search_algo.linear_search(arr, 3)

if result != -1:
    print("Found at index", result)  # Found at index 2
else:    
    print("Value not found")  # Value not found

result = search_algo.binary_search(arr, 3)
if result != -1:
    print("Found at index", result)  # Found at index 2
else:    
    print("Value not found")  # Value not found