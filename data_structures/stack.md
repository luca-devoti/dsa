# Stack ADT

## Description
> A Stack Abstract Data Type (ADT) is a linear data structure that operates on the LIFO (Last-In, First-Out) principle where the addition of new items and the removal of existing items always takes place at the same end, referred to as the top of the stack.

---

## Key Idea
- A Stack is comprised of two primary operations:
  - Push — adds a new item to the top of the stack.
  - Pop — removes the item at the top of the stack.

- Other common operations include:
  - Peek — returns the top item without removing it.
  - is_empty — returns whether the stack contains any items.
  - size — returns the number of items currently in the stack.
  - clear — removes all items from the stack.

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
        return self.items[len(self.items) - 1]

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
| Access / Peak | $O(1)$ | The top item is always at the end of the list, so it can be accessed directly. |
| Search | $O(n)$ | In the worst case, every item in the stack must be checked sequentially. |
| Insertion | $O(1)$ | Items are only added to the end (top) of the stack, which is a constant-time operation. |
| Deletion | $O(1)$ | Items are only removed from the end (top) of the stack, so no shifting of elements is required. |

---

## Space Complexity

| Space Complexity | Explanation |
|---|---|
| $O(n)$ | A Stack ADT stores up to n elements, so the memory used grows linearly with the number of items in the stack. |

---

## Where it's useful
[stack algorithms]
- [Postfix Expression Evaluation](../algorithms/stack/stack_algorithms.md#postfix-expression-evaluation)
- [Infix to Postfix Conversion](../algorithms/stack/stack_algorithms.md#infix-to-postfix-conversion)
- [Balanced Brackets/Braces](../algorithms/stack/stack_algorithms.md#balanced-brackets/braces)
- Undo and Redo features

---

## Notes
> N/A.