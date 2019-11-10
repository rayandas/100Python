'''
Define a function that can receive two integer numbers in string form and compute their sum and then print it in console.
'''

sum = lambda str1, str2 : int(str1) + int(str2)

str1 = input("enter the input1:")
str2 = input("enter the input2:")

print(sum(str1,str2))

