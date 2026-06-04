# Stack ADT

## Description
> Abstract Data Type (ADT) is a conceptual model. They define what a data structure does without dictating how it does it. By separating the logical properties from the physical implementation, ADTs allow for cleaner, more maintainable code.

> A Stack Abstract Data Type (ADT) is an ordered collection of items which follows the **Last-In, First-Out (LIFO)** property, where the addition of new items and removal of existing items always take place at the same end, referred to as the **top of the stack**.

---

## Key Idea
- We implement a stack using a Python list, with elements added to and removed from the end of the list, which represents the top of the stack.
- The basic Stack ADT consists of the following functionality:

1. `Stack()` - Creates and returns a new, empty stack instance.
2. `push(item)` - Adds a new item to the top of the stack.
3. `pop()` - Removes and returns the item at the top of the stack.
4. `peek()` - Returns the item at the top of the stack without removing it.
5. `is_empty()` - Returns a boolean value indicating whether the stack contains no items.
6. `size()` - Returns the total number of items currently in the stack.

- Optional methods:

7. `__str__()` - Returns a formatted string representation of the stack.
8. `clear()` - Removes all items from the stack.

---

## Python Code

```py
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)                

    def pop(self):
        if self.is_empty():
            raise IndexError('ERROR: The stack is empty!')
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError('ERROR: The stack is empty!')
        return self.items[-1]

    def size(self):
        return len(self.items)        

    def __str__(self):
        return str(self.items)[:-1] + ' <-'

    def clear(self):
        self.items = []
```

---

## Time Complexity

| Case | Complexity | Explanation |
|---|---|---|
| peek() | $O(1)$ | The top item is always at the end of the list, so it can be accessed directly. |
| push(item) | $O(1)$ | Items are only added to the end (top) of the stack, which is a constant-time operation. |
| pop() | $O(1)$ | Items are only removed from the end (top) of the stack, so no shifting of elements is required. |
| search | $O(n)$ | In the worst case, every item in the stack must be checked sequentially. |

---

## Space Complexity

| Space Complexity | Explanation |
|---|---|
| $O(n)$ | A Stack ADT stores up to n elements, so the memory used grows linearly with the number of items in the stack. |

---

## Visualisation

![Stack ADT Visualisation](/visualisations/stack.gif)

---

## Where it's useful
- [Postfix Expression Evaluation](../algorithms/stack/stack_algorithms.md#postfix-expression-evaluation)
- [Infix to Postfix Conversion](../algorithms/stack/stack_algorithms.md#infix-to-postfix-conversion)
- [Balanced Brackets/Braces](../algorithms/stack/stack_algorithms.md#balanced-brackets/braces)
- Undo and Redo features

---

## Notes
> N/A.