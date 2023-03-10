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
- `post_order_walk()`: returns a list of the nodes traversed in post-order
- `get_tree_height()`: returns the height of the tree
- `get_min()`: returns the smallest node in the tree
- `get_max()` returns the largest node in the tree
- `to_graphviz()`: returns a code the can be used to visualize the tree


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

You can also use https://dreampuf.github.io/GraphvizOnline/ to visulize the tree.
To this you need to call the `to_graphviz()` function:
```python
print(tree.to_graphviz())
```
The function prints the code you need to copy and paste in the website above.





## License
This code is released under the MIT License.
