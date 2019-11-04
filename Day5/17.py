'''
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200
D means deposit while W means withdrawal.

Suppose the following input is supplied to the program:

D 300
D 300
W 200
D 100

Then, the output should be:

500
'''

lst = []
while True:
    x = input()
    if len(x)==0:
        break
    lst.append(x)

m=0
for i in lst:
    if 'D' in i:
        m = m + int(i.strip('D '))
    if 'W' in i:
        m = m - int(i.strip('W '))

print(m)
