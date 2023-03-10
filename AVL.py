# Written by Farhad Asadi

class AVL:
    """ AVL Tree """
    class Node:
        """ Node Class"""
        def __init__(self):
            """ Constructor for Node """
            self.left = None
            self.right = None
            self.data = None
            self.height = 1

    def __init__(self):
        """ Constructor for avl Tree"""
        self._root = None
        self.node_id = 0 # ONLY USED WITHIN to_graphviz()!

    def insert(self, element):
        """ This function inserts new node into the tree """
        self._root = self._insert(self._root, element)

    def _insert(self, root, element):
        new_node = self.Node()
        new_node.data = element
        # If no root, create one
        if root is None:
            root = new_node
            return root
        # Ignore duplicates
        if element == root.data:
            pass
        elif element < root.data:
            root.left = self._insert(root.left, element)
        else:
            root.right = self._insert(root.right, element)

        root.height = 1 + max(self._height(root.left), self._height(root.right))

        # Balance The treex
        balance_factor = self.get_balance(root)
        if balance_factor > 1:
            if element < root.left.data:
                return self.right_rotation(root)
            root.left = self.left_rotation(root.left)
            return self.right_rotation(root)
        if balance_factor < -1:
            if element > root.right.data:
                return self.left_rotation(root)
            root.right = self.right_rotation(root.right)
            return self.left_rotation(root)
        return root

    def remove(self, element):
        self._root = self._remove(self._root, element)

    def _remove(self, root , key):
        if not root:
            return root
        elif key < root.data:
            root.left = self._remove(root.left, key)
        elif key > root.data:
            root.right = self._remove(root.right, key)
        else:
            if root.left is None and root.right is None:
                #print("No children")
                root = None
                return root
            elif root.left is not None:
                current_temp = root.left
                parent_temp = root
                if current_temp.right is None:
                    parent_temp.data = current_temp.data
                    parent_temp.left = current_temp.left
                else:
                    current_temp = self._get_max(root.left)
                    root.data = current_temp.data
                    root.left = self._remove(root.left, current_temp.data)
            else:
                current_temp = root.right
                root = None
                return current_temp

        root.height = 1 + max(self._height(root.left), self._height(root.right))

        # Balance the tree
        balanceFactor = self.get_balance(root)
        if balanceFactor > 1:
            if self.get_balance(root.left) >= 0:
                return self.right_rotation(root)
            root.left = self.left_rotation(root.left)
            return self.right_rotation(root)
        if balanceFactor < -1:
            if self.get_balance(root.right) <= 0:
                return self.left_rotation(root)
            root.right = self.right_rotation(root.right)
            return self.left_rotation(root)
        return root

    def left_rotation(self, root):
        a = root.right
        b = a.left
        a.left = root
        root.right = b
        root.height = 1 + max(self._height(root.left), self._height(root.right))
        a.height = 1 + max(self._height(a.left), self._height(a.right))
        return a

    def right_rotation(self, root):
        a = root.left
        b = a.right
        a.right = root
        root.left = b
        root.height = 1 + max(self._height(root.left), self._height(root.right))
        a.height = 1 + max(self._height(a.left), self._height(a.right))
        return a

    def is_balanced(self, root):
        if root is None:
            return True
        left_height = self._height(root.left)
        right_height = self._height(root.right)
        if (abs(left_height - right_height) <= 1) and self.is_balanced(root.left) is True and self.is_balanced(root.right) is True:
            return True
        return False

    def get_balance(self, root):
        if root is None:
            return 0
        return self._height(root.left) - self._height(root.right)

    def find(self, element):
        value = self._find(self._root, element)
        return value

    def _find(self,node, key):
        #node = self._root
        if node is None:
            return False
        if node.data == key:
            return True
        left_find = self._find(node.left, key)
        if left_find:
            return True
        right_find = self._find(node.right, key)
        return right_find

    # Preorder traversering
    def pre_order_walk(self):
        """ Preorder walk, The function returns a list"""
        current = self._root
        lst1 = self._preorder(current)
        return lst1

    def _preorder(self, root):
        lst1 = []
        if root is not None:
            lst1.append(root.data)
            lst1 = lst1 + self._preorder(root.left)
            lst1 = lst1 + self._preorder(root.right)
        return lst1

    #Inorder traversering
    def in_order_walk(self):
        """ Inorder traversering, The function returns a list"""
        current = self._root
        lst1 = self._inorder(current)
        return lst1

    def _inorder(self, root):
        lst1 = []
        if root is not None:
            lst1 = self._inorder(root.left)
            lst1.append(root.data)
            lst1 = lst1 + self._inorder(root.right)
        return lst1

    # Postorder traversering
    def post_order_walk(self):
        """ Postorder walk. The function returns a list"""
        current = self._root
        lst1 = self._postorder(current)
        return lst1

    def _postorder(self, root):
        lst1 = []
        if root is not None:
            lst1 = self._postorder(root.left)
            lst1 = lst1 + self._postorder(root.right)
            lst1.append(root.data)
        return lst1

    # Get the tree height
    def get_tree_height(self):
        """ This function returns the height of the tree """
        if not self._root:
            return -1
        return self._height(self._root) - 1

    def _height(self, current_node):
        if not current_node:
            return 0
        return current_node.height

    def _get_min(self, root):
        if root is None or root.left is None:
            return root
        return self._get_min(root.left)

    def get_min(self):
        """ This function returns the smallest value in the tree """
        current = self._root
        while current is not None:
            if current.left is None:
                return current.data
            current = current.left

    def _get_max(self, root):
        if root is None or root.right is None:
            return root
        return self._get_max(root.right)

    def get_max(self):
        """ This function return the largest value in the tree"""
        current = self._root
        while current is not None:
            if current.right is None:
                return current.data
            current = current.right

    def to_graphviz_rec(self, data, current):
        my_node_id = self.node_id
        data += "\t" + str(my_node_id) + " [label=\"" + str(current.data) + "\"];\n"
        self.node_id += 1
        if current.left is not None:
            data += "\t" +  str(my_node_id) + " -> " + str(self.node_id) + " [color=blue];\n"
            data = self.to_graphviz_rec(data, current.left)
        else:
            data += "\t" + str(self.node_id) + " [label=nill,style=invis];\n"
            data += "\t" +  str(my_node_id) + " -> " + str(self.node_id) + " [style=invis];\n"

        self.node_id += 1
        if current.right is not None:
            data += "\t" +  str(my_node_id) + " -> " + str(self.node_id) + " [color=red];\n"
            data = self.to_graphviz_rec(data, current.right)
        else:
            data += "\t" + str(self.node_id) + " [label=nill,style=invis];\n"
            data += "\t" +  str(my_node_id) + " -> " + str(self.node_id) + " [style=invis];\n"
        return data

    def to_graphviz(self):
        data = ""
        if self._root is not None:
            self.node_id = 0
            data += "digraph {\n"
            data += "\tRoot [shape=plaintext];\n"
            data += "\t\"Root\" -> 0 [color=black];\n"
            data = self.to_graphviz_rec(data, self._root)
            data += "}\n"
        return data
