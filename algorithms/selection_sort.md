# Selection Sort

## Description
> Selection Sort is a **comparison-based sorting algorithm** that repeatedly selects the largest (or smallest) element from the unsorted portion of an array and swaps it with the last (or first) element of the unsorted porton.

---

## Key Idea
- The array is divided into a **sorted** and **unsorted** portion.
- Selection Sort can sort by either the **smallest** or **largest** value each pass.
- In this example, we sort by the **largest** value, so:
  - the sorted portion grows from the right
  - the unsorted portion shrinks from the left

1. Find the largest value in the unsorted portion.
2. Swap it with the last unsorted element.
3. Increase the sorted portion by one.
4. Repeat until only one unsorted element remains, indicating the array is sorted.

---

## Python Code - Sort By Largest:

```py
def selection_sort_largest(arr):
    for i in range(len(arr) - 1, 0, -1):
        max_idx = 0
        
        for j in range(1, i + 1):
            if arr[j] > arr[max_idx]:
                max_idx = j

        arr[i], arr[max_idx] = arr[max_idx], arr[i]

    return arr
```

## Python Code - Sort By Smallest:

```py
def selection_sort_smallest(arr):
    for i in range(len(arr)):
        min_idx = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr
```

---

## Time Complexity

| Case | Complexity | Explanation |
|---|---|---|
| Best Case | \(O(n^2)\) | jflksahfks hfklsfksd hfhsdlfjk sdhjkfhsdl fsldfhsadkjfhsd |
| Average Case | o | jflksahfks hfklsfksd hfhsdlfjk sdhjkfhsdl fsldfhsadkjfhsd |
| Worst Case | o | jflksahfks hfklsfksd hfhsdlfjk sdhjkfhsdl fsldfhsadkjfhsd |

---

## Space Complexity

| Complexity | |
|---|---|
| Space | |

### Explanation
> Explain memory usage.

---

# Example Run Through

## Initial Array

```text
[]
```

---

## 1st Pass

### Find Minimum
> Explain what values are checked.

### Swap
```text
[]
```

### Comparisons
-

### Swaps
-

---

## 2nd Pass

### Find Minimum
> Explain what values are checked.

### Swap
```text
[]
```

### Comparisons
-

### Swaps
-

---

## 3rd Pass

### Find Minimum
> Explain what values are checked.

### Swap
```text
[]
```

### Comparisons
-

### Swaps
-

---

# Total Operations

## Total Comparisons

```text
formula here
```

### Example
```text
example calculation
```

---

## Total Swaps

```text
formula here
```

---

# Characteristics

## Advantages
- 
- 
- 

## Disadvantages
- 
- 
- 

---

# Stability
- Stable / Not Stable
- Explanation:

---

# In-Place?
- Yes / No
- Explanation:

---

# When To Use
- 
- 
- 

---

# Notes
> Extra observations, tips, or exam notes.