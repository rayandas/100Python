'''
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. 
Suppose the following input is supplied to the program:

1,2,3,4,5,6,7,8,9

Then, the output should be:

1,9,25,49,81
'''
from math import *

lst = input().split(',')
x = []
for i in lst:
    if int(i)%2 !=0:
        x.append(int(i)**2)

print(x)

