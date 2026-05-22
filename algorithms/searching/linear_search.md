# Linear Search

## Description
> Linear search (or sequential search) is the simplest searching algorithm. It works by checking each element in an array one by one until the target value is found or the end of the list is reached.

---

## Key Idea
1. Iterate through each item in the array (unsorted or sorted).
2. Compare each element with the target value.
   - If the target value is found, return its index (or the element, depending on the implementation).
   - If the target value is not found after checking all elements, return -1.

---

## Python Code - Returning Index

```py
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

---

## Time Complexity