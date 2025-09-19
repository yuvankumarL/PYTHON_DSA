def binary_search(arr, target, start=None, end=None):
        """
        Perform a binary search for the target in a sorted array.

        :param arr: Sorted list of elements to search through.
        :param target: The element to search for.
        :return: Index of the target if found, otherwise -1.
        """
        if start is None and end is None:
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

def search_in_2d_array(arr, target):
    """
    Search for a target value in a 2D array.

    :param arr: 2D list of elements to search through.
    :param target: The element to search for.
    :return: Tuple of (row_index, col_index) if found, otherwise (-1, -1).
    """
    row = 0
    col = len(arr)-1
    while row < len(arr) and col >= 0:
        if arr[row][col] == target:
            return (row, col)
        
        if arr[row][col] < target:
            row += 1
        else:
            col -= 1
    return (-1, -1)

def find_in_infinite(arr, target):
    """
    Search for a target value in an infinite sorted array.

    :param arr: Infinite sorted list of elements to search through.
    :param target: The element to search for.
    :return: Index of the target if found, otherwise -1.
    """
    start, end = 0, 1
    while target > arr[end]:
        temp = start+1
        end = end + (end - start + 1) * 2   
        start = temp
    return binary_search(arr, target, start, end)

