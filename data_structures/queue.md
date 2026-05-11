### Stack ADT

```py
class Queue:
    def __init__(self):
        self.items = []
        self.count = 0
    def is_empty(self):
        return self.count == 0
    def enqueue(self, item):
        self.items.insert(0,item)
        self.count += 1
    def dequeue(self):
        if self.is_empty():
            raise IndexError('ERROR: The queue is empty!')
        self.count -= 1
        return self.items.pop() 
    def size(self):
        return self.count
    def peek(self):
        if self.is_empty():
            raise IndexError('ERROR: The queue is empty!')
        return self.items[-1]
    def __str__(self):
        return '-> |' + str(self.items)[1:-1] + '| ->'
    def clear(self):
        self.items = []
```