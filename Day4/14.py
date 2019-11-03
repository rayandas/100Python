'''
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Suppose the following input is supplied to the program:

Hello world!

Then, the output should be:

UPPER CASE 1
LOWER CASE 9
'''

w = input()

upper, lower = 0, 0
for i in w:
    if i.islower():
        lower += 1
    if i.isupper():
        upper += 1

print("Upper case %d \n Lower case %d"%(upper, lower))
