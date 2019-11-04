

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
