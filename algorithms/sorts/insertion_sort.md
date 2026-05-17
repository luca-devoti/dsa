# Insertion Sort

## Description
> Insertion Sort is a **comparison-based sorting algorithm** that repeatedly takes the first element from the unsorted portion and inserts it into its correct position among the already sorted elements.

---

## Key Idea
- The array is divided into a **sorted** and **unsorted** portion.
1. Select the first element from the unsorted portion.
2. Compare the selected element with elements in the sorted portion, moving from right to left.
3. While an element in the sorted portion is greater than the selected element, shift it one position to the right.
4. Continue shifting elements until an element smaller than or equal to the selected element is found, or the beginning of the array is reached.
5. Insert the selected element into its correct position (one position to the right of the current element) in the sorted portion.
6. Repeat until the entire array is sorted.

---

```Python Code