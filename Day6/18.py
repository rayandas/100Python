'''
A website requires the users to input username and password to register. 
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:


Minimum length of transaction password: 6
Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. 
Passwords that match the criteria are to be printed, each separated by a comma.
'''

def islow(x):
    for i in x:
        if i>='a' and i<='z':
            return True
    return False

def isup(x):
    for i in x:
        if i>='A' and i<='Z':
            return True
    return False

def isnum(x):
    for i in x:
        if i>='0' and i<='9':
            return True
    return False

def isother(x):
    for i in x:
        if i=='#' or i=='@' or i=='$':
            return True
    return False

pwd = input().split(',')
lst = []
for i in pwd:
    l = len(i)
    if l>=6 and l<=12 and isup(i) and islow(i) and isnum(i) and isother(i):
        lst.append(i)


#print(",".join(lst))
print(lst)
        
