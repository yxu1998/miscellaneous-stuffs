# hw8_skel.py
# Derrick Xu

class Node(object):
    """
    Represents a singly-linked node
    """
    def __init__(self, value, next_node):
        self.value = value
        self.next = next_node

class LinkedList(object):
    """
    Represents a singly-linked list
    """
    def __init__(self):
        self.head = None

def is_empty(lst):
    """
    lst: LinkedList
    returns: bool, True if lst is empty (has no nodes) and False otherwise
    """
    return lst.head is None

def insert_front(lst, val):
    """
    lst: LinkedList
    val: int
    returns: nothing. lst is mutated such that a node with value val is the
    first node
    """
    new_node = Node(val,None)
    new_node.next = lst.head
    lst.head = new_node

def insert_after_node(node, val):
    """
    node: Node
    val: int
    returns: nothing. Node is being mutated to link to a new node with value
    val
    """
    new_node = Node(val, None)
    new_node.next = node.next
    node.next = new_node

def insert_in_position(lst, val, pos):
    """
    lst: LinkedList
    val: int
    pos: int, position in the list where new node should be inserted
    returns: nothing.  lst is mutated  such that a node with value val is added
    in position pos
    precondition: pos is a valid position (i.e. non-negative and <= than the
    list length)
    """
    if pos == 0:
        insert_front(lst, val)
        return
    i = 0
    curr  = lst.head
    while curr is not None and i < pos-1:
        i = i+1
        curr = curr.next

    # according to the precondition curr should not be None,
    # but let's check just in case
    if curr is not None:
         insert_after_node(curr, val)


def list_to_str(lst):
    """
    lst: LinkedList
    returns: str, string representation of lst
    """
    curr = lst.head
    s = ' '
    while curr is not None:
        s = s + str(curr.value) + ' -> '
        curr = curr.next
    s = s + 'None'
    return s


"""
Part I: practice problems (not graded). Solutions available on Moodle
"""

def insert_in_position_recur(lst, val, pos):
    """
    same as insert_in_position but with no loop
    """
    if pos == 0:
        insert_front(lst, val)
    elif pos == 1:
        insert_after_node(lst.head, val)
    else:
        short_list = LinkedList()
        short_list.head = lst.head.next
        insert_in_position_recur(short_list, val, pos-1)

# UNCOMMENT FOLLOWING LINES TO TEST
#lst = LinkedList()
#insert_front(lst, 1)
#insert_front(lst, 8)
#insert_front(lst, 2)
#insert_front(lst, 3)
#insert_in_position_recur(lst, -5, 2) #  3 -> 2 -> -5 -> 8 -> 1 -> None
#print(list_to_str(lst))
#insert_in_position_recur(lst, -10, 0) #  -10 -> 3 -> 2 -> -5 -> 8 -> 1 -> None
#print(list_to_str(lst))
#insert_in_position_recur(lst, -20, 6) #  -10 -> 3 -> 2 -> -5 -> 8 -> 1 -> -20 -> None
#print(list_to_str(lst))

def int_to_list(num):
    """
    num: int, non-negative integer
    returns: LinkedList, the digits of num
    """


# UNCOMMENT FOLLOWING LINES TO TEST
#print(list_to_str(int_to_list(147))) # 1 -> 4 -> 7 -> None
#print(list_to_str(int_to_list(4))) #  4 -> None
#print(list_to_str(int_to_list(9148))) #  9 -> 1 -> 4 -> 8 -> None
#print(list_to_str(int_to_list(0))) #. None

def only_events(lst):
    """
    lst: LinkedList
    returns: LinkedList, a list with only the elements in lst that are even

    IMPORTANT: you are not allowed to create new nodes, i.e. no calls
    to Node constructor are allowed (including via a helper function).
    Also, you are not allowed to change the value of any of the nodes.
    In other words, you are only allowed to change the 'next' attribute
    """
    pass

# UNCOMMENT FOLLOWING LINES TO TEST
#lst = LinkedList()
#insert_front(lst, 12)
#insert_front(lst, 11)
#insert_front(lst, 8)
#insert_front(lst, 4)
#insert_front(lst, 1)
#print(list_to_str(only_events (lst))) # 4 -> 8 -> 12 -> None

#lst = LinkedList()
#insert_front(lst, 12)
#insert_front(lst, 11)
#insert_front(lst, 8)
#insert_front(lst, 4)
#insert_front(lst, 2)
#print(list_to_str(only_events (lst))) # 2 -> 4 -> 8 -> 12 -> None

#lst = LinkedList()
#insert_front(lst, 9)
#insert_front(lst, 11)
#insert_front(lst, 8)
#insert_front(lst, 4)
#insert_front(lst, 2)
#print(list_to_str(only_events (lst))) # 2 -> 4 -> 8 -> None

def concatenate(lst1, lst2):
    """
    lst1: LinkedList
    lst2: LinkedList
    returns: LinkedList, list obtained by concatenating lst1 and lst2

    IMPORTANT: you are not allowed to create new nodes, i.e. no calls
    to Node constructor are allowed (including via a helper function).
    Also, you are not allowed to change the value of any of the nodes.
    In other words, you are only allowed to change the 'next' attribute
    """
    pass


# UNCOMMENT FOLLOWING LINES TO TEST
#lst1 = LinkedList()
#insert_front(lst1, 3)
#insert_front(lst1, 2)
#insert_front(lst1, 1)
#lst2 = LinkedList()
#insert_front(lst2, 10)
#insert_front(lst2, 20)
#print(list_to_str(concatenate(lst1, lst2))) # 1 -> 2 -> 3 -> 20 -> 10 -> None

#lst1 = LinkedList()
#insert_front(lst1, 3)
#insert_front(lst1, 2)
#insert_front(lst1, 1)
#lst2 = LinkedList()
#print(list_to_str(concatenate(lst1, lst2))) # 1 -> 2 -> 3 -> None

#lst1 = LinkedList()
#lst2 = LinkedList()
#insert_front(lst2, 3)
#insert_front(lst2, 2)
#insert_front(lst2, 1)
#print(list_to_str(concatenate(lst1, lst2))) #  1 -> 2 -> 3 -> None


"""
Part II: Graded problems (25 points each)
"""


def insert_in_place(lst, x):
    """
    lst: LinkedList, a sorted list (increasing order)
    x: int
    returns: nothing. x is inserted to lst in  the right place
    """
    curr=lst.head
    if lst.head== None:
        insert_front(curr, x)
    else:
        while curr is not None:
            if curr.next is None:
                if curr.value>x:
                    print('1')
                    insert_after_node(prev, x)
                    break
                else:
                    insert_after_node(curr, x)
                    break
            else:
                if curr.value>x:
                    print(curr.value)
                    print('3')
                    insert_front(lst, x)
                    break
                else:
                    print('4')
                    prev=curr
                    curr=curr.next








# UNCOMMENT FOLLOWING LINES TO TEST
#lst = LinkedList()
#insert_front(lst, 8)
#insert_front(lst, 3)
#insert_front(lst, 2)
#insert_front(lst, 1)
#insert_in_place(lst, 5)
#print(list_to_str(lst)) #  1 -> 2 -> 3 -> 5 -> 8 -> None

#lst = LinkedList()
#insert_front(lst, 3)
#insert_front(lst, 2)
#insert_front(lst, 1)
#insert_in_place(lst, 5)
#print(list_to_str(lst)) #  1 -> 2 -> 3 -> 5 -> None

#lst = LinkedList()
#insert_front(lst, 3)
#insert_front(lst, 2)
#insert_front(lst, 1)
#insert_in_place(lst, 0)
#print(list_to_str(lst)) #  0 -> 1 -> 2 -> 3 -> None


def interleave(lst1, lst2):
    """
    lst1: LinkedList
    lst2: LinkedList
    returns: LinkedList, list obtained by interleaving lst1 and lst2
    and tucking leftovers at the end.

    IMPORTANT: you are not allowed to create new nodes, i.e. no calls
    to Node constructor are allowed (including via a helper function).
    Also, you are not allowed to change the value of any of the nodes.
    In other words, you are only allowed to change the 'next' attribute
    """
    i=0
    lst = LinkedList()
    curr1=lst1.head
    curr2=lst2.head
    next1=curr1.next
    next2=curr2.next
    lst.head=lst1.head
    curr_lst=lst.head
    curr1=curr1.next
    while curr1 != None or curr2 !=None:
        
        if curr2 != None:
            next2 = curr2.next
            curr_lst.next=curr2
            curr2=next2
            
            curr_lst=curr_lst.next
            
        if curr1 !=None:
            next1=curr1.next
            curr_lst.next=curr1
            
            curr1=next1
    
            curr_lst=curr_lst.next
            
        
    return lst

# UNCOMMENT FOLLOWING LINES TO TEST
lst1 = LinkedList()
insert_front(lst1, 3)
insert_front(lst1, 2)
insert_front(lst1, 1)
lst2 = LinkedList()
insert_front(lst2, 'c')
insert_front(lst2, 'b')
insert_front(lst2, 'a')
print(list_to_str(interleave(lst1, lst2))) #  1 -> a -> 2 -> b -> 3 -> c -> None

lst1 = LinkedList()
insert_front(lst1, 5)
insert_front(lst1, 4)
insert_front(lst1, 3)
insert_front(lst1, 2)
insert_front(lst1, 1)
lst2 = LinkedList()
insert_front(lst2, 'c')
insert_front(lst2, 'b')
insert_front(lst2, 'a')
print(list_to_str(interleave(lst1, lst2))) #  1 -> a -> 2 -> b -> 3 -> c -> 4 -> 5 -> None

lst1 = LinkedList()
insert_front(lst1, 3)
insert_front(lst1, 2)
insert_front(lst1, 1)
lst2 = LinkedList()
insert_front(lst2, 'e')
insert_front(lst2, 'd')
insert_front(lst2, 'c')
insert_front(lst2, 'b')
insert_front(lst2, 'a')
print(list_to_str(interleave(lst1, lst2))) #  1 -> a -> 2 -> b -> 3 -> c -> d -> e -> None

def deal(lst):
    """
    lst: LinkedList
    returns: (LinkedList,LinkedList) two linked lists obtained by
    dealing the elements of lst into odd and even positions (see examples below)

    IMPORTANT: you are not allowed to create new nodes, i.e. no calls
    to Node constructor are allowed (including via a helper function).
    Also, you are not allowed to change the value of any of the nodes.
    In other words, you are only allowed to change the 'next' attribute
    """
    lst1= LinkedList()
    lst2= LinkedList()
    curr1=lst1.head
    curr2=lst2.head
    
    curr=lst.head
    if lst.head is None:
        return (lst1,lst2)
    if lst.head.next is None:
        return (lst,lst2)
    lst1.head=lst.head
    lst2.head=lst.head.next
    curr=lst.head
    while curr.next != None:
        
        temp = curr.next
        curr.next = curr.next.next
        curr = temp

    return(lst1,lst2)

# UNCOMMENT FOLLOWING LINES TO TEST
lst = LinkedList()
insert_front(lst, 6)
insert_front(lst, 5)
insert_front(lst, 4)
insert_front(lst, 3)
insert_front(lst, 2)
insert_front(lst, 1)
lst1, lst2 = deal(lst)
print(list_to_str(lst1)) # 1 -> 3 -> 5 -> None
print(list_to_str(lst2)) # 2 -> 4 -> 6 -> None

#lst = LinkedList()
insert_front(lst, 5)
insert_front(lst, 4)
insert_front(lst, 3)
insert_front(lst, 2)
insert_front(lst, 1)
lst1, lst2 = deal(lst)
print(list_to_str(lst1)) # 1 -> 3 -> 5 -> None
print(list_to_str(lst2)) # 2 -> 4 -> None

lst = LinkedList()
insert_front(lst, 10)
lst1, lst2 = deal(lst)
print(list_to_str(lst1)) # 10 -> None
print(list_to_str(lst2)) # None


def swap(lst, i, j):
    """
    lst: LinkedList
    i, j: int
    returns: nothing. swaps the elements in positions i and j
    precondition: i and j are valid indices and i < j

    IMPORTANT: you are not allowed to create new nodes, i.e. no calls
    to Node constructor are allowed (including via a helper function).
    Also, you are not allowed to change the value of any of the nodes.
    In other words, you are only allowed to change the 'next' attribute
    """
    if i == j:
        return

       # Search for x (keep track of prevX and CurrX)
    previ = None
    curri = lst.head
    while curri != None and curri.value != i:
        previ = curri
        curri = curri.next
        
    # Search for y (keep track of prevY and currY)
    prevj = None
    currj = lst.head
    while currj != None and currj.value != j:
        prevj = currj
        currj = currj.next
    # If either x or y is not present, nothing to do
    if curri == None or curri == None:
        return
    # If x is not head of linked list
    if previ != None:
        previ.next = currj
    else: #m
        lst.head = currj

        # If y is not head of linked list
    if prevj != None:
        prevj.next = curri
    else: # make x the new head
        lst.head = curri

        # Swap next pointers
    temp = curri.next
    curri.next = curri.next
    currj.next = temp

# UNCOMMENT FOLLOWING LINES TO TEST
lst = LinkedList()
insert_front(lst, 6)
insert_front(lst, 5)
insert_front(lst, 4)
insert_front(lst, 3)
insert_front(lst, 2)
insert_front(lst, 1)
insert_front(lst, 0)
swap(lst, 2, 4)
print(list_to_str(lst)) # 0 -> 1 -> 4 -> 3 -> 2 -> 5 -> 6 -> None
swap(lst, 0, 3)
print(list_to_str(lst)) # 3 -> 1 -> 4 -> 0 -> 2 -> 5 -> 6 -> None
swap(lst, 0, 6)
print(list_to_str(lst)) # 6 -> 1 -> 4 -> 0 -> 2 -> 5 -> 3 -> None
swap(lst, 5, 6)
print(list_to_str(lst)) # 6 -> 1 -> 4 -> 0 -> 2 -> 3 -> 5 -> None
swap(lst, 0, 1)
print(list_to_str(lst)) # 1 -> 6 -> 4 -> 0 -> 2 -> 3 -> 5 -> None

