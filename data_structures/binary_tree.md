# Binary Tree

## Description
> A Binary Tree is a hierarchical, non-linear structure that consists of a set of points called nodes and edges that connect these nodes. Binary trees are recursive. They are similar to linked lists, but each node contains data and references to a left child and a right child, instead of a single next node.


![Binary Basic Visual](/visualisations/binary_tree_code_visual.jpeg)

## Terminology
- Node: A single item in a binary tree, storing a value and references/pointers to its left and right child nodes.
- Edge: A connection between two nodes.
    - Node A is the parent of Node B, and Node B is the child of Node A, if an edge points from Node A to Node B.
        - A node can only have one parent.
        - In a binary tree, each node can have at most 2 children.
- Root: One node is distinguished and called the root node - the node without a parent.
- Siblings: If two nodes have the same parent, they are siblings.
- Ancestor: Node A is an ancestor of Node D if there is a path from Node A down to Node D.
- Descendant: If Node A is an ancestor of Node D, then Node D is a descendant of Node A.
- Leaf: A node without any children. 
- Internal nodes: A non-leaf node / a node with at least one child, including the root if it has children.
- Subtree: A node and all its descendants form a subtree.
- Path: A sequence of nodes connected by edges from one node to another.
- Height of a node: The number of edges from the **node** to the **deepest leaf**. That is, the longest path from the node to a leaf node.
- Depth of a node: The number of edges from **the root** to **the node**.
- Height of a tree: The height of a tree is the height of the root node, which is equal to the depth of the deepest node.

![Binary Tree Terminology](/visualisations/binary_tree_terminology.png)
![Binary Tree Heights and Depths](/visualisations/binary_tree_heights_depths.jpg)

---

## Types of trees

### 1. Full Binary Tree
- A **full binary tree** is a binary tree in which every node has either **0 children** or **2 children**.

![Full Binary Tree](/visualisations/full_binary_tree.png)

### 2. Complete Binary Tree
- A **complete binary tree** is a binary tree in which every level is full except possibly the last level. The last level is filled from **left to right**.

![Complete Binary Tree](/visualisations/complete_binary_tree.png)

### 3. Perfect Binary Tree
- A **perfect binary tree** is a binary tree in which every internal node has exactly **2 children**, and all leaf nodes are at the same level.

![Perfect Binary Tree](/visualisations/perfect_binary_tree.png)

---

## Key Idea
- Trees are recursive structures. For example, the sum of all values in a tree is: `root value + sum of left subtree + sum of right subtree`

A BinaryTree class consists of the following functionality:

1. `BinaryTree(data)` - Creates and returns a tree node with the inputted data value.
2. `insert_left(data)` - If there is no left child, insert a new tree node with the specified data as the current node's left child.  
   Otherwise, create a new node containing the specified data, make the existing left subtree the left child of the new node, and then make the new node the left child of the current node.
3. `insert_right(data)` - If there is no right child, insert a new tree node with the specified data as the current node's right child.  
   Otherwise, create a new node containing the specified data, make the existing right subtree the right child of the new node, and then make the new node the right child of the current node.


```py
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert_left(self, new_data):
        if self.left == None:
            self.left = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data)
            t.left = self.left
            self.left = t
        
    def insert_right(self, new_data):
        if self.right == None:
            self.right = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data)
            t.right = self.right
            self.right = t
```

---

## Tree traversal techniques

> Trees are not linear structures like lists, so there is more than one way to visit every node. These different methods are called tree traversal techniques.

> Recursive traversal techniques work like a recursive checklist. You follow the steps from top to bottom. When a step tells you to visit a subtree, you apply the same checklist again to that subtree. When there is no subtree left to visit, you return to the previous call and continue from where you left off.

### 1. In-order Traversal

For each node/subtree:

- Traverse the left subtree, if it exists.
- Visit the current node/root of that subtree.
- Traverse the right subtree, if it exists.

![In-order visualisation](/visualisations/inorder_traversal.png)
![In-order visualisation gif](/visualisations/inorder_traversal_gif.gif)

### 2. Pre-order Traversal

For each node/subtree:

- Visit the current node/root of that subtree.
- Traverse the left subtree, if it exists.
- Traverse the right subtree, if it exists.

![Pre-order visualisation](/visualisations/preorder_traversal.png)
![Pre-order visualisation gif](/visualisations/preorder_traversal_gif.gif)

### 3. Post-order Traversal

For each node/subtree:

- Traverse the left subtree, if it exists.
- Traverse the right subtree, if it exists.
- Visit the current node/root of that subtree.

![Post-order visualisation](/visualisations/postorder_traversal.png)
![Post-order visualisation gif](/visualisations/postorder_traversal_gif.gif)

4. Breadth First / Level-order
- Visit all nodes from left to right at the current level
- Move to the next level
---

## Where it's useful
- Converting infix expressions into an expression tree 

![Expression Tree](/visualisations/expression_tree.jpg)

## Notes: 
> N/A