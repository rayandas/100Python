'''
define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).
'''


def newtuple():
    lst = []
    for i in range(1,21):
        lst.append(i**2)
    
    print(tuple(lst))

newtuple()    

