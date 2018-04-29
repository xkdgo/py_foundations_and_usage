#!/usr/bin/python
try:
    x = [1, 2, "hello", 7]
    x.sort()
    print(x[4])
except IndexError:
    print('IndexError :(')
print('I can`t catch')
