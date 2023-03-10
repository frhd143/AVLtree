# AVL Tree Implementation in Python
This is an implementation of the AVL tree data structure in Python.

## Overview
AVL tree is a self-balancing binary search tree, and it is named after its two inventors, Adelson-Velsky and Landis. In an AVL tree, the heights of the two child subtrees of any node differ by at most one. In other words, it is a binary tree with height-balancing property.

This implementation contains the following methods:

- `insert(element)`: inserts a new node into the tree
- `remove(element)`: removes a node from the tree
- `find(element)`: finds an element in the tree
- `pre_order_walk()`: returns a list of the nodes traversed in pre-order
- `in_order_walk()`: returns a list of the nodes traversed in in-order

## Usage
To use the AVL tree, simply import the `AVL` class from the module and create an instance of it:
```python
from AVL import AVL

tree = AVL()
```

You can then use the methods listed above to insert, remove, and find elements in the tree.

```python
tree.insert(5)
tree.insert(3)
tree.insert(8)

print(tree.find(3)) # True
print(tree.find(10)) # False

print(tree.pre_order_walk()) # [5, 3, 8]
print(tree.in_order_walk()) # [3, 5, 8]
```

You can also user https://dreampuf.github.io/GraphvizOnline/#digraph%20G%20%7B%0A%0A%20%20subgraph%20cluster_0%20%7B%0A%20%20%20%20style%3Dfilled%3B%0A%20%20%20%20color%3Dlightgrey%3B%0A%20%20%20%20node%20%5Bstyle%3Dfilled%2Ccolor%3Dwhite%5D%3B%0A%20%20%20%20a0%20-%3E%20a1%20-%3E%20a2%20-%3E%20a3%3B%0A%20%20%20%20label%20%3D%20%22process%20%231%22%3B%0A%20%20%7D%0A%0A%20%20subgraph%20cluster_1%20%7B%0A%20%20%20%20node%20%5Bstyle%3Dfilled%5D%3B%0A%20%20%20%20b0%20-%3E%20b1%20-%3E%20b2%20-%3E%20b3%3B%0A%20%20%20%20label%20%3D%20%22process%20%232%22%3B%0A%20%20%20%20color%3Dblue%0A%20%20%7D%0A%20%20start%20-%3E%20a0%3B%0A%20%20start%20-%3E%20b0%3B%0A%20%20a1%20-%3E%20b3%3B%0A%20%20b2%20-%3E%20a3%3B%0A%20%20a3%20-%3E%20a0%3B%0A%20%20a3%20-%3E%20end%3B%0A%20%20b3%20-%3E%20end%3B%0A%0A%20%20start%20%5Bshape%3DMdiamond%5D%3B%0A%20%20end%20%5Bshape%3DMsquare%5D%3B%0A%7D to visulize the tree.

## License
This code is released under the MIT License.
