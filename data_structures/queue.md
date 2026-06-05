# Queue ADT

## Description
> Abstract Data Type (ADT) is a conceptual model. They define what a data structure does without dictating how it does it. By separating the logical properties from the physical implementation, ADTs allow for cleaner, more maintainable code.

> A Queue Abstract Data Type (ADT) is an ordered collection of items which follows the **First-In, First-Out (FIFO)** property, where the addition of new items take place at the **back, or rear, of the queue**, and removal of existing items take place at the other end, **the front of the queue**.

> 

---

## Key Idea - Basic 
- We implement a queue using a Python list, with elements inserted at the start (the back) and removed from the end of the list, which represents the front of the queue.
- The basic Queue ADT consists of the following functionality:

1. `Queue()` - Creates and returns a new, empty queue instance. 
2. `enqueue(item)` - Inserts a new item at the back of the queue.
3. `dequeue()` - Removes and returns the item at the front of the queue.
4. `peek()` - Returns the item at the front of the queue without removing it.
5. `is_empty()` - Returns a boolean value indicating whether the queue contains no items.
6. `size()` - Returns the total number of items currently in the queue.

- Optional methods:

7. `__str__()` - Returns a formatted string representation of the queue.
8. `clear()` - Removes all items from the queue.

---

## Python Code - Basic

```py
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.count == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError('ERROR: The queue is empty!')
        return self.items.pop() 
    
    def peek(self):
        if self.is_empty():
            raise IndexError('ERROR: The queue is empty!')
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return '-> |' + str(self.items)[1:-1] + '| ->'

    def clear(self):
        self.items = []
```

---

## Time Complexity

| Case | Complexity | Explanation |
|---|---|---|
| `peek()` | $O(1)$ | The front of the queue is always at the end of the list `self.items[-1]`, so it is accessed directly. |
| `enqueue(item)` | $O(n)$ | Inserting at index 0 requires shifting all existing elements one position to the right. |
| `dequeue()` | $O(1)$ | Removing from the end of the list using `pop()` is a constant-time operation. |

---

## Space Complexity

| Space Complexity | Explanation |
|---|---|
| $O(n)$ | A Queue ADT stores up to `n` elements, so the memory used grows linearly with the number of items in the queue. |

---

## Visualisation

![Queue Visualisation](/visualisations/queue.png)

---

## Key Idea - Circular
- We implement a circular queue using a standard Python list initialized with a fixed capacity of None values. Instead of shifting elements, we maintain the indices of the start (front, where items are dequeued) and the end (back, where items are enqueued).
- The core purpose of this approach is to optimise the `enqueue` time complexity from $O(n)$ to $O(1)$. By directly overwriting `None` placeholders at specific indices, we completely avoid the costly linear shifting of elements required by the basic queue.
- We manipulate the front and back indices of the static list using the modulo operator (`%`) so that they wrap around back to index `0` the moment they advance **past** index `max_queue - 1` (the final slot of the list).
- The Circular Queue ADT consists of the following functionality:

1. `CircularQueue(capacity)` - Creates and returns a new circular queue instance with a fixed capacity filled with `None` placeholders.
2. `enqueue(item)` - Advances the `back` pointer to the next available index and inserts the new item at that position, **only if the queue is not full**.
3. `dequeue()` - Returns the item at the current `front` index position, advances the `front` pointer to the next item, **only if the queue is not empty**.
4. `peek()` - Returns the item at the `front` of the queue without removing it.
5. `is_empty()` - Returns a boolean value indicating whether the queue contains zero elements.
6. `is_full()` - Returns a boolean value indicating whether the current count of elements has reached the maximum capacity.

- Optional methods:

7. `clear()` - Re-initialises the internal list with `None` values, resets the `front` and `back` pointers to their original starting configurations, and resets the element `count` to `0`.

---

## Python Code - Circular

```py
class CircularQueue:
    def __init__(self, capacity):
        self.items = [None] * capacity
        self.max_queue = capacity
        self.front = 0
        self.back = capacity - 1
        self.count = 0

    def is_full(self):
        return self.count == self.max_queue

    def is_empty(self):
        return self.count == 0

    def enqueue(self, item):
        if self.is_full():
            raise IndexError("ERROR: The queue is full.")
        self.back = (self.back + 1) % self.max_queue
        self.items[self.back] = item
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("ERROR: The queue is empty.")
        item = self.items[self.front]
        self.front = (self.front + 1) % self.max_queue
        self.count -= 1
        return item
    
    def peek(self):
        if self.is_empty():
            raise IndexError('ERROR: The queue is empty!')
        return self.items[self.front]

    def clear(self):
        self.items = [None] * self.max_queue
        self.front = 0
        self.back = self.max_queue -1
        self.count = 0
```

---

## Time Complexity

| Operation | Complexity | Explanation |
| --------- | ---------- | ----------- |
| `peek()` | $O(1)$ | The front element is accessed directly using the `front` index, requiring no traversal. |
| `enqueue(item)` | $O(1)$ | The `back` index is advanced using modular arithmetic and the item is inserted at that position without shifting elements. |
| `dequeue()` | $O(1)$ | The item at the `front` index is removed *logically*, and the `front` index is advanced using modular arithmetic without shifting elements. |

---

## Space Complexity

| Space Complexity | Explanation |
|---|---|
| $O(n)$ | A Circular Queue ADT stores up to `n` elements in a fixed-size array. The memory usage is linear in the capacity of the queue, and no additional dynamic memory is required for shifting or resizing during operations. |

---

## Visualisation

![Circular Queue](/visualisations/circular_queue.png)

---

## Notes
> The circular queue does not physically remove elements on dequeue(). It just moves the front pointer forward, and the old value is ignored. enqueue() then inserts at the back position, overwriting old unused values.