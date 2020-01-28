class LinkedList(object):
    """
    Represents a singly linked list with integer labels
    """
    def __init__(self, first, rest):
        """
        first: int
        rest: LinkedList or None
        """
        self.first= first
        self.rest = rest

"""
(15 points) Implement a recursive function count that counts the number of occurrences of a
given integer x in a linked list xs. You may NOT use a Python list or a loop in your code.
"""

def count(xs, x):
    """
    xs: LinkedList
    x: int
    returns: int, number of times x appears in xs
    """
    if xs.rest == None:
        return 0
    elif xs.value == x:
        return 1 + count(xs.rest, x)
    else:
        return count(xs.rest, x)

# creating the list 4 -> 7 -> 2 -> 4 -> 5
node1 = LinkedList(5, None)
node2 = LinkedList(4, node1)
node3 = LinkedList(2, node2)
node4 = LinkedList(7, node3)
node5 = LinkedList(4, node4)

print(count(node5, 7)) # 1
print(count(node5, 4)) # 2
print(count(node5, 1)) # 0
