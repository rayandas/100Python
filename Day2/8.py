'''

Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

Suppose the following input is supplied to the program:

without,hello,bag,world

Output:

bag,hello,without,world
'''

lst = input().split(',')
lst.sort()
print(",".join(lst))
