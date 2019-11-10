'''
Define a function which can compute the sum of two numbers.
'''
'''
def sumOfNum(x,y):
    s = x+y
    return s

a = int(input()) 
b = int(input())
print(sumOfNum(a,b))
'''


sum = lambda x,y : x+y

a = int(input())
b = int(input())
print(sum(a,b))
