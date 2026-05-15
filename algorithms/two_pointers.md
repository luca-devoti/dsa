# Two Pointers

## Description

---

## Python Code

```py
def two_sum(arr, target):
    # Sort the array

    left, right = 0, len(arr) - 1

    # Iterate while left pointer is less than right
    while left < right:
        sum = arr[left] + arr[right]

        # Check if the sum matches the target
        if sum == target:
            return True
        elif sum < target: 
            left += 1  # Move left pointer to the right
        else:
            right -= 1 # Move right pointer to the left

    # If no pair is found
    return False
```

---