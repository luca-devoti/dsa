# Selection Sort By Largest
def selection_sort_largest(arr):
    for i in range(len(arr) - 1, 0, -1):
        max_idx = 0
        
        for j in range(1, i + 1):
            if arr[j] > arr[max_idx]:
                max_idx = j

        arr[i], arr[max_idx] = arr[max_idx], arr[i]

    return arr

# Selection Sort By Smallest
def selection_sort_smallest(arr):
    for i in range(len(arr)):
        min_idx = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr