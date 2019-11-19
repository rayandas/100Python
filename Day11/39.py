'''
Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
'''

tpl1 = (1,2,3,4,5,6,7,8,9,10)
tpl = []

for i in range(10):
    if (tpl1[i]%2==0):
        tpl.append(tpl1[i])

print(tpl1,end='')
print()
print(tuple(tpl),end='')

