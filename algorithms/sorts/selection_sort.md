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

## Python Code - Sort by Largest

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

## Python Code - Sort by Smallest

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
| Best Case | $O(n^2)$ | Even if the array is already sorted, Selection Sort still performs all comparisons. |
| Average Case | $O(n^2)$ | The algorithm repeatedly scans the unsorted portion of the array to locate the minimum/maximum value. |
| Worst Case | $O(n^2)$ | Even when the array is in reverse order, the same number of comparisons are still required. |

---

## Space Complexity

| Space Complexity | Explanation |
|---|---|
| $O(1)$ | Selection Sort sorts the array in-place, so it does not require additional memory that grows with the size of the input. |

---

## Visualisation - Sort by Largest

![Selection Sort Animation](../visualisations/selection_sort.gif)

---
## Example Run Through - Sort By Largest

### Initial Array

```py
[7, 3, 2, 9, 6]
```

---

| Pass | Resulting Array State | # of Comparisons to Locate Largest | # of Swaps |
|---|---|---|---|
| 1st pass | [7, 3, 2, 6, **9**] | 4 | 1 |
| 2nd pass | [6, 3, 2, **7, 9**] | 3 | 1 |
| 3rd pass | [2, 3, **6, 7, 9**] | 2 | 1 |
| 4th pass | [2, **3, 6, 7, 9**] | 1 | 1 |

---

## Notes
> N/A.