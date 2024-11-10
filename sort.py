def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    # Choose a pivot (we'll use the last element here for simplicity)
    pivot = arr[-1]
    
    # Partition the array into two parts: less than and greater than the pivot
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    # Recursively apply quicksort to the left and right parts, then combine
    return quicksort(left) + [pivot] + quicksort(right)
