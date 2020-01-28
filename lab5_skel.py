# lab_skel.py
# October 3, 2018


"""
Part I: warm up exercises. Complete the functions below
"""

def sum_list(xs):
    """
    xs: list, a list of integers
    returns: int, sum of all elements in xs
    precondition: none (if list is empty, 0 should be returned)
    """
    pass
    acc=0
    for char in xs:
        acc=char+abc
    return acc

print(" ----- TEST sum_list ----- ")
print(sum_list([1,12,3,10]))
print(sum_list([4]))
print(sum_list([]))

def mul_list(xs):
    """
    xs: list, a list of integers
    returns: int, multiple of all elements in xs
    precondition: none (if list is empty, 1 should be returned)
    """
    pass
    acc=1
    for char in xs:
        acc=char*abc
    return acc
print(" ----- TEST mul_list ----- ")
print(mul_list([1,5,2,10]))
print(mul_list([4]))
print(mul_list([]))

def largest(xs):
    """
    xs: list, a list of integers
    returns: int, largest element in xs
    precondition: list is not empty
    """
    pass
    lar=xs[0]
    for char in xs:
        if lar>char:
            lar=lar
        else:
            lar=char
    return lar


print(" ----- TEST largest ----- ")
print(largest([1,5,2,10]))
print(largest([4]))
print(largest([60,1,-2,9,4]))


"""
Part II: working with lists
"""


"""
1. write a function that counts the number of palindromes in a list of
strings. You can use the function is_palindrome provided below.

Examples:
    >>> count_palindromes(['aba', 'abca', 'abccba'])
    2
    >>> count_palindromes(['abcdef'])
    0
    >>> count_palindromes([])
    0
    >>> count_palindromes([''])
    1

"""

def is_palindrome(s):
    """
    s: str
    returns: True if s is a palindrome and False otherwise
    precondition: none
    """
    reverse_s = ''
    for ch in s:
        # concatenate ch from the left
        reverse_s = ch + reverse_s
    return reverse_s==s

def count_palindromes(xs):
    """
    xs: list, list of strings
    returns: number of strings in xs that are a palindrome
    precondition: none
    """
    count=0
    for char in xs:

        if is_palindrome(char)==True:
            count+=1
        else:
            count=count
    return count
    pass # remove pass after implementing




"""
2. write a function is_common_member that takes two lists and returns True if
they have at least one common member.

Examples:
    >>> is_common_member([1,2,3],[4,5,6])
    False
    >>> is_common_member([1,2,3],[4,5,3,6])
    True
    >>> is_common_member([1,2,3],[])
    False
"""

def is_common_member(xs, ys):
    """
    xs: list, a list of integers
    ys: list, a list of integers
    returns: True if there is at least one number x that is in both xs and ys
    precondition: none
    """
    for char in xs:
        if char in ys:
            return True
    return False
    # YOUR CODE HERE
    pass # remove pass after implementing

print(" ----- TEST is_common_member -----")
print(is_common_member([1,2,3],[4,5,3,6]))


"""
3. write a function elim_reps that takes a list xs and returns a new list
containing the elements of xs without repetitions (in any order).

Note: xs should NOT be mutated.

Examples:
    >>> elim_reps([1,2,3,1,2,3,4])
    [1,2,3,4]
    >>> elim_reps([1,2,3,4])
    [1,2,3,4]
    >>> elim_reps([])
    []
"""


def elim_reps(xs):
    """
    xs: list
    returns: list, a list containing the elements of xs without repetitions. xs
    is not mutated.
    precondition: none
    """
    acc=[]
    for char in xs:
        if char in acc:
            acc=acc
        else:
            acc.append(char)
    return acc
    pass # remove pass after implementing

print(" ----- TEST elim_reps -----")

"""
4. write a function factors that takes a positive number n and return a list of
the factors of n, i.e. a list of numbers a such that a divides n without
remainder.

Examples:
    >>> factors(8)
    [1, 2, 4, 8]
    >>> factors(17)
    [1, 17]
    >>> factors(1)
    [1]
"""

def factors(n):
    """
    n: int, a positive integer
    returns: list, a list with factors of n
    precondition: none
    """
    acc=[]
    a=1
    while a<=n:
        if n%a==0:
            acc.append(a)
            a+=1
        else:
            a+=1
    return acc
    pass # remove pass after implementing



print(" ----- TEST factors -----")
print(factors(8))
"""
5. write a function fibonacci that takes a positive integer n and returns a
list with the first n terms of Fibonacci series.

The first two Fibonacci numbers are F_1=1, F_2=1, and for n>2, F_n  is given
by the sum of the two preceding numbers:
    F_n = F_{n-1} + F_{n-2}

Examples:
    >>> fibonacci(5)
    [1, 1, 2, 3, 5]
    >>> fibonacci(12)
    [ 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ]
    >>> fibonacci(1)
    [1]
    >>> fibonacci(2)
    [1, 1]

"""

def fibonacci(a):
    """
    n: int, a positive integer
    returns: list, a list with the first n terms of Fibonacci series
    precondition: n is positive
    """
    acc=[1,1]
    n=2
    if a<2:
        return [1]
    else:
        while n<a:
            acc.append(acc[n-2]+acc[n-1])
            n+=1
    return acc
    pass # remove pass after implementing


print(" ----- TEST fibonacci -----")
print(fibonacci(2))

"""
6. write a function prefixes that takes a string and returns a list of all
prefixes of s.

Examples:
    >>> prefixes('funny')
    ['', 'f', 'fu', 'fun', 'funn', 'funny']

"""
def prefixes(s):
    """
    s: str
    returns: list, a list of all prefixes of s
    precondition: none
    """
    acc1=""
    acc2=[""]
    for char in s:
        acc1=acc1+char
        acc2.append(acc1)

    return acc2

    pass # remove pass after implementing



print(" ----- TEST prefixes -----")



"""
7. write a function longest_upsequence that takes a list xs and returns the length
of the longest subsequence of xs that is strictly increasing (i.e. each member
is less than the next).

Examples:
    >>> longest_upsequence([1,2,0,1,2,-1])
    3
    >>> longest_upsequence([1,2,0,-1,5,2,3])
    2
    >>> longest_upsequence([8,7,6,5,4,3])
    1
    >>> longest_upsequence([1,2,0,1,2,3,4])
    5
"""

def longest_upsequence(xs):
    """
    xs: list, a list of integers
    returns: the length of the longest subsequence of xs that is strictly
    increasing
    precondition: xs is not empty
    """
    count=1
    lar=1
    acc=[]
    n1=0
    n2=0
    while n<len(xs):
        while xs(n)<xs(n+1):
            count+=1
            n2+=1
        if count>lar:
            lar=count
        else:
            lar=lar
        n1+=1
    return lar

    pass # remove pass after implementing


print(" ----- TEST longest_upsequence -----")
# TESTS HERE
print(longest_upsequence([1,2,0,-1,5,2,3]))

"""
8. (harder question, involves nested loops): write a function list_binary that
takes a positive integer n and returns a list of all binary strings of length n

Examples:
    >>> list_binary(2)
    ['00', '01', '10', '11']
    >>> list_binary(3)
    ['000', '001', '010', '011', '100', '101', '110', '111']
"""

def list_binary(n):
    """
    n: int, a positive integer
    returns: list, a list of all binary strings of length n
    precondition: n is positive
    """
    # YOUR CODE HERE
    pass # remove pass after implementing


print(" ----- TEST list_binary -----")
# TESTS HERE
