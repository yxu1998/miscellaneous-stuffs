# hw9_skel.py
# YOUR NAME


"""
In this assignment you are asked to implement a hash table that stores
usernames and passwords. Both usernames and passwords are strings. Usernames
are unique and should be used as keys. In order to hash a string you should
sum the value of its characters. To get the value of a character, you should
use the built-in function ord which takes a character and returns an integer
(its ascii code): https://docs.python.org/3/library/functions.html#ord

In part 1 you are asked to use separate chaining and in part 2 linear probing.

You may use any helper functions and helper classes.

You should write your own tests.
"""


"""
Part 1: separate chaining (50 points)
"""


class LoginSystemChaining(object):
    """
    Represents a hash table the stores usernames and passwords using separate
    chaining
    """
    def __init__(self, size):
        """
        size: int, positive integer
        """
        self.size = size
        self.table = []
        for i in range(self.size):
            self.table.append(LinkedList())


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

def new_user_chaining(system, username, password):
    """
    system: LoginSystemChaining
    username: str
    password: str
    returns: bool, indicating whether or not insertion was successful
    Note: insertion fails if the username already exists in the system
    """
    user=0
    pw=0
    pos=0
    
    for char in username:
        user+=ord(char)
    for char in password:
        pw+=ord(char)
    pos=user%system.size
    curr=system.table[pos].head
    i=[user,pw]
    
    while curr != None:
        if curr.value[0]==i[0]:
            return False
        curr=curr.next
    new_node=Node(i,None)
    
    temp=curr
    system.table[pos].head=new_node
    new_node.next=temp
    return True



def login_chaining(system, username, password):
    """
    system: LoginSystemChaining
    username: str
    password: str
    returns: bool, indicating whether or not login was successful
    Note: login fails if the username doesn't exist in the system or if the 
    password doesn't match the one stored in the system
    """
    user=0
    pw=0
    pos=0
    
    for char in username:
        user+=ord(char)
    for char in password:
        pw+=ord(char)
    pos=user%system.size
    curr=system.table[pos].head
    i=[user,pw]
    
    while curr != None:
        if curr.value[0]==user:
            if curr.value[1]==pw:
                return True
            else:
                return False
        curr=curr.next
    return False
    
def change_password_chaining(system, username, old_password, new_password):
    """
    system: LoginSystemChaining
    username: str
    old_password: str
    new_password: str
    returns: bool, indicating whether or not password was changed successfully
    Note: password change fails if the username doesn't exist in the system or
    if the old password given doesn't match the one stored in the system
    """
    user=0
    opw=0
    npw=0
    pos=0
    
    for char in username:
        user+=ord(char)
    for char in old_password:
        opw+=ord(char)
    for char in new_password:
        npw+=ord(char)
    pos=user%system.size
    curr=system.table[pos].head
    i=[user,opw]
    while curr is not None:
        if curr.value[0]==user:
            if curr.value[1]==opw:
               
                curr.value[1]=npw
                
                return True
            else:
                return False
        
        curr=curr.next
    return False

def reset_password_chaining(system, username):
    """
    system: LoginSystemChaining
    username: str
    returns: bool, indicating whether or not password was reset successfully
    password reset means reseting the password to '00password00'. This function
    fails if the username doesn't exist in the system
    """
    user=0
    opw=0
    npw=0
    pos=0
    
    for char in username:
        user+=ord(char)
    for char in "00password00":
        npw+=ord(char)
    pos=user%system.size
    curr=system.table[pos].head
    i=[user,opw]
    while curr is not None:
        if curr.value[0]==user:
            
            curr.value[1]=npw
            
            return True
        
        curr=curr.next
    return False

system=LoginSystemChaining(5) 
print(new_user_chaining(system, "xuyufan", "xuyufan"))
print(new_user_chaining(system, "xuyufan1", "xuyufanq1"))
print(new_user_chaining(system, "xuyufan1", "xuyufanq"))
print(login_chaining(system, "xuyufan1", "xuyufanq1"))
print(login_chaining(system, "xuyufan1", "xuyufan1988111"))
print(change_password_chaining(system,"xuyufan1", "xuyufanq1","xuyufan1988111"))
print(login_chaining(system, "xuyufan1", "xuyufan1988111")) 
print(reset_password_chaining(system, "xuyufan132"))



"""
Part 2: linear probing (50 points)
"""

class LoginSystemLinearProbing(object):
    """
    Represents a hash table the stores usernames and passwords using open
    addressing with linear probing
    """
    def __init__(self, size):
        """
        size: int, positive integer
        """
        self.size = size
        self.table = []
        for i in range(self.size):
            self.table.append(Entry(None, True, False))


class Entry(object):
    """
    Represents an entry in a hash with open addressing
    """
    def __init__(self, value, is_empty, is_deleted):
        """
        value: any object or None
        is_empty: bool
        is_deleted: bool
        """
        self.value = value
        self.is_empty = is_empty
        self.is_deleted = is_deleted



def new_user_probing(system, username, password):
    """
    system: LoginSystemLinearProbing
    username: str
    password: str
    returns: bool, indicating whether or not insertion was successful
    Note: insertion fails if the username already exists in the system
    """
    user=0
    pw=0

    for char in username:
        user+=ord(char)
    for char in password:
        pw+=ord(char)
    key=[user,pw]
    for i in range(system.size):
        pos=(user+i)%system.size
        
        if system.table[pos].is_empty or system.table[pos].is_deleted:
        
            system.table[pos] = Entry(key, False, False)
            return True
        elif system.table[pos].value[0]==user:
            
            return False
            
    
    

            



def login_probing(system, username, password):
    """
    system: LoginSystemLinearProbing
    username: str
    password: str
    returns: bool, indicating whether or not login was successful
    Note: login fails if the username doesn't exist in the system or if the 
    password doesn't match the one stored in the system
    """
    user=0
    pw=0
    for char in username:
        user+=ord(char)
    for char in password:
        pw+=ord(char)
    key=[user,pw]
    for i in range(system.size):
        pos=(user+i)%system.size
        if system.table[pos].value==[user,pw]:
            return True
        else:
            return False
         


def change_password_probing(system, username, old_password, new_password):
    """
    system: LoginSystemLinearProbing
    username: str
    old_password: str
    new_password: str
    returns: bool, indicating whether or not password was changed successfully
    Note: password change fails if the username doesn't exist in the system or
    if the old password given doesn't match the one stored in the system
    """
    user=0
    opw=0
    npw=0
    for char in username:
        user+=ord(char)
    for char in old_password:
        opw+=ord(char)
    for char in new_password:
        npw+=ord(char)
    
    key=[user,opw]
    for i in range(system.size):
        pos=(user+i)%system.size
        if system.table[pos].value==key:
            system.table[pos].value==[user,npw]
            return True
        
    return False


def reset_password_probing(system, username):
    """
    system: LoginSystemLinearProbing
    username: str
    returns: bool, indicating whether or not password was reset successfully
    password reset means reseting the password to '00password00'. This function
    fails if the username doesn't exist in the system
    """
    user=0
    
    npw=0
    for char in username:
        user+=ord(char)
    for char in "00password00":
        npw+=ord(char)

    for i in range(system.size):
        pos=(user+i)%system.size
        if system.table[pos].is_empty or system.table[pos].is_deleted:
            return False
        elif system.table[pos].value[0]==user:
            
            system.table[pos].value=[user,npw]
            
            return True
        
    return False


system=LoginSystemLinearProbing(5)
print(new_user_probing(system,"xuyufan1","xuyufan1"))
print(reset_password_probing(system,"xuyufan2"))
print(login_probing(system, "xuyufan1", "00password00"))
