'''
Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
'''
def sqr(x):
    return x*x

def even(x):
    return x%2==0


li = [1,2,3,4,5,6,7,8,9,10]

numbers = map(sqr, filter(even,li))

print(list(numbers))
