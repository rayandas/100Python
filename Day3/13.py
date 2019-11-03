'''
Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:

hello world! 123

Then, the output should be:

LETTERS 10
DIGITS 3
'''

w = input()
letter, digit = 0, 0

for i in w:
    if (i>='a' and i<='z') or (i>='A' and i<='Z'):
        letter += 1
    if (i>='0' and i<='9'):
        digit += 1
print("Letters %d \n Digit %d"%(letter,digit))        
