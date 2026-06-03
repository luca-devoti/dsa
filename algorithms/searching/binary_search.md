# Binary Search

## Description
> Binary search is an efficient searching algorithm that works on a **sorted array**. It repeatedly compares the target with the middle element and eliminates half of the remaining elements each step until the target is found or the search space becomes empty.

---

## Key Idea
- The algorithm only works on a **sorted** array.
1. Find the middle element of the current search range.
2. Compare the middle element with the target value:
    - If it is equal, return the index (search is complete).
    - If the target is larger, discard the left half of the array.
    - If the target is smaller, discard the right half of the array.
3. Repeat the process on the remaining half by finding the new middle element.
4. Continue dividing the search space in half until the target is found or the range becomes empty (target not present).

---

## Python Code - Returning Index

```py
def binary_search(numbers, target_value):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target_value:
            return middle
        elif numbers[middle] > target_value:
            right = middle - 1
        else:
            left = middle + 1

    return -1
```

---

## Time Complexity

| Case | Complexity | Explanation |
|---|---|---|
| Best Case | $O(1)$ | The target value is found at the middle on the first check. |
| Average Case | $O(\log n)$ | Each comparison eliminates half of the remaining search space. On average, the target is found after logarithmic steps. |
| Worst Case | $O(n)$ | Even in the worst case, the search space is halved repeatedly until it becomes empty. |

---

## Space Complexity

| Space Complexity | Explanation |
|---|---|
| $O(1)$ | Binary search uses a constant amount of extra memory. It only stores a few variables such as left, right, and middle, regardless of the input size. |

---

## Visualisation

![Binary Search Animation](/visualisations/binary_search.gif)

---

## Example Run Through

### Initial Array - Target value = 83
```py
[25, 27, 32, 83, 96, 97]
```

---

| Step | Array State (active range)  | left | right | middle | middle value | Comparison | Action            |
| ---- | --------------------------  | ---- | ----- | ------ | ------------ | ---------- | ----------------- |
| 1    | [**25, 27, 32, 83, 96, 97**]| 0    | 5     | 2      | 32           | 32 < 83    | search right half |
| 2    | [25, 27, 32, **83, 96, 97**]| 3    | 5     | 4      | 96           | 96 > 83    | search left half  |
| 3    | [25, 27, 32, **83**, 96, 97]| 3    | 3     | 3      | 83           | 83 == 83   | Found             |


---

## Notes
> N/A.