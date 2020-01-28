# lab4_skel.py
# September 26, 2018

"""
1. complete the following function that takes a string, s and return a copy
of s in reverse.

Examples:
    >>> reverse('abc')
    'cba'
    >>> reverse('a')
    a
    >>> reverse('')
    ''
"""


def reverse(s):
    """
    s: str
    returns: str, s in reverse
    preconditions: none
    """
    acc=""
    for char in s:
        acc=char+acc
    return acc

    # the command 'pass' does nothing. It is just to prevent python from complaining
    # that there is no indented block under the function. You can remove it after you
    # are done implementing the function
    pass

"""
Now, call the function with various values of s and print the returned value
(see example below)
"""

# first, we call the function and put the returned value in a variable called 'res'
res = reverse('abc')

# then we print res
print(res)

# we can also do everything in one line
print(reverse('abc'))

"""
2. complete the following function that takes a string s and return True if
s is a palindrome and False otherwise.

Note: Palindrome is a string that reads the same backward as forward

You MUST use the function reverse(s) that you implemented in the previous
question

Examples:
    >>> is_palindrome('abc')
    False
    >>> is_palindrome('abccba')
    True
    >>> is_palindrome('abcba')
    True
    >>> is_palindrome('aa')
    True
    >>> is_palindrome('a')
    True
    >>> is_palindrome('')
    True
"""

def is_palindrome(s):
    """
    s: str
    returns: bool, True if s is a palindrome and False otherwise
    precondition: none
    """

    rev=reverse(s)
    if s==rev:
        return True
    else:
        return False

    pass

"""
now call the function with each of the examples above and make sure that your
function returns the write result (by printing it)
"""

print("-------- TEST is_palindrome --------")
print(is_palindrome('abc'))
print(is_palindrome('abccba'))
print(is_palindrome('abcba'))
print(is_palindrome('aa'))
print(is_palindrome('a'))
print(is_palindrome('≈'))



"""
3. write a function replace_with_dollars which takes a string, s and return a
copy of s where all occurrences of its first char have been changed to '$',
except the first char itself

You should write the function specifications as well

Examples:
    >>> replace_with_dollars('restart')
    'resta$t'
    >>> replace_with_dollars('abracadabra')
    'abr$c$d$br$'
    >>> replace_with_dollars('background')
    'background'
"""
def replace_with_dollars(s):
    """
    SPECIFICATION GOES HERE
    """
    # YOUR CODE GOES HERE
    list=[]
    acc=""
    for char in s:
        if char in list:
            acc=acc+"$"
        else:
            list.append(s[0])
            acc=acc+char
    return acc



    pass

print("-------- replace_with_dollars --------")
print(replace_with_dollars('restart'))
print(replace_with_dollars('abracadabra'))
print(replace_with_dollars('background'))

# ADD MORE TESTS HERE

"""
4. write a function find_subsequence that given a string seq and a substring subseq
returns the position of the first time that subseq appears in seq. If subseq is
not in seq the function should return -1

You should write the function specifications as well

Examples:
    >>> find_subsequence('hellohelloworld', 'lo')
    3
    >>> find_subsequence('hellohelloworld', 'rld')
    12
    >>> find_subsequence('hellohelloworld', 'rldz')
    -1
"""

def find_subsequence(seq, subseq):
    """
    SPECIFICATION GOES HERE
    """
    n=0
    len1=len(subseq)
    len2=len(seq)
    while n<len2-len1+1:
        if seq[n:n+len1]==subseq:
            return n
        else:
            n+=1
    return -1
    pass

print("-------- TEST find_subsequence --------")
print(find_subsequence('hellohelloworld', 'lo'))
print(find_subsequence('hellohelloworld', 'rld'))
print(find_subsequence('hellohelloworld', 'rldz'))

# ADD MORE TESTS HERE


"""
5. write a function that takes a string of digits, s and returns the largest
product of 3 consecutive digits

Examples:
    >>> largest_product_of_3('0123456')
    120
    >>> largest_product_of_3('612341')
    24
    >>> largest_product_of_3('11291137')
    21
"""

def largest_product_of_3(s):
    """
    s: str, a string of digits
    returns: largest product of 3 consecutive digits
    precondition: s has only digits and len(s) is at least 3
    """

    n=0
    lar=0
    while n<len(s)-2:
        if lar<int(s[n])*int(s[n+1])*int(s[n+2]):
            lar=int(s[n])*int(s[n+1])*int(s[n+2])
            n+=1
        else:
            lar=lar
            n+=1
    return lar

    pass

print("-------- largest_product_of_3 --------")
print(largest_product_of_3('612341'))
print(largest_product_of_3('0123456'))
print(largest_product_of_3('11291137'))

# ADD MORE TESTS HERE

"""
6. write a function that takes a quadratic equation of the form a*x**2+b*x+c
(where a,b,c are positive integers) and a number *x* and return the value of
the equation at *x*.

Examples:
    >>> evaluate_quad('5*x**2+167*x+11', 0)
    11
    >>> evaluate_quad('5*x**2+167*x+11', 1.5)
    272.75
    >>> evaluate_quad('1*x**2+0*x+11', 1)
    12
"""

def evaluate_quad(eq, x):
    """
    eq: str, a quadratic equation
    x: int or float, a number
    returns: float, the value of eq at x
    precondition: eq is of the form a*x**2+b*x+c where a,b,c are positive integers
    """
    acc=""

    for char in eq:
        if char=="x":
            acc=acc+str(x)
        else:
            acc=acc+char
    return eval(acc)


    pass

print("-------- TEST evaluate_quad --------")
print(evaluate_quad('5*x**2+167*x+11', 0))
print(evaluate_quad('5*x**2+167*x+11', 1.5))
print(evaluate_quad('1*x**2+0*x+11', 1))

# ADD MORE TESTS HERE

"""
7. the following function has a bug in it. Write down a set of test cases and
debug the function
"""

def buggy_find(s, ch):
    """
    s: str
    ch: str, a character
    returns: int, the location of the first appearance of ch in s or -1 if ch is
    not in s
    """
    found = False
    i = 0
    while not found and i<len(s):
        if s[i] == ch:
            found=True
        i+=1
        if found:
            return i
        else:
            return -1
