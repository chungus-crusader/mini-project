from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    value: Any = None
    left: Any = None
    right: Any = None

    def insert(self, num):
        if num < self.value:
            if not self.left:
                self.left = Node(num)
            else:
                self.left.insert(num)
        elif num > self.value:
            if not self.right:
                self.right = Node(num)
            else:
                self.right.insert(num)


@dataclass
class BST:
    def __init__(self, root=None):
        self.root = root

    def add(self, n):
        if not self.root:
            self.root = Node(n)
            return
        else:
            self.root.insert(n)


bi = BST()

bi.add(50)
bi.add(60)
bi.add(30)
print(bi.root)
print('A'.lower())
print('azc' < 'bdc')
print('Zoe' == 'Zoe')


five = 5

if five == 5:
    if five < 0:
        print('sus')
elif five > 0:
    print('additional sus')


print('Aa' > 'A')

