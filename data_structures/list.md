# Linked List ADT

## Description
> Abstract Data Type (ADT) is a conceptual model. They define what a data structure does without dictating how it does it. By separating the logical properties from the physical implementation, ADTs allow for cleaner, more maintainable code.

> A Linked List Abstract Data Type (ADT) is a linear collection of items consisting of **nodes**, where each node contains data and a reference (link) to the next node in the sequence. Items are connected through these links rather than being stored in consecutive memory locations, as they are in an array-based list. 

## Key Idea
- The first node in a linked list is referred to as the head of the list, and the final node in the sequence points to None, indicating the end of the list.
- A Linked List, in comparison to a normal array-based list, allows for efficient insertion and removal of items, as there is no need to shift existing data. Instead, we simply update the references (links) between nodes by adjusting their next values.
- To implement a Linked List ADT, we must first define a Node class that provides the following functionality:

1. `Node(data, next)` - Creates and returns a new node instance with the provided data, and a reference to the next node. If no next node is provided, it is set to None.

- The LinkedList ADT consists of the following functionality:

1. `LinkedList()` - Creates and returns a new linked list instance. 
2. `add(item)` - Adds a new item to the front (head) of the linked list.
3. `remove(item)` - Removes the specified item from the linked list, if it exists.
4. `search(item)` - Searches for the item in the linked list and returns True if it is found, otherwise False.
5. `is_empty()` - Returns True if the linked list contains no items, otherwise False.
6. `size()` - Returns the number of items currently stored in the linked list.

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
            if previous is None: # Must be first node in list
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
| `add(item)` | $O(1)$ | Inserting at the head only updates pointers (head and next), no traversal needed. |
| `remove(item)` | $O(n)$ | In the worst case, you may need to traverse the entire list to find the item. |
| `search(item)` | $O(n)$ | Must potentially check every node until the item is found or list ends. |

---

## Space Complexity

| Space Complexity | Explanation |
|---|---|
| $O(n)$ | Each node stores one item and a reference to the next node, so memory grows linearly with the number of elements. |

---

## Why use a Linked List?
- You might already realise that the time complexity of a basic array-based list is similar to that of a linked list in some cases. Both allow O(1) insertion, but in different ways: linked lists insert at the head, while array-based lists typically insert at the end (amortised O(1)). However, both require O(n) time for searching and removing a specific item, since they may need to traverse the entire structure.
- The key advantage of a linked list is flexibility in memory management. Unlike arrays, linked lists do not require contiguous memory, making them useful when memory is fragmented or when the size of the data structure is unknown in advance.
- **Understanding the underlying functionality of a linked list is important for better understanding the next topic, binary trees.**

---

![Linked List Visualisation](/visualisations/linked_list.png)

---

> Notes: When modifying a linked list, it is important to always ensure that the links between nodes are maintained before changing them. If a link is lost, the rest of the list can become inaccessible.

> For example, when removing a node, you should first update the previous node’s `next` reference to point to the node after the one being removed. If you instead set the removing node’s `next` to `None` first, you lose access to the rest of the list.

> When a value is removed, it is no longer part of the logical linked list, even though the node may still exist in memory. It is simply treated as no longer accessible through the list, and will eventually be cleaned up by garbage collection if no other references exist.