# lab6_skel.py
# October 10, 2018

"""
Recall the big-O facts:

- O(1) ⊂ O(log n) ⊂ O(n) ⊂ O(n log n) ⊂ O(n2) ⊂ O(n3) ⊂ . . .

- To find the big-O, you ignore constants and take the dominant factor

- If we ask for a “tight big-O bound”, that means to give the smallest
  big-O bound that you can from the above list of options
  (e.g. don’t say O(n2) if it is also O(n))
"""

"""
One more thing, when we write log(n) we mean log with base 2 unless mentioned
otherwise
"""


"""
Problem 1: for each of the expressions below, select the dominant term and
specify the lowest Big-Oh complexity (see example)
"""

# 1. n^2+100n                   is n^2(?)
# 2. 0.01n + 100n^2             is n^2(?)
# 3. 100n + 0.01n^2             is n^2(?)
# 4. 100n logn + n^3 + 100n     is n^3(?)
# 5. 0.3n + 5n logn + 2.5 n^2   is n^2(?)
# 6. n logn + (logn)^2          is nlogn(?)


"""
Problem 2: what is the worst-case complexity of the functions below
(as a function of N)?
"""

def func1():
    i = N
    while i>0:
        print(i) # one step
        i = i-1  # one step

"""
1. the loop runs __n_ iterations
2. each iteration takes __2_ steps
3. therefore, func1 takes ___2n+1 steps
4. the worst-case complexity of func1 is O(_n_)
"""

def func2():
    i = 0 # one step
    while i < N: # loop1
        j = 0 # one step
        while j < N: # loop2
            print(i,j) # one step
            j = j+1    # one step
        i=i+1 # one step

"""
solution:
loop 1 run n time
each iteration takes 2+2n steps
fuc2 take n(2+2n)
the worst-case complexity of fuc2 is O(n^2)
"""

def func3():
    i = 0 # one step
    j = 0 # one step
    while i < N: # loop1
        while j < N: # loop2
            print(i,j) # one step
            j = j+1 # one step
        i=i+1 # one step



"""
solution:
1. the loop runs __n_ iterations
2. each iteration takes __2+2n_ steps
3. therefore, func1 takes ___n(2n+1) steps
4. the worst-case complexity of func1 is O(_n^2_)
"""

def func4():
    i = 0 # one step
    while i < N: # loop1
        j = i # one step
        while j < N: # loop2
            print(i,j) # one step
            j = j+1 # one step
        i=i+1 # one step



"""
solution:
1. the loop runs __N_ iterations
2. the first iteration takes 2N+2
3. the second iteration takes 2(N-1)+2
..
..
4. he Nth iteration takes 2(1)+2
5. so the entire thing takes 2N+2+2(N-1)+2 + ... + 2(1)+2 = N(N-1)+2N = O(N^2)



each iteration takes __2+(2(n(n-1))/2)_ steps
3. therefore, func1 takes ___n(2+(2(n(n-1))/2)) steps
4. the worst-case complexity of func1 is O(_n^3_)
"""

def func5(x):
    my_sum = 0
    if (x>0):
        for i in range(N):
            my_sum = my_sum + i # one step
            print(i) # one step
            print(my_sum) # one step
    else:
        print('x is not positive', x) # one step
        my_sum = 7 # one step

    return my_sum


"""
solution:
1. the loop runs __n_ iterations
2. each iteration takes __3_ steps
3. therefore, func1 takes ___3n steps
4. the worst-case complexity of func1 is O(_n_)
"""

"""
At this point, you can even start ignoring steps and just say something like
"each iteration of the loop takes O(1) steps so the loop taken O(N) steps" or
"each iteration of the loop takes O(N) steps so the loop taken O(N^2) steps"
"""

"""
Problem 3: for each of the functions below, what is the maximum number of iterations
that the loop runs (in the worst-case)?
"""

def gcd(x,y):
    """
    x: int, a positive integer
    y: int, a positive integer
    returns: int, he greatest common divisor of x and y
    """
    if x > y:
        small = y
    else:
        small = x
    i = 1
    while i <= small:
        if x%i == 0 and y%i == 0:
            gcd = i
        i+=1
    return gcd
small-1 times

def lcm(x,y):
    """
    x: int, a positive integer
    y: int, a positive integer
    returns: int, the least common multiple of x and y
    """
    if x > y:
        big = x
    else:
        big = y
    i = big
    while i<x*y:
        if i%x == 0 and i%y == 0:
            return i
        i += big
    return x*y
(xy-big)/big

def is_prime(x):
    """
    x: int, a positive integer
    returns: bool, True if x is prime and False otherwise
    """
    i = 2
    while i*i<=x:
        if x%i==0:
            return False
        i+=1
    return True

sqrt(x)-2
def sum_list(xs):
    """
    xs: list, a list of integers
    returns: int, sum of all elements in the list or 0 if xs is empty
    """
    s = 0
    for x in xs:
        s += x
    return s

len(xs)
def find_largest(xs):
    """
    xs: list, a list of integers
    returns: int, the largest element in xs
    precondition: xs is not empty
    """
    largest = xs[0]
    for i in range(1,len(xs)):
        if xs[i] > largest:
            largest = xs[i]
    return largest
len(xs)-1

def is_even_in_list(xs):
    """
    xs: list, a list of integers
    returns: bool, True if xs has at least one even number and False otherwise
    """
    for x in xs:
        if x%2==0:
            return True
    return False
len(xs)


"""
Problem 4: complexity of code with function calls

Assume that the worst-case complexity of python list methods is given by:
    append  - O(1)
    insert  - O(n)
    remove  - O(n)
    pop     - O(n)
    x in xs - O(n)

For each of the problems below, first characterize the worst-case argument and
then analyze their complexity
"""

def is_common_member(xs, ys):
    """
    xs: list, a list of integers
    ys: list, a list of integers
    returns: True if there is at least one number x that is in both xs and ys
    precondition: none
    """
    for x in xs:
        if x in ys:
            return True
    return False


"""
worst-case arguments: nothing in common for xs and ys

complexity (should be function of N and M where len(xs)=N and len(ys)=M):  o(NM)

"""

def elim_reps(xs):
    """
    xs: list
    returns: list, a list containing the elements of xs without repetitions. xs
    is not mutated.
    precondition: none
    """
    res = []
    for x in xs:
        if x not in res:
            res.append(x)
    return res

"""
worst-case argument: xs has not repetition

complexity (as a function of n=len(xs)): 


"""

def longest_upsequence(xs):
    """
    xs: list, a list of integers
    returns: the length of the longest subsequence of xs that is strictly
    increasing
    precondition: xs is not empty
    """
    largest = 1
    current = 1
    i = 1
    while i < len(xs):
        if xs[i] > xs[i-1]:
            # sequence keeps increasing
            current += 1
        else:
            # sequence just stopped
            current = 1

        if current > largest:
            largest = current

        i += 1

    return largest

"""
worst-case argument:

complexity (as a function of n=len(xs)):

"""


"""
problem 5: implementation
"""

"""
consider the function below that takes a sorted list of n-1 integers
between 0 and n and the function should find the missing integer
(i.e. the only integer between 0 and n that is not in the list)

"""

def find_missing_number_slow(xs):
    """
    xs: list, a list of n-1 integers between 0 and n (including n)
    returns: int, the missing integer
    precondition: xs is sorted in an increasing order
    """
    for i in range(len(xs)):
        if xs[i]>i+1:
            return i+1
    return len(xs)+1

print(find_missing_number_slow([1, 2, 3, 4, 6, 7, 8]))
print(find_missing_number_slow([2, 3, 4, 5, 6, 7, 8]))
print(find_missing_number_slow([1, 2, 3, 4, 5, 6, 7]))

"""
what is the complexity of this function?
"""

"""
now, write a function that does the same thing in O(logn) time where n is the
length of the list, i.e. n=len(xs)
"""


def find_missing_number_fast(xs):
    """
    xs: list, a list of n-1 integers between 0 and n (including n)
    returns: int, the missing integer
    precondition: xs is sorted in an increasing order
    """
    pass

print(find_missing_number_fast([1, 2, 3, 4, 6, 7, 8]))
print(find_missing_number_fast([2, 3, 4, 5, 6, 7, 8]))
print(find_missing_number_fast([1, 2, 3, 4, 5, 6, 7]))


"""
write a function that takes a sorted list of integers, xs and a number, x
and returns the first position i for which xs[i]>x. If there is no such i
(i.e. x is larger or equal to any element in xs), the function should
return len(xs)

Examples:
    >>> find_first_larger_slow([2,4,7,9,10,10,56,100], 8)
    3
    >>> find_first_larger_slow([2,4,7,9,10,10,56,100], 1)
    0
    >>> find_first_larger_slow([2,4,7,9,10,10,56,100], 150)
    8
    >>> find_first_larger_slow([2,4,7,9,10,10,56,100], 10)
    6

First, implement the function naively (i.e with a simple loop). You
implementation should have O(n) complexity where n is the length of the list

Then, implement the function in O(logn) time

"""


def find_first_larger_slow(xs, x):
    """
    xs: list, a list of integers
    x: int
    returns: position of the first element in xs that is strictly larger than x
    (i.e. smallest i such that xs[i]>x or len(xs) if all elements in xs are <= x)
    precondition: xs is sorted in non-decreasing order
    """
    # NAIVE IMPLEMENTATION GOES HERE
    pass

print(find_first_larger_slow([2,4,7,9,10,10,56,100], 8))
print(find_first_larger_slow([2,4,7,9,10,10,56,100], 1))
print(find_first_larger_slow([2,4,7,9,10,10,56,100], 150))
print(find_first_larger_slow([2,4,7,9,10,10,56,100], 10))


def find_first_larger_fast(xs, x):
    """
    xs: list, a list of integers
    x: int
    returns: position of the first element that is strictly larger than x
    (i.e. smallest i such that xs[i]>x or len(xs) if all elements in xs are <= x)
    precondition: xs is sorted in non-decreasing order
    """
    # O(logn) IMPLEMENTATION GOES HERE
    pass


print(find_first_larger_fast([2,4,7,9,10,10,56,100], 8))
print(find_first_larger_fast([2,4,7,9,10,10,56,100], 1))
print(find_first_larger_fast([2,4,7,9,10,10,56,100], 150))
print(find_first_larger_fast([2,4,7,9,10,10,56,100], 10))
