# Linked List ADT

## Description
> Abstract Data Type (ADT) is a conceptual model. They define what a data structure does without dictating how it does it. By separating the logical properties from the physical implementation, ADTs allow for cleaner, more maintainable code.

> A Linked List Abstract Data Type (ADT) is a linear collection of items consisting of **nodes**, where each node contains data and a reference (link) to the next node in the sequence. Items are connected through these links rather than being stored in consecutive memory locations, as they are in an array-based list. 

## Key Idea
- The first node is referred to as the head of the linked list, and the final node points to None, indicating the end of the list.
- A Linked List, in comparison to a normal array-based list, allows for efficient insertion and removal of items, as there is no need to shift existing data. Instead, we simply update the references (links) between nodes by adjusting their next values.
- To make use of a LinkedList ADT, we must first define a Node class that offers the following functionality:

1. `Node(data, next)` - Creates and returns a new node instance with the provided data, and pointing to a next node (if left blank set to None)

- The LinkedList ADT consists of the following functionality:

1. `LinkedList()` - Creates and returns a new linked list instance. 
2. `add(item)` - Adds a new item to the front of the linked list.
3. `remove(item)` - Removes the item from the linked list.
4. `search(item)` - Searches for the item in the linked list and returns a boolean whether it is found
5. `is_empty()` - Returns a boolean value indicating whether the linked list contains any items.
6. `size()` - Returns the number of items in the linked list.

---

## Python Code - Node

```py
class Node:
   def __init__(self, init_data, next=None):
       self.data = init_data
       self.next = next
```

---

## Python Code - Linked List

```py
class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def add(self, item):
        new_node = Node(item, self.head)
        self.head = new_node
        self.count += 1

    def remove(self, item):
        found = False
        current = self.head
        previous = None
        while current is not None and not found:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next
        if found:
            if previous == None: # Must be first node in list
                self.head = current.next
            else: # In this case node has a previous node
                previous.next = current.next
            self.count -= 1
    
    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            else:
                current = current.next
        return False

    def is_empty(self):
        return self.count == 0
    
    def size(self):
        return self.count
```

---

## Time Complexity

| Case | Complexity | Explanation |
|---|---|---|
| `add(item)` | $O(1)$ |  |
| `remove(item)` | $O(n)$ |  |
| `search(item)` | $O(n)$ |  |

---


## Space Complexity

| Space Complexity | Explanation |
|---|---|
| $O(n)$ | |

---

## Why use a linkedlist?
- You might already realise that the time complexity of a basic array-based list is the same as the linkedlist. Both add in $0(1)$, linked lists adding to the start and array-based lists as the end, and both require $0(n)$ for removing/searching for a specific item.

1. 

> Notes: Whenever altering a linked list, **always** make sure there will be a link between the nodes before changing them, if you lose one chained link, the list is gone. 
> For example, if you're trying to remove a node, make sure to update the previous pointer to the *removing_node*'s next first, because if you set the *removing_node*'*s next to none, you will lose the other end in memory.

> When we remove a value, we just remove it from the theoretical linked list, even though it still exists now somewhere in memory, we just ignore it as a garbage value. 