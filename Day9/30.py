'''
Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.
'''
def printVal(s1,s2):
    l1 = len(s1)
    l2 = len(s2)
    if l1==l2:
        print(s1)
        print(s2)
    elif l1>l2:
        print(s1)
    elif l2>l1:
        print(s2)

s1 = input()
s2 = input()
printVal(s1,s2)


