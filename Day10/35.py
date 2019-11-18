'''
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.
'''

def newlist():
    lst = []
    for i in range(1,21):
        lst.append(i**2)

    for i in range(19,14,-1):
        print(lst[i])

newlist()        

