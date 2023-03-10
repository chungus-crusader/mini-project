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

    # Methods that adds to value if keys are the same
    # Instead of overriding the value
    def add(self, key, value):

        # If key == current key, value += value that's passed in
        if self.key == key:
            self.value += value
            return

        # The rest is the same as in put

        if key > self.key:
            if not self.right:  # If right branch does not exist
                self.right = Node(key, value)
                return
            self.right.add(key, value)

        elif key < self.key:
            if not self.left:  # If left branch does not exist
                self.left = Node(key, value)
                return
            self.left.add(key, value)  # If left branch exists

    # Method to insert new key-value pair
    def put(self, key, value):
        if self.key == key:  # If key == key that's passed in
            self.value = value
            return

        if key > self.key:  # If key is > current key
            if not self.right:  # If right branch does not exist
                self.right = Node(key, value)
                return
            self.right.put(key, value)  # If right branch exists

        elif key <= self.key:  # If key <= current key
            if not self.left:  # If left branch does not exist
                self.left = Node(key, value)
                return
            self.left.put(key, value)  # If left branch exists

    # Method to return the entire BST as a string
    def to_string(self):

        txt = ''  # Starting string

        # Adding current key and value to the string, as an f-string
        txt += f'({self.key},{self.value}) '
        if self.left:

            # Recursively call itself on left node and
            # add everything on the left as f-strings
            txt += self.left.to_string()
        if self.right:
            # Do the same for right node
            txt += self.right.to_string()

        # Split the completed string by whitespace,
        # sort alphabetically, then join again
        txt = ' '.join((sorted(txt.split(' '), key=lambda e: e)))

        # return txt stripped of trailing whitespace + ' '
        return (txt + ' ').strip() + ' '

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

    def max_depth(self):  # Get maximum depth of any one branch

        # Starting depths
        depthL = 1
        depthR = 1

        # depthL += return value of recursive call on next left node
        # Same for right node, except depthR
        if self.left:
            depthL += self.left.max_depth()
        if self.right:
            depthR += self.right.max_depth()

        # Return depthR if depthL is less than depthR
        if depthL < depthR:
            return depthR

        # Return depthL otherwise
        else:
            return depthL

    def count_leafs(self):  # Counting every leaf (node with no children)

        count = 0  # Starting count is 0
        if not self.left and not self.right:
            count += 1  # += 1 if no children

        # Recursive call on both left and right child if they exist
        if self.left:
            count += self.left.count_leafs()
        if self.right:
            count += self.right.count_leafs()

        return count

    """
    Special list method for part 3
    Does same thing as as_lst, but sorts
    numerically instead of alphabetically
    and only returns keys greater than 4 in length
    """

    def as_sorted_lst(self, lst):

        # If value > 1 and length of key > 4
        if self.value > 1 and len(self.key) > 4:
            # Append key and value as a list
            lst.append([self.key, self.value])

        if self.left:  # If left branch exists
            self.left.as_sorted_lst(lst)  # Call itself recursively on left
        if self.right:  # If right branch exists
            self.right.as_sorted_lst(lst)  # Same thing for right

        return lst

    # We do a left-to-right in-order traversal of the tree
    # to get the key-value pairs sorted base on their keys
    def as_list(self, lst):

        # Append current key and value in a tuple to lst
        lst.append((self.key, self.value))

        if self.left:  # If left branch exists
            self.left.as_list(lst)  # Call itself recursively on left
        if self.right:  # If right branch exists
            self.right.as_list(lst)  # Same for right :UUU

        # Res = same as lst but sorted alphabetically
        res = list(sorted(lst, key=lambda i: i[0]))

        return res  # Return finished string of all elements


# The BstMap class is rather simple. It basically just takes care
# of the case when the map is empty. All other cases are delegated
# to the root node ==> the Node class.
# The class below is complete ==> not to be changed
@dataclass
class BstMap:
    root: Node = None

    def add(self, key, value):
        if self.root is None:
            self.root = Node(key, value, None, None)
            return 1
        else:
            return self.root.add(key, value)

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

    # r
    # w
    def count_leafs(self):
        if self.root is None:
            return 0
        else:
            return self.root.count_leafs()

    # Returns a sorted list of all key-value pairs in the map.
    # Each key-value pair is represented as a tuple and the
    # list is sorted on the keys ==> left-to-right in-order
    def as_sorted_lst(self):
        lst = []
        if self.root is None:
            return lst
        else:
            return list(sorted(self.root.as_sorted_lst(lst),
                        key=lambda i: i[1], reverse=True))

    def as_list(self):
        lst = []
        if self.root is None:
            return lst
        else:
            return self.root.as_list(lst)
