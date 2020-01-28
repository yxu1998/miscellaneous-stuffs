# lab3_skel.py
# YOUR NAME GOES HERE
# September 19, 2018

"""
Part I: conditionals
"""

"""
1. write a program to print the absolute value of a given number x

Examples:
    for x=7, your program should print "the absolute value of 7 is 7"
    for x=-7.7, your program should print "the absolute value of -7.7 is 7.7"
    for x=0, your program should print "the absolute value of 0 is 0"

Note: to print a float variable, you may use %g like this:
    print("the absolute value of %g is %g"%(x,abs_x))
where x and abs_x are floats
"""
def absolute(x):
    new=abs(x)
    print("the absolute value of "+str(x)+" is "+str(new))


"""
2. write a program to print whether a given point (x,y) is inside
inside (not on the edge) of the 10x10 square (0,10) x (0,10)

Examples:
    for (x,y)=(5,5) your program should print "The point (5,5) is inside the square"
    for (x,y)=(-2,5.7) your program should print "The point (-2,5.7) is NOT inside the
    square"

Use %g like before to print, for example:
    "The point (%g,%g) is inside the square"%(x,y)
"""
def inside(x,y):
    if 0<x<10:
        if 0<y<10:
            print("The point "+str((x,y))+" is inside the square")
        else:
            print("The point "+str((x,y))+" is NOT inside the square")
    else:
        print("The point "+str((x,y))+" is NOT inside the square")

inside(-2,5.7)

# YOUR CODE GOES HERE



"""
3. write a program that computes the Euclidean distance between two points (x1,y1) and
(x2,y2), and print "close!" if the distance is less than 6

Examples:
    for (x1,y1)=(1.4,3.1) and (x2,y2)=(-2.6,0.1) your program should print "close!"
    for (x1,y1)=(0,0) and (x2,y2)=(20,20) your program should not print anything
"""


x1=1.4
y1=3.1
x2=-2.6
y2=0.1

# YOUR CODE GOES HERE



"""
4.1 Consider the following program that describes the effect of an earthquake of a
given strength. Try running it with different values of 'richter_intensity'.
What is wrong with the code and how would you fix it?
"""

richter_intensity = 8

if richter_intensity > 8:
    print("All structures fail")
if richter_intensity > 6:
    print("Many buildings fall")
if richter_intensity > 4:
    print("Some buildings damaged")
if richter_intensity > 2:
    print("Minor damage")

"""
4.2 Now consider the code below that attempts to do the same thing. Try running it
with different values of 'richter_intensity'. What is wrong with the code and how
would you fix it?
"""

richter_intensity = 5

if richter_intensity > 2:
    print("Minor Damage")
elif richter_intensity > 4:
    print("Some buildings damaged")
elif richter_intensity > 6:
    print("Many buildings fall")
elif richter_intensity > 8:
        print("All structures fail")

"""
Part II: while loops
"""

"""
5. write a program that calculates the n factorial, i.e. the product of the
first n positive numbers.

Examples:
    for n=5, your program should print "5!=120"
    for n=1, your program should print "1!=1"
    for n=2, your program should print "2!=2"
"""

n = 5

# YOUR CODE GOES HERE



"""
6. write a program that prints the sum of the first n positive even numbers.

Examples:
    for n=5, your program should print "30" because 2+4+6+8+10=30
    for n=4, your program should print "20" because 2+4+6+8=20
    for n=2, your program should print "2"
"""

n=5

# YOUR CODE GOES HERE


""" 
7. write a program that prints the sum of the series  9 + 99 + 999 + 9999 ... up
to n terms

Examples:
    for n=1, your program should print 9
    for n=2, your program should print 108 (since 9+99=108)
    for n=5, your program should print 111105 (since 9+99+999+9999+99999=111105)

"""

n = 2

# YOUR CODE GOES HERE




"""
8. write a program to find the greatest common divisor (GCD) of two positive
integers x, y. The GCD of x and y is the largest positive integer that divides
both x and y (without remainder)

Examples:
    for x=8 and y=6 your program should print "THE GCD of 8 and 6 is 2"
    for x=3 and y=6 your program should print "THE GCD of 3 and 6 is 3"
    for x=5 and y=6 your program should print "THE GCD of 5 and 6 is 1"

Note that if x,y,GCD are integers you can print using the following command:

    print("THE GCD of %d and %d is %d"%(x,y,gcd)

"""

x=7
y=25


# YOUR CODE GOES HERE



"""
9. write a program that computes the sum of digits in a positive integer, n and
prints the result

Examples:
    for n=174 your program should print "digits sum = 12"
    for n=1014 your program should print "digits sum = 6"
    for n=10000 your program should print "digits sum = 1"
"""


n = 174

# YOUR CODE GOES HERE



"""
10. complete the following program to ask the the user repeatedly to type in a whole
number OR 'q' to quit and then, when the user types 'q' print the sum of the last 3
numbers entered. If less than 3 numbers entered, print the sum of all of them.
"""


# ADD SOME VARIABLES HERE

# asking the user for input
inp = input("type a whole number or 'q' to quit: ")
# now inp is a string, you need to use int(inp) to turn it into an integer


while inp != 'q':

    # turning inp into an integer
    num = int(inp)

    # YOUR CODE GOES HERE
 

    # asking the user for new input
    inp = input("type a whole number or 'q' to quit: ")


# printing the result (assuming you keep it in the variable 'sum_last_3'
print("the sum of the last 3 numbers is %d"%sum_last_3)
