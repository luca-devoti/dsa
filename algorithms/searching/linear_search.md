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

| Case | Complexity | Explanation |
|---|---|---|
| Best Case | $O(1)$ | The element is found at the first position of the array. |
| Average Case | $O(n)$ | On average, the target is equally likely to be anywhere in the list, so about $\frac{n}{2}$ comparisons are needed before it is found. Therefore, the average-case time complexity is $O(n)$ |
| Worst Case | $O(n)$ | The element is at the end of the array or not present at all, requiring scanning all elements. |

---

## Space Complexity

| Space Complexity | Explanation |
|---|---|
| $O(1)$ | Linear search uses a constant amount of extra memory, only storing a few variables (such as the index and target), regardless of the size of the input list. |

---

## Visualisation

![Linear Search Animation](/visualisations/linear_search.gif)

---

## Example Run Through

### Initial Array - Target value = 32
```py
[96, 83, 97, 32, 25, 27]
```

---

| Step | Element Checked | Comparison | Result          |
| ---- | --------------- | ---------- | --------------- |
| 1    | 96              | 96 ≠ 32    | Not found       |
| 2    | 83              | 83 ≠ 32    | Not found       |
| 3    | 97              | 97 ≠ 32    | Not found       |
| 4    | 32              | 32 = 32    | Found (index 3) |

---

## Notes
> N/A.