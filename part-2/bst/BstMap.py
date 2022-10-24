from dataclasses import dataclass
from typing import Any

# The BstMap class is a binary search tree based implementation of
# a map (or dictionary). It works for any type of values and for
# all types keys that are comparable ==> we can compare keys using
# the operators < and >.


# The Node class is responsible for most of the work.
# Each call to the BstMap class is just delegated to the
# root node which starts a recursive sequence of calls to
# handle the request. Notice: All Node methods are recursive.
@dataclass
class Node:
    key: Any = None         # the key
    value: Any = None       # the value
    left: Any = None        # left child (a Node)
    right: Any = None       # right child (a Node)

    # Method to insert new key-value pair
    def put(self, key, value):

        # Check if key already exists
        if self.get(key):

            if self.key == key:  # Check if current node has this key
                self.value = value  # Reassign the value if true

            else:  # If current node's key != key, but key exists elsewhere
                if self.left:  # If left branch exists
                    if self.left.get(key):  # If left branch has key
                        self.left.put(key, value)  # Call itself on left branch
                        return

                if self.right:  # Else If right branch exists
                    if self.right.get(key):  # If right branch has key
                        self.right.put(key, value)  # Call itself on right
                        return

        else:

            if key[0] > self.key[0]:
                if not self.right:  # If right branch does not exist
                    self.right = Node(key, value)
                else:  # If right branch exists
                    self.right.put(key, value)

            elif key[0] <= self.key[0]:
                if not self.left:  # If left branch does not exist
                    self.left = Node(key, value)
                else:
                    self.left.put(key, value)  # If left branch exists

    # Method to return the entire BST as a string
    def to_string(self):
        lst = []
        done = self.as_list(lst)
        return ' '.join([f"({','.join(map(lambda c: str(c), i))})"
                        for i in sorted(done)])

    # Method to return total length of the BST
    def count(self):
        c = 1  # Every method call returns 1
        if self.left:  # If left child exists
            c += self.left.count()  # Add c to return value of child method
        if self.right:  # Same for right child
            c += self.right.count()
        return c  # Returns total count

    # Method to get an element value based on key
    def get(self, key):
        found = None  # Initial value of found

        if self.key == key:  # If node's key == key
            found = self.value  # Reassign found to node's key
        else:

            if self.left:  # If left child exists
                found = self.left.get(key)  # Calls itself on left child

            # Make sure we didn't find key on left branch before right search
            if self.right and found is None:  # Same for right child
                found = self.right.get(key)
        return found

    def max_depth(self):
        depthL = 1
        depthR = 1

        if self.left:
            depthL += self.left.max_depth()
        if self.right:
            depthR += self.right.max_depth()

        if depthL < depthR:
            return depthR
        else:
            return depthL

    # We do a left-to-right in-order traversal of the tree
    # to get the key-value pairs sorted base on their keys
    def as_list(self, lst):
        lst.append((self.key, self.value))

        if self.left:  # If left branch exists
            self.left.as_list(lst)  # Call itself recursively on left
        if self.right:  # If right branch exists
            self.right.as_list(lst)

        res = list(sorted(lst, key=lambda i: i[0]))
        return res  # Return finished string of all elements


# The BstMap class is rather simple. It basically just takes care
# of the case when the map is empty. All other cases are delegated
# to the root node ==> the Node class.
# The class below is complete ==> not to be changed
@dataclass
class BstMap:
    root: Node = None

    # Adds a key-value pair to the map
    def put(self, key, value):
        if self.root is None:    # Empty, add first node
            self.root = Node(key, value, None, None)
        else:
            self.root.put(key, value)

    # Returns a string representation of all the key-value pairs
    def to_string(self):
        if self.root is None:     # Empty, return empty brackets
            return "{ }"
        else:
            res = "{ "
            res += self.root.to_string()
            res += "}"
            return res

    # Returns the current number of key-value pairs in the map
    def size(self):
        if self.root is None:
            return 0
        else:
            return self.root.count()

    # Returns the value for a given key. Returns None
    # if key doesn't exist (or map is empty)
    def get(self, key):
        if self.root is None:
            return None
        else:
            return self.root.get(key)

    # Returns the maximum tree depth. That is, the length
    # (counted in nodes) of the longest root-to-leaf path
    def max_depth(self):
        if self.root is None:
            return 0
        else:
            return self.root.max_depth()

    # Returns a sorted list of all key-value pairs in the map.
    # Each key-value pair is represented as a tuple and the
    # list is sorted on the keys ==> left-to-right in-order
    def as_list(self):
        lst = []
        if self.root is None:
            return lst
        else:
            return self.root.as_list(lst)