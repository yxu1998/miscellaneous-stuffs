# hw2_sol.py
# Derrick Xu
#Sep 24 2018

"""
Part I: conditionals
"""

"""
1. write a program to find the largest of three numbers and print it.
You may NOT use the python built-in function max()

Examples:
    for x=5, y=6,    z=2 your program should print "the largest number is 6"
    for x=5, y=-6,   z=2 your program should print "the largest number is 5"
    for x=-5, y=-12, z=-1 your program should print "the largest number is -1"


You might find these helpful for printing:

    - print("the largest number is", largest)
    - print("the largest number is " + str(largest))
    - print("the largest number is %d"%largest)

where 'largest' is a variable containing an integer value

"""

x=-5
y=-12
z=-1

def largest(x,y,z):
    if x>y:
        if x>z:
            print("the largest number is " + str(x))
        else:
            print("the largest number is " + str(z))
    else:
        if y>z:
            print("the largest number is " + str(y))
        else:
            print("the largest number is " + str(z))


largest(-5,-12,-1)



"""
2. write a program to print whether a given point (x,y) is inside
the circle with center (0,0) and radius 10.5

Examples:
    for (x,y)=(5,5) your program should print "The point (5,5) is inside the circle"
    for (x,y)=(10.5,10.5) your program should print "The point (10.5,10.5) is not inside the circle"
    for (x,y)=(15,40.15) your program should print "the point (15,40.15) is not inside the
    circle"



You might find these helpful for printing:

    - print("The point (", x, ",", y, ") is inside the circle")
    - print("The point (" + str(x) + "," + str(y) + ") is inside the circle")
    - print("The point (%g,%g) is inside the circle"%(x,y))

"""

x = 5.0
y = 5.0

def circle(x,y):
    rad=((x)**2+y**2)**(1/2)
    if rad>10.5:
        print("the point"+str((x,y))+" is not inside the circle")
    else:
        print("the point"+str((x,y))+" is inside the circle")

circle(5,5)

"""
3. write a program to print whether a triangle with sides a,b,c is equilateral,
isosceles or scalene.

Note :
    - An equilateral triangle is a triangle in which all three sides are equal.
    - A scalene triangle is a triangle that has three unequal sides.
    - An isosceles triangle is a triangle with (at least) two equal sides.

Examples:
    for a=7,b=4,c=1 your program should print "Scalene triangle"
    for a=7,b=4,c=7 your program should print "Isosceles triangle"
    for a=4,b=4,c=4 your program should print "Equilateral triangle"
"""

a=4
b=5
c=5
def triangle(a,b,c):
    if a==c:
        if a==b :
            print("Equilateral triangle")

        else:
            print("Isosceles triangle")
    else:
        if b==c or a==b:
            print("Isosceles triangle")
        else:
            print("Scalene triangle")
triangle(4,5,5)


# YOUR CODE GOES HERE


"""
Part II: loops
"""

"""
4. write a program that computes the Least Common Multiple (LCM) of two positive
integers x, y. The LCM of x and y is the smallest positive integer that is divisible
by both x and y (without remainder)

Examples:
    for x=15 and y=25 your program should print THE LCM of 15 and 25 is 75"
    for x=10 and y=1 your program should print THE LCM of 10 and 2 is 10"
    for x=7 and y=9 your program should print THE LCM of 7 and 9 is 63"
"""

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)
def lcm(a,b):
    lcm=a*b/gcd(a,b)
    print("THE LCM of "+str(a)+" and "+str(9)+ "is"+str(lcm))


lcm(7,9)
# YOUR CODE GOES HERE


"""
5. write a program that computes the unsigned binary representation of a
positive integer n

Examples:
    for n=7, your program should print "the binary representation of 7 is 111"
    for n=712, your program should print "the binary representation of 7 is 1011001000"

Note1: to concatenate a character, ch to the left of a given string, s you can
use s = ch+s. For example, '1' + '1010' = '11010'

Note2: to print a string, you may use %s like this:
    print("the binary representation of %d is %s"%(n,binary_rep))

"""
def bin(x):
    acc=""

    while x>0:
        acc=str(x%2) +acc
        x=x//2
    print(acc)
bin(712)


# YOUR CODE GOES HERE


"""
6.1 The Collatz is defined as follows: start with any positive integer n. Then
each term is obtained from the previous term as follows:
    - if the previous term is even, the next term is one half the previous term.
    - if the previous term is odd, the next term is 3 times the previous term plus 1.

There is a conjecture that no matter what value of n, the sequence will always
reach 1. Write a program that computes the number of transforms made when
computing the for n until a 1 is reached (i.e. the length of the sequence).

Examples:
    - The Collatz sequence of 13 is:
    13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 ->4 -> 2 ->1
    Therefore, for n=13 your program should print 10 (the length of the sequence)
    - for n=15, your program should print 18
    - for n=20, your program should print 8

"""

n = 15

def collatz(x):
    n=1
    while x!=1:
        if x%2==0:
            x=x/2
            n+=1
        else:
            x=3*x+1
            n+=1
    print(n)
collatz(20)



"""
6.2 Now write a program that computes the largest int in the Collatz sequence
for n.

    Examples:
    - For n=13, the largest number in the sequence is 40
    - For n=15, the largest number in the sequence is 160
    - For n=20, the largest number in the sequence is 20


"""

n=15
def collatz(x):
    lar=0
    while x!=1:
        if x%2==0:
            if x>lar:
                lar=x
                x=x/2
            else:
                x=x/2

        else:
            if x>lar:
                lar=x
                x=3*x+1
            else:
                x=3*x+1


    print(lar)
collatz(15)



"""
7. write a program that asks the the user repeatedly to type in a whole number
OR 'q' to quit and then, when the user types 'q' print the *second* largest
number that was entered. You may assume that the user types at least two
(different) numbers.

Examples:
    if the user enters '5', '10', '7', '25', '5', '15', '9', 'q' your program should print
    "the second largest entered number is 15"

Note: use python command 'input' to ask the user for an input and then convert the
string entered by the user to an integer (just like we did in the lab)
"""

def second():
    lar=0
    second=0
    num=""
    n=0
    while n!=1:
        num=input("please enter")
        if num=="q":
            n=1

        elif int(num) > lar:
            second=lar
            lar=int(num)


    print("the second largest entered number is "+str(second))
second()
# YOUR CODE GOES HERE


"""
8. The program you wrote above is a typical example for a do-while pattern.

8.1: define the execution of do-while (just like we did in lectures with other
control-flow statements)

solution:

Syntax: if e is an expression and i is an instruction(s), then do i while e is a do-while loop.
e is called the test expression and i the body

Execution: to execute a do-while loop from binding table s:

    1.creating binding table
    2.we execute a program no matter what condition is
    3.change binding table
    4.check if e loop condition is true and decide if i program will run
    5.repeat 3 to 5
8.2: given a while loop of the form:

    while e:
        i

    write an equivalent do-while

solution:

    a (whatever code that we are runing)
    while e:
        i

"""
