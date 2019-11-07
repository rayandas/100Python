'''
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
'''

from collections import Counter

s = input().split()
s = Counter(s)
s = sorted(s.items())

for i in s:
    print("%s:%d"%(i[0],i[1]))
