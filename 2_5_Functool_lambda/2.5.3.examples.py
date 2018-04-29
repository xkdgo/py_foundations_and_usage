#x = input().split()
#xs = (int(i) for i in x)


#def even(x):
#    return x % 2 == 0
'''
even = lambda x: x % 2 == 0

evens = list(filter(even, xs))
print(evens)
'''
xs = [1, 2, 3, 4, 5, 6, 7, 8]

print(list(filter(lambda x: x % 2 == 0, xs))) # [2, 4, 6, 8]

