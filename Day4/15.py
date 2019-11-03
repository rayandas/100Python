'''
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

Suppose the following input is supplied to the program:

9

Then, the output should be:

11106
'''

x = input()
a = int(x) + int(2*x) + int(3*x) + int(4*x)
print(a)
