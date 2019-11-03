'''
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

Suppose the following input is supplied to the program:

Hello world
Practice makes perfect

output:

HELLO WORLD
PRACTICE MAKES PERFECT

'''


lst = []

while True:
    w = input()
    if len(w)==0:
        break
    lst.append(w.upper())

for lines in lst:
    print(lines)
