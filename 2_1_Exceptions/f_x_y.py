#!/usr/bin/python

def f(x, y):
    try:
        return x / y
    except TypeError:
        print('Type Error oqured')
#    except ZeroDivisionError:
#        print('Zerodivision :(')

try:
    print(f(5, 0))
except ZeroDivisionError:
    print('ZeroDivision :((')

print(ZeroDivisionError.mro())
