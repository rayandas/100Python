'''
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a 
single line.Suppose the following input is supplied to the 
program: 8 Then, the output should be:40320
'''

n = int(input("Enter the number: "))
f=1
while n>0:
    f=f*n
    n-=1

print(f)    
