# Insertion Sort

## Description
> Insertion Sort is a **comparison-based sorting algorithm** that repeatedly takes the first element from the unsorted portion and inserts it into its correct position among the already sorted elements.

---

## Key Idea
- The array is divided into a **sorted** (left) and **unsorted** (right) portion, where the sorted portion initially contains the element at index 0.
1. The outer loop selects the first element from the unsorted portion.
2. Compare the selected element with elements in the sorted portion, moving from right to left.
3. While an element in the sorted portion is greater than the selected element, shift it one position to the right.
4. Continue shifting elements until an element smaller than or equal to the selected element is found, or the beginning of the array is reached.
5. Insert the selected element into its correct position (one position to the right of the current element) in the sorted portion.
6. Repeat until the entire array is sorted.

---

## Python Code

```py
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key
```

---

## Time Complexity

| Case | Complexity | Explanation |
|---|---|---|
| Best Case | $O(n)$ | If the array is already sorted, the inner while loop never shifts elements, so only one pass through the array is needed. |
| Average Case | $O(n^2)$ | On average, each element must shift partway through the sorted portion of the array. |
| Worst Case | $O(n^2)$ | If the array is reverse sorted, each element must shift through the entire sorted portion of the array. |

---

## Space Complexity

| Space Complexity | Explanation |
|---|---|
| $O(1)$ | Insertion Sort sorts the array in place and only uses a small, constant amount of extra memory for variables such as `key` and `j`. |

---

## Visualisation

![Insertion Sort Visualisation](/visualisations/insertion_sort.jpg)

![Insertion Sort Visualisation 2](/visualisations/insertion_sort.gif)

---

## Example Run Through

### Initial Array

```py
[10, 7, 9, 5, 6]
```

---

| Pass | Resulting Array State | # of Comparisons | # of Shifts |
|---|---|---|---|
| 1st pass | [**7, 10**, 9, 5, 6] | 1 | 1 |
| 2nd pass | [**7, 9, 10**, 5, 6] | 2 | 1 |
| 3rd pass | [**5, 7, 9, 10**, 6] | 3 | 3 |
| 4th pass | [**5, 6, 7, 9, 10**] | 4 | 3 |

---

## Notes
> We assume the first element is already part of the sorted portion and begin from the second element.
