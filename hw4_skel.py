# hw4_skel.py
# WRITE YOUR NAME HERE


"""
Instructions:
    1. please do NOT change the name of the file (hw4_skel.py) before submitting
    2. remember to write down your name at the top of the file
    3. you are only allowed to use list methods discussed in class (i.e. len,
    append, insert, remove, pop, list concatenation and asking if something
    is in a list. if you need something else, just implement it yourself :)
    4. make sure to test your code!

"""

"""
1. (15 points) Write a function is_circularly_identical that returns
True if two given lists are circularly identical and False otherwise.

Note: if you compare two lists using the == operator, python will compare them
element by element (just like you expect). So the lists will be considered equal
only if they have the same number of elements, and each element of the first list
is equal to the element at the same position in the second list.

Examples:
    >>> is_circularly_identical([1,2,3,4,5], [3,4,5,1,2])
    True
    >>> is_circularly_identical([1,0], [0,1])
    True
    >>> is_circularly_identical([], [])
    True
    >>> is_circularly_identical([1], [1,2])
    False
    >>> is_circularly_identical([1,2,3], [3,2,1])
    False
"""

def is_circularly_identical(xs, ys):
    """
    xs: list
    ys: list
    returns: bool, True if xs and ys are circularly identical and False otherwise
    """
    acc=[]
    n=0
    xx=xs*2
    for i in(0,len(xx)):
        if ys==xx[i:i+len(xs)]:
            return True
    return False



    pass


print("----- TEST is_circularly_identical -----")
print(is_circularly_identical([1,2,3,4,5], [3,4,5,1,2]))

# ADD MORE TESTS HERE

"""
2. (15 points) Write a function is_sorted that returns True if a given
list is sorted in a strictly increasing order and False otherwise.

Note: an empty list is considered (vacuously) sorted.

Exampels:
    >>> is_sorted([1,2,3])
    True
    >>> is_sorted([1,2,2])
    False
    >>> is_sorted([3,2])
    False
    >>> is_sorted([3])
    True
    >>> is_sorted([])
    True

"""

def is_sorted(xs):
    """
    xs: list, a list of numbers
    returns: bool, True if xs is ordered in a strictly increasing order and
    False otherwise
    precondition: none
    """
    n=0
    while n<len(xs)-1:
        if xs[n]< xs[n+1]:
            n+=1
        else:
            return False
    return True
    pass


print("----- TEST is_sorted ----- ")
print(is_sorted([1,2,3]))
# ADD MORE TESTS HERE

"""
3. (15 points) Write a function min_loc that returns the location of the
smallest element in a list of numbers. If the smallest element appears more
than once, the function should return the position of its first occurrence.

Examples:
    >>> min_loc([1,2,3])
    0
    >>> min_loc([7,2,9,-1,4,53])
    3
    >>> min_loc([7,2,9,-1,4,53,-1])
    3

"""

def min_loc(xs):
    """
    xs: list, a list of numbers
    returns: int, the location of the smallest element in xs
    precondition: xs is not empty
    """
    small=xs[0]
    pos=0
    n=0
    while n<len(xs):
        if xs[n]<small:
            small=xs[n]
            pos=n

        else:
            small=small
        n+=1

    return pos
    pass

print("----- TEST min_loc -----")
print(min_loc([1,2,3]))
# ADD MORE TESTS HERE

"""
4. (20 points) Write a function list_primes that returns a list with all
prime numbers less than a given a positive integer n. You should use a helper
function is_prime that return True if a given positive integer is prime and
False otherwise.

Note (1): a prime number is a positive integer greater than 1 whose only factors
are 1 and itself

Note (2): to check if a number is prime, we have to test if it is divisible by
numbers between 2 and the square root of that number (inclusive). why? because
it it doesn't have a factor less than or equal to the square root, then it
doesn't have any factor. Think about that and make sure that your loop runs only
on numbers less than or equal to the square root of n.

Examples:
    >>> list_primes(16)
    [2, 3, 5, 7, 11, 13]
    >>> list_primes(17)
    [2, 3, 5, 7, 11, 13]
    >>> list_primes(1)
    []
    >>> list_primes(2)
    []
    >>> list_primes(3)
    [2]
    >>> list_primes(1000)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
    79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163,
    167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251,
    257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
    353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
    449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557,
    563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647,
    653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757,
    761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863,
    877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983,
    991, 997]

"""
def is_prime(n):
    """
    n: int, a positive integer
    returns: bool, True if n is prime and False otherwise
    precondition: n is a positive integer
    """
    for i in range(2,n-1):
        if n%i==0:
            return False

    return True

    pass

def list_primes(n):
    """
    n: int, a positive integer
    returns: list, a list will all prime numbers < n
    precondition: n is a positive integer
    """
    acc=[]
    for i in range(2,n):

        if is_prime(i)==True:
            acc.append(i)
    return acc
    pass

print("----- TEST list_primes -----")
print(list_primes(16))

# ADD MORE TESTS HERE

"""
5. (20 points) It was proposed by Christian Goldbach that every odd composite
number can be written as the sum of a prime and twice a square:

    9 = 7 + 2*(1**2)
    15 = 7 + 2*(2**2)
    21 = 3 + 2*(3**2)
    25 = 7 + 2*(3**2)
    27 = 19 + 2*(2**2)
    33 = 31 + 2*(1**2)

    But it turns out that the conjecture was false. Write a function that finds (and returns)
    the smallest (positive) odd composite that cannot be written as the sum of a prime and
    twice a square.

    You can use the function is_prime that you implemented above and you might
    want to write another helper function that returns True if a given number
    can be written as the sum of a prime and twice a square and False otherwise.

"""
def is_prime(n):
    """
    n: int, a positive integer
    returns: bool, True if n is prime and False otherwise
    precondition: n is a positive integer
    """
    i = 2
    if n < 0:
        return False

    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True

def list_primes(n):
    """
    n: int, a positive integer
    returns: list, a list will all prime numbers < n
    precondition: n is a positive integer
    """
    i = 2
    primes = []
    while i < n:
        if is_prime(i) == True:
            primes.append(i)
        i += 1
    return primes

primes = []

def checker(n):
    i = 1
    while i < n:
        if is_prime(n - (2*(i**2))):
            return True
        i += 1

    return False

def find_counter_example():
    """
    returns: the smallest odd composite number that can NOT be written as the sum of a
    prime and twice a square
    """
    i = 1
    while True and i < 6000:
        if is_prime(i) == False and checker(i) == False:
            return i
        else:
            i+=2

print("----- TEST find_counter_example -----")
print(find_counter_example())



"""
6. (15 points) Write down the binding table for the code below. Don't forget
that the loop variable in a for loop is a separate variable in the binding
table. For lists, write down the values of the list in the table (see example below).

Make sure that your answer is right by printing the variable values at the end.
"""

# Example:

x = 5
ys = []
xs = [1,2]
for x in xs:
    ys.append(x)

# Solution:

# {x -> 5}
# {x -> 5, ys -> []}
# {x -> 5, ys -> [], xs -> [1,2]}
# {x -> 1, ys -> [], xs -> [1,2]}
# {x -> 1, ys -> [1], xs -> [1,2]}
# {x -> 2, ys -> [1], xs -> [1,2]}
# {x -> 2, ys -> [1,2], xs -> [1,2]}


# Code:
xs = [1, 5, 3, 7]
ys = []
for x in xs:
    i = 0
    while i < len(ys) and ys[i] < x:
        i += 1
    ys.insert(i,x)

{xs = [1, 5, 3, 7]}
{xs -> [1, 5, 3, 7],ys -> []}
{xs -> [1, 5, 3, 7],ys -> [],x -> 1}
{xs -> [1, 5, 3, 7],ys -> [],x -> 1, i -> 0}
{xs -> [1, 5, 3, 7],ys -> [1],x -> 1, i -> 1}
{xs -> [1, 5, 3, 7],ys -> [1,5],x -> 5, i -> 1}
{xs -> [1, 5, 3, 7],ys -> [1,5],x -> 3, i -> 1}
{xs -> [1, 5, 3, 7],ys -> [1,3,5],x -> 3, i -> 1}
{xs -> [1, 5, 3, 7],ys -> [1,3,5],x -> 7, i -> 0}
{xs -> [1, 5, 3, 7],ys -> [1,3,5],x -> 7, i -> 1}
{xs -> [1, 5, 3, 7],ys -> [1,3,5],x -> 7, i -> 2}
{xs -> [1, 5, 3, 7],ys -> [1,3,5],x -> 7, i -> 3}
{xs -> [1, 5, 3, 7],ys -> [1,3,5,7],x -> 7, i -> 3}
