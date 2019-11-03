'''
    Write a program that calculates and prints the value according to the given formula:

        Q = Square root of [(2 * C * D)/H]

Following are the fixed values of C and H:

        C is 50. H is 30.

D is the variable whose values should be input to your program in a comma-separated sequence.
'''
from math import *
C,H = 50,30

def calc(D):
    return sqrt((2*C*D)/H)

D = input().split(',')
D = [str(round(calc(int(i)))) for i in D]

print(",".join(D))


