# hw3_skel.py
# Yufan Xu
# Professor Shai


"""
Instructions:
    1. do NOT change the name of the file (hw3_skel.py) before submitting
    2. make sure to test your functions by calling them
    3. in functions where the specification is not provided, you need to write it
    (specify parameters, what the function returns and precondition)
    4. you can use either while or for loops (whatever you find easier). If you
    don't feel comfortable with for loops yet, you can always use while (every
    for loop can be replaced with a while)
"""

"""
1. write a function remove_odds that given a string, s returns a copy of s
where all characters in odd positions are removed

Examples:
    >>> remove_odds('abcdefg')
    aceg
    >>> remove_odds('a')
    'a'
    >>> remove_odds('ab')
    'a'
    >>> remove_odds('')
    ''
"""


def remove_odds(s):
    """
    s: str
    returns: str, a copy of s where all characters in odd positions have been removed
    precondition: none
    """
    n=0
    acc=""
    while n<len(s):
        if n%2==0:
            acc=acc+s[n]
            n+=1
        else:
            acc=acc
            n+=1
    return acc
    pass



print("-------- TEST remove_odds --------")
print(remove_odds('abcdefg'))
print(remove_odds('a'))
print(remove_odds('ab'))
print(remove_odds(''))
# ADD MORE TESTS HERE


"""
2. write a function find_first_loc that given a string s and a character ch
returns the first location of ch in s. If ch is not in s, the function should
return -1

Examples:
    >>> find_first_loc('abracadabra', 'a')
    0
    >>> find_first_loc('abracadabra', 'b')
    1
    >>> find_first_loc('abracadabra', 't')
    -1

"""
def find_first_loc(s, ch):
    """
    ADD SPECIFICATION HERE
    """
    small=-1
    n=0
    for char in s:
        if char==ch:
            small=n
            return small
        else:
            n+=1
    return -1





    pass


print("-------- TEST find_first_loc --------")
print(find_first_loc('abracadabra', 'a'))
print(find_first_loc('abracadabra', 'b'))
print(find_first_loc('abracadabra', 't'))

# ADD MORE TESTS HERE

"""
3. write a function extract_third that given a string containing a comma-separated list of
names (where every name is a sequence of letters), returns the third name on the list.

    Examples:
    >>> extract_third('Alice,Bob,Carol,Chuck,Eve')
    Carol
    >>> extract_third('Alice,Bob,Carol')
    Carol

Note: you might want to use the function find_first_loc that you implemented
above

"""

def extract_third(s):
    """
    s:str, a list of names
    returns: str, the third name on the list
    precondition: s is a string of at least 3 names separated by a comma. Each
    name should be a non-empty sequence of letters
    """
    n=0
    num1=0
    num2=0
    acc=[]
    for char in s:
        n+=1
        if char==",":
            acc.append(n)
    if len(acc)==2:

        return s[acc[1]:n]
    else:
        return s[acc[1]:acc[2]-1]




    pass

print("-------- TEST extract_third --------")
print(extract_third('Alice,Bob,Carol,Chuck,Eve'))
print(extract_third('Alice,Bob,Carol'))


"""
4. write a function find_unique that given a string, s returns the first non-repeating character in s

Examples:
    >>> find_unique('abracadabra')
    c
    >>> find_unique('abcdabe')
    c
    >>> find_unique('abbb')
    a

Note: you might want to write a helper function count(s, ch) which takes a
string, s and a character, ch and returns the number of times that ch appears in
s. If you write a helper function, make sure to write its specification as well.

"""

def count(x,y):
    n=0
    for char in y:
        if char==x:
            n+=1
        else:
            n=n
    return n
'this is a helper '
def find_unique(s):
    """
    s: str
    returns: str, the first non-repeating character in s
    precondition: s has at least one non-repeating character
    """
    acc=[]
    for char in s:
        if count(char,s)==1:
            return char
        else:
            acc=acc


    pass

print("-------- TEST find_unique --------")
print(find_unique('abracadabra'))
print(find_unique('abcdabe'))
print(find_unique('abbb'))
# ADD MORE TESTS HERE
# ADD MORE TESTS HERE

"""
5. write a function largest_product that takes a string of digits, s and a
positive integer, n and returns the largest product of n consecutive digits
in s (like we did in lab, but with general n instead of 3)

Examples:
    >>> largest_product('162534', 1)
    6
    >>> largest_product('162534', 2)
    15
    >>> largest_product('162534', 3)
    60

Note: you might want to write a helper function that computes the product of n consecutive
digits in a string starting from the i-th position, i.e. int(s[i])*int(s[i+1])*...*int(s[i+n-1])
If you write a helper function, make sure to write its specification as well
"""
def helper(a,b,c):
    acc=1

    new=""
    new=a[b:c]
    for char in new:
        acc=acc*int(char)

    return acc

def largest_product(s, n):
    """
    s: str, a string of digits
    n: int, a positive integer
    returns: int, the largest product of n consecutive digits in s
    precondition: (s contains only digits) and (len(s)>=n) and (n>0)
    """
    lar=0
    a=0
    while a<len(s)-n:
        a+=1
        if lar>helper(s,a,a+n):
            lar=lar
        else:
            lar=helper(s,a,a+n)
    return lar
    pass

print("-------- TEST largest_product --------")
print(largest_product('162534', 1))
print(largest_product('162534', 2))
print(largest_product('162534', 3))
# ADD MORE TESTS HERE

"""
6. write the binding table stack associated with the code below (see example on
slide 3 in the class of Sep 20)
"""

def f(x):
    if x%2==0:
        res = x//2
    else:
        res = x*3+1
    return res

def g(x,y):
    if x>y:
        big=x
    else:
        big=y
    res = f(big)
    return res

x = 3
y = 5
res = g(x,y)

"""
Solution:

S = {}
S = { x -> 3}
S = { x -> 3, y -> 5}
S = { x -> 3, y -> 5},{ x -> 3, y -> 5}
S = { x -> 3, y -> 5},{ x -> 3, y -> 5, big -> 5}
S = { x -> 3, y -> 5},{ x -> 3, y -> 5, big -> 5},{ x ->5 }
S = { x -> 3, y -> 5},{ x -> 3, y -> 5, big -> 5},{ x ->5, res -> 16 }
.

"""
