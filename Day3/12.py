'''
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

lst = []
for i in range(1000,3001):
    f = 1
    for j in str(i):
        if int(j)%2 !=0:
            f = 0
            break
    if f==1:        
        lst.append(str(i))

print(",".join(lst))    
