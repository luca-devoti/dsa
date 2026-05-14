# Bubble Sort

## Description
> Bubble Sort is a **comparison-based sorting algorithm** that repeatedly steps through an array, compares adjacent elements, and swaps them if they are in the wrong order.

---

## Key Idea
- Bubble Sort has two variations: standard and optimised.
- This example demonstrates the steps of the **standard** algorithm.
- The array is divided into a **sorted** and **unsorted** portion.
  - The sorted portion grows from the right.
  - The unsorted portion shrinks from the left.

1. Compare adjacent elements in the unsorted portion of the array.
2. If the left element is greater than the right element, swap them.
3. Continue through the unsorted portion, causing the largest value to “bubble” to the end of the array.
4. Shrink the unsorted portion by one element.
5. Repeat until the array is sorted.

---

## Python Code - Default

```py
def bubble_sort_default(arr): 
    for index in range(len(arr) - 1, 0, -1):
        for i in range(index):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
```

## Python Code - Optimised

```py
def bubble_sort_optimised(arr): 
    for index in range(len(arr) - 1, 0, -1):
        swapped = False
        for i in range(index):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
```

---

## Time Complexity 

| Case | Complexity | Explanation |
|---|---|---|
| Best Case | $O(n^2)$ | The algorithm still performs all passes even if the array is already sorted. |
| Average Case | $O(n^2)$ | Even if some parts are already sorted, the nested loop structure still performs multiple passes through the array. |
| Worst Case | $O(n^2)$ | Every element must be repeatedly swapped into the correct position. |

| Optimised Case | Complexity | Explanation |
|---|---|---|
Best Case | $O(n)$ | If no swaps are made during the first pass, the array is already sorted, so the algorithm exits early. |

---

## Space Complexity

| Space Complexity | Explanation |
|---|---|
| $O(1)$ | Bubble Sort sorts the array in place and only uses a small, constant amount of extra memory for temporary variables during swaps. |

---

## Visualisation

![Bubble Sort Animation](/visualisations/bubble_sort.gif)

---

## Example Run Through

### Initial Array
```py
[96, 83, 97, 32, 25, 27]
```

---

| Pass | Resulting Array State | # of Comparisons to Bubble Largest | # of Swaps |
|---|---|---|---|
| 1st pass | [83, 96, 32, 25, 27, **97**] | 5 | 4 |
| 2nd pass | [83, 32, 25, 27, **96, 97**] | 4 | 3 |
| 3rd pass | [32, 25, 27, **83, 96, 97**] | 3 | 3 |
| 4th pass | [25, 27, **32, 83, 96, 97**] | 2 | 2 |
| 5th pass | [25, **27, 32, 83, 96, 97**] | 1 | 0 |

---

## Notes
> N/A.