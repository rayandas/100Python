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
        
