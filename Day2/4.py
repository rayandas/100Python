'''
Write a program which accepts a sequence of comma-separated numbers from 
console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Output: ['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
'''

lst = input().split(",")

tpl = tuple(lst)

print(lst)
print(tpl)
