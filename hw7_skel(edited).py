# hw7_skel.py
# YOUR NAME


"""
1. Consider the following function that takes a list xs and a function f, and
returns the sum f(x[0]) + f(x[1]) + ... + f(x[len(xs)-1]).

In each of the problems below, you need to implement f such that the function
call sum_general(xs, f) returns the desired result (see example below).
"""

def sum_general(xs, f):
    """
    xs: list
    f: function, a function that returns an integer
    returns: int, f(x[0]) + f(x[1]) + ... + f(x[len(xs)-1])
    """
    res = 0
    for x in xs:
        res += f(x)
    return res

# Example
def sum_list(xs):
    """
    xs: list, a list of integers
    returns: int, sum of elements in xs
    """
    def f(x):
        return x
    return sum_general(xs, f)

print(sum_list([1,5,0,8,3,0,2])) # 19
***
# Problem 1 (10 points)
def sum_squares(xs):
    """
    xs: list, a list of integers
    returns: int, sum  of the squares of elements in xs
    """
    sum=0
    def f(x):
        return x**2
    for x in xs:
        sum+= f(x)
    return sum
# UNCOMMENT THE FOLLOWING LINE TO TEST YOUR CODE
print(sum_squares([1,5,0,8,3,0,2])) # 103

# Problem 2 (10 points)
def count_zeros(xs):
    """
    xs: list, a list of integers
    returns: int, number of zeroes in xs
    """
    def f(x):
        if x==0:
            return 1
        else:
            return 0
    return sum_general(xs, f)

# UNCOMMENT THE FOLLOWING LINE TO TEST YOUR CODE
# print(count_zeros([1,5,0,8,3,0,2])) # 2

# Problem 3 (10 points)
def sum_seconds(xs):
    """
    xs: list, a list of tuples representing time
    returns: int, total number of seconds obtained by adding all times in xs
    """

    def f(x):
        a=x(0)
        b=x(1)
        c=x(2)
        return a*(60*60)+b*60+c
        pass
    return sum_general(xs, f)

# UNCOMMENT THE FOLLOWING LINES TO TEST YOUR CODE
# print(sum_seconds([(1,10,0),(0,0,20)])) # 72620
print(sum_seconds([(1,40,30),(2,0,0),(3,50,1)])) # 117031


"""
2. Consider the following class that represents a 2D point, and use it to
implement the functions below.

"""

class Point(object):
    """
    Represents a point in 2D
    """
    def __init__(self, x, y):
        """
        x: int or float
        y: int or float
        """
        self.x = x
        self.y = y


# 5 points
def point_to_str(p):
    """
    p: Point
    returns: str, string representation of the point p
    """
    left=p.x
    right=p.y
    return(left,right)

p = Point(2,3)
print(point_to_str(p)) # should print (2,3)

# 5 points
def distance(p1, p2):
    """
    p1, p2: Point
    returns: float, the Euclidean distance between p1 and p2
    """
    left=p1.x-p2.x
    right=p1.y-p2.y
    return (left**2+right**2)**(1/2)

print(distance(Point(1,2), Point(1,3))) # 1.0

# 5 points
def is_on_line(p, slope, intercept):
    """
    p: Point
    a, b: integers
    returns: bool, True if the point p is on the line y=slope*x+intercept
    """
    left=p.x
    right=p.y
    if right==slope*left+intercept:
        return True
    else:
        return False


print(is_on_line(Point(1,2), 2, 0)) # True
print(is_on_line(Point(1,3), 2, 1)) # True
print(is_on_line(Point(1,2), 1, 0)) # False

"""
3. Consider the following class that represents a list of 2D points on a line,
and use it to implement the functions below.
"""

class PointsOnLine(object):
    """
    Represents a list of points on the line y=ax+b
    """
    def __init__(self, slope, intercept):
        """
        slope: int
        intercept :int
        """
        self.m = slope
        self.b = intercept
        self.points = []

# 10 points
def add_point_to_line(line, p):
    """
    line: PointsOnLine
    p: Point
    returns: nothing. The function should append p to line.points only
    if p is indeed on the line y = line.m * x+ line.b.
    Note: you should use the function is_on_line the you implemented above
    """
    x=p.x
    y=p.y
    slope=line.m
    intercept=line.b
    acc=line.points
    if y==slope*x+intercept:
        acc.append(p)



line = PointsOnLine(1, 1) # creates the line y = x+1
add_point_to_line(line, Point(2,3)) # adds the point (2,3)
add_point_to_line(line, Point(2,2)) # does nothing since the point (2,2) is not on the line y=x+1
print(len(line.points)) # should print 1

"""
# 10 points
def remove_point_from_line(line, p):
    """
    line: PointsOnLine
    p: Point
    returns: nothing. The function should remove the first occurrence of p in
    line.points if it is in line.points. If the point is not there, nothing
    should happen.
    Note that you can't ask if p is in line.points since Python
    doesn't know how to compare two Point objects. For the same reason, you can't use
    the list method 'remove'. Instead, you will have to find the index of the point and use 'pop'
    """
    i=0
    while i < len(line.points):
        if (line.points[i]).x == p.x and (line.points[i]).y == p.y:
            line.points.pop(i)
            break
        i += 1

"""

line = PointsOnLine(1, 1) # creates the line y = x+1
add_point_to_line(line, Point(2,3)) # adds the point (2,3)
add_point_to_line(line, Point(5,6)) # adds the point (5,6)
add_point_to_line(line, Point(2,3)) # adds the point (2,3)
remove_point_from_line(line, Point(2,3)) # removes the first occurrence of (2,3) from line.points
remove_point_from_line(line, Point(2,2)) # does nothing since the point (2,2) is not on the line
print(len(line.points)) # should print 2


"""
4. Recall the class LinkedLlist that was discussed in lectures
"""

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

"""
(20 points) Implement a recursive function min_list that returns the value and location
of the minimum  element in a linked list xs. You may NOT use a Python list or a loop in your code.

Remember that you can use a tuple to return two values from a function.

"""


def min_list(xs):
    """
    xs: LinkedList
    returns: tuple, the value and location of the minimum element in xs
    """

    if xs.rest == None:
        return (xs.value, 0)
    elif xs.value < (min_list(xs.rest))[0]:
        return (xs.value, (min_list(xs.rest))[1] + 1)
    else:
        return min_list(xs.rest)

# creating the list 0 -> 5 -> -3 -> 1 -> 4
node1 = LinkedList(4, None)
node2 = LinkedList(1, node1)
node3 = LinkedList(-3, node2)
node4 = LinkedList(5, node3)
node5 = LinkedList(0, node4)

res = min_list(node5)
print(res)
# res[0] should be -3
# res[1] should be 2
