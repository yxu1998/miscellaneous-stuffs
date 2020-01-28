# hw6_skel.py
#Derrick Xu

"""
All the functions in this homework must be implemented recursively.
"""

"""
1. write a recursive function is_palindrome that given a string, s returns
True if s is a palindrome and False otherwise. Recall that a palindrome is
a string that reads the same backward as forward.
"""
def is_palindrome(s):
    """
    s: str
    returns: True if s is a palindrome and False otherwise
    precondition: none
    """
    if s=="":
        return True
    elif s[0]==s[-1]:
        return is_palindrome(s[1:-1])
    elif s[0]!=s[-1]:
        return False
        return is_palindrome(s[0:-1])

print(is_palindrome('abcba'))  # True
print(is_palindrome('abccba')) # True
print(is_palindrome('acba'))   # False
print(is_palindrome('accba'))  # False


"""
2. write a recursive function min_loc that given a list of integers returns the
position of the smallest element
"""

def min_loc(xs):
    """
    xs: list, a list of integers
    returns: int, i such that xs[i]<=xs
    precondition: xs is not empty
    """
    small=999
    n=-1
    small_index=0
    while len(xs)!=0:
        if small>xs[0]:

            n+=1
            small=xs[0]
            small_index=n
            xs=xs[1:]


        elif small<xs[0]:

            n+=1
            small=small
            xs=xs[1:]

    return small_index
print(min_loc([0,7,8,1,2,4]))  # 0
print(min_loc([0,7,8,1,2,-4])) # 5
print(min_loc([0,7,-8,1,2,4])) # 2

"""
3. write a recursive implementation for binary search. It should have both the same
functionality and the same complexity i.e. O(logn), as binary search
"""


def binary_search(xs, x):
    """
    xs: list, a list of integers
    x: int
    returns: int, i such that xs[i]=x or -1 if x is not in xs
    precondition: xs is sorted in increasing order
    """
    n=len(xs)

    if x not in xs:
        return -1
    elif xs[n//2]==x:

        return n//2
    elif xs[n//2]<x:

        return binary_search(xs[n//2:], x)+len(xs)//2
    elif xs[n//2]>x:

        return binary_search(xs[0:n//2], x)

print(binary_search([1,4,6,8,9,10,12,15,20], 6))  # 2
print(binary_search([1,4,6,8,9,10,12,15,20], 5))  # -1
print(binary_search([1,4,6,8,9,10,12,15,20], 15)) # 7

"""
4. write a recursive function all_words that given a list of characters (without duplicates), chars_list
returns a list of all possible words of length k that can be written using the characters in chars_list.

For example, all_words(['a','b','c'], 2) should return a list with the elements
	'aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc'
in some order
"""
def helper(xs,x):
    acc=[]
    for char in xs:
        acc.append(x+char)
    return acc

def all_words(chars_list, k):
    """
    chars_list: list, a list of distinct characters
    k: int
    returns: list, a list with all words of k characters from chars_list
    precondition: k >= 0
    """
    acc=[]
    if k==0:

        return [""]
    else:
        for char in chars_list:
            acc+=helper(all_words(chars_list,k-1),char)



        return acc


print(all_words(['a','b','c'], 0)) # ['']
print(all_words(['a','b','c'], 1)) # ['a', 'b', 'c']
print(all_words(['a','b','c'], 2)) # ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']
print(all_words(['a','b'], 3))     # ['aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb']



"""
5. write a recursive function is_reachable that given a source, src and a target, trg, determines
if you can reach from src to trg if at each step i you can move i positions either left or right.

For example, to reach from 0 to 5 you can take the following steps:
0 -> 1 -> 3 -> 0 -> 4 -> -1 -> 5

"""

def is_reachable(src, trg, i):
    """
    src: int, starting position
    trg: int, target position
    returns: bool, True if trg is reachable from src (according the rules described in the question)
    precondition: none
    """
    if src==trg:
        return True
    elif src>trg:
        return False
    else:
        if True:
            return is_reachable(src+i+1, trg, i+1) or is_reachable(src-i-1, trg, i+1)


# you can assume in your testing that the function always starts with src=0 and i=0
print(is_reachable(0, 0, 0)) # True
print(is_reachable(0, 1, 0)) # True
print(is_reachable(0, 2, 0)) # True
print(is_reachable(0, 3, 0)) # True
print(is_reachable(0, 4, 0)) # True
print(is_reachable(0, 5, 0)) # True
print(is_reachable(0, 6, 0)) # True

"""
6. One can prove that it's always possible to get from 0 to any target using the rules from question 5. How? Think about it!

Now, write a recursive function that finds what is the *smallest* number of steps required to get from src to trg

"""

def min_steps(src,trg,i):
   
    if (src-trg)%2!=0:
        return i+1
    elif src==trg:
        return i
    else:
        return min_steps(src+i+1,trg,i+1) or min_steps(src-i-1,trg,i-1)


# you can assume in your testing that the function always starts with src=0 and i=0
print(min_steps(0, 3, 0))  # 2
print(min_steps(0, 11, 0)) # 5
print(min_steps(0, 17, 0)) # 6
print(min_steps(0, 20, 0)) # 7
