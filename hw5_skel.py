# hw5_skel.py
Derrick Xu
# DO NOT CHANGE THE FILE NAME PLEASE

"""
1. (25 points) Write a function is_id that takes a sorted list of integers
and return True if there is an element in the list whose value is equal to
its position.

Examples:

    -for the list xs = [-7,-4,-0,3,6,9], is_id(xs) should return True
    since xs[3] is equal to 3

    -for the list xs = [-7,-4,5,7,8], is_id(xs) should return False
    because there is no index i such that xs[i] is equal to i

Your function should have worst-case complexity of O(log n) where n is the
length of the list
"""


def is_id(xs):
    """
    xs: list, a sorted list of integers
    returns: bool, True if there is an i such that xs[i]=i
    precondition: xs is sorted in a non-decreasing order
    """
    n=len(xs)
    if xs==[]:
        return False
    elif xs[n//2]==n//2:
        return True
    elif xs[n//2]>n//2:
        return is_id(xs[:(n//2)])

    elif xs[n//2]<n//2:
        return is_id(xs[(n//2):])





print(is_id([-7,-4,-0,3,6,9]))
print(is_id([0,5,8,9,10,56]))
print(is_id([-5,-4,-3,-2,-1,0,2,4,8]))
print(is_id([1,3,5,7,9]))
# ADD MORE TESTS

"""
2. (25 points) Consider the code below that takes a positive integer n and
checks if n can be written as a sum of the first k positive integers (for sum k)

"""

def is_natural_sum_slow(n):
    """
    n: int, a positive integer
    returns: bool, True if n=1+2+...+k for some k
    precondition: none
    """
    numbers_sum = 0
    i = 1
    while(numbers_sum < n):
        numbers_sum += i
        i += 1

    if numbers_sum == n:
        return True

    return False

print(is_natural_sum_slow(15))
print(is_natural_sum_slow(20))

"""
The same function can be implemented more efficiently using the formula:
    1+2+...+k = (k*(k+1))//2

Use this formula to search (using binary search) for the right k.

Hint: think of 'mid' as 'k'

You function should have worst-case complexity O(log n)
"""

def list(n):
    xs=[]
    for char in range(n+1):
        xs.append(char)
    return xs
def is_natural_sum_fast(n):
    """
    n: int, a positive integer
    returns: bool, True if n=1+2+...+k for some k
    precondition: none
    """
    a=1
    b=n//2
    c=n
    while c>a:
        if b*(b+1)//2>n:
            c=b
            b=(a+c)//2

        elif (b*(b+1))//2<n:
            a=b+1
            b=(a+c)//2

        elif (b*(b+1))//2==n:
            return True
        elif n==1:
            return True
    return False

print(is_natural_sum_fast(15))




"""
3. (25 points) Selection sort is a sorting algorithm that works as follows:
each iteration i, we search for the minimum element in xs[i:] and place it in xs[i]

So for the list xs = [3,6,1,4,0], we would
    - search for the minimum element in [3,6,1,4,0] and put it in xs[0].
    The resulting list is [0,6,1,4,3]
    - then, we search for the minimum element in [6,1,4,3] and put it in xs[1].
    The resulting list is [0,1,6,4,3]
    - then, we search for the minimum element in [6,4,3] and put it in xs[2].
    The resulting list is [0,1,3,4,6]
    - then, we search for the minimum element in [4,6] and put it in xs[3].
    The resulting list is [0,1,3,4,6]

Implement the algorithm described above while maintaining the loop invariant.

You may want to use helper functions. As usual, you are NOT allowed to use
python list methods apart from the one discussed in class (append, remove, etc)

"""


def selection_sort(xs):###something wrong when xs = [3,5,6,6,6,5]
    """
    xs: list, a list of integers
    returns: nothing. xs is mutated such that at the end of the function it is
    sorted in non-decreasing order
    precondition: none
    """
    i = 0
    small=0
    small_index=0
    a=0
    while i<len(xs)-1:
        # LI: xs[k]<xs[k+1:] for all k in range(0,i)
        small=xs[i]
        small_index=0
        a=0
        while a< len(xs[i:]):
            if small<xs[a+i]:
                small=small
                
            else:
                small=xs[a+i]
                small_index=i+a
            a+=1
        tmp = xs[small_index]
        xs[small_index]=xs[i]
        xs[i] = tmp
        
        
        i+=1
 #      selection_sort(xs[i:])
    # post: xs[k]<xs[k+1:] for all k in range(0,len(xs))
    # => xs[0]<xs[1]<xs[2]<...<xs[len(xs)-1]
    return xs

xs = [3,6,2,1,5,7,8,6,7,8]
selection_sort(xs)
print(xs)


# ADD MORE TESTS

"""
4. (25 points) Complete the following problems from Lab 8 (see description in the lab skeleton):
"""

"""
Problem 1 (iv)
"""
# P: x < xs[h:100]
if x> xs[h-1]:
    x=xs[h-1]
# h = h - 1
# P: x < xs[h:100]


"""
Problem 2 (iii)
"""
# LI: i = k
k = 0
i = 0
while k <= 10000:
    k = k + 1
    i = i + 2


# SOLUTION: counter example: after the first iteration, i=2 and k=1. therefore, i!=k

"""
Problem 3 (iv)
"""
def is_prime(x):
    i = 2
    while i*i<=x:
        #Li:i<x
        if x%i==0:
            return False
        i+=1
    # if the x is not a prime number, then the loop return Falseself. otherwise
    #after the loop exited, the LI is still valid. the function will return True
    # =>    x is prime not determine it is not prime
    return True
