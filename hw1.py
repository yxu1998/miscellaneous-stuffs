# hw1_skel.py
# PUT YOUR NAME HERE
# Skeleton by Prof. Shai (sshai@wesleyan.edu), Sep 3 2018

"""
You can either enter your solution in this file and submit through Moodle, or print the file and write down your answers
(you can give it to me directly during Tuesday lecture or leave it in the box outside my office).
If you print it, I suggest that you add some space between problems for your solution.
In future coding assignments, you will have to submit the skeleton file through Moodle.

"""

"""
Part 1: Information representation (70 points)

    problem 1:  Consider the following sequence of bits: 1010 1100
                (spaces have been inserted spaces for readability, but have no meaning)
                i) interpret the sequence as an unsigned representation
                172
                ii) interpret the sequence as a signed representation
                -44
                iii) interpret the sequence as a twos-complement representation
                -84


    problem 2:  i) what is the binary for the decimal numeral 255, using 8 bits?
                1111 1111    
                ii) what is the binary signed for the decimal numeral -17, using 8 bits?
                10010001
                iii) what is the binary twos/////-c/omplement f/or the decimal numeral -17, using 8 bits?
                11101111
   

    problem 3:  Recall the 16-bit representation of floating points discussed in class:
                the first (left most) bit represents the sign of the number,
                the next 5 bits are a signed representation of the exponent (e),
                and the remaining 10 bits are an unsigned representation of the fraction bits (f).
                What is the floating point number represented by the following sequence:
                1101 0101 0001 0011
                s = 1
                e = 10101 = -5
                f = 0100010011 = 1 + 2 + 16 + 256 = 275
                -8.59375
                

    problem 4: Imagine that you have 1023 coins and 10 bags and you want to divide the coins over the ten bags, so that you can make any number of coins simply by handing over a few bags.
               For example, if someone asks you for 17 coins you just hand them a few bags with coins which sum up to exactly 17. How can you do it?
               Divide coins in this order to bags: 512 256 128 64 32 16 8 4 2 1

"""

"""
Part 2: Binding tables (15 points)

Consider the following Python code:

"""

x = 7/2
y = 7//2
y = y+int(x)

b1 = type(y)==int
b2 = b1 and False
b2 = b2 or True

s = 'hi'
s = s*y
"""
Describe the evolution of the state (i.e. table binding) for the execution of this program, starting from the empty state.
Use the notation s_i to describe the binding tables after executing line number i. So, s_0 = {}.
You may add print statements to help you determine the values of variables.
s_0={}
s_1={x=3.5}
s_2={x=3.5 y=3}
s_3={x=3.5 y=6}
s_4={x=3.5 y=6 b1=True}
s_5={x=3.5 y=6 b1=True b2=False}
s_6={x=3.5 y=6 b1=True b2=True}
s_7={x=3.5 y=6 b1=True b2=True s="hi"}
s_8={x=3.5 y=6 b1=True b2=True s="hihihihihihi"}

"""

"""
Part 3: Editing and running python programs (15 points) 

    i) read the python code below
    ii) change the variable n to be your student ID
    iii) run the program and report what it being printed
"""

# importing the module `random`
import random

# define a variable `n`
n=360063

# set a random seed
random.seed(n)

# draw a random number in the range [a,b]
my_number = random.randint(0,100) 

# print the type of the number (should be int)
print(type(my_number))

# print the number itself
print(my_number)

what is printed is 95
