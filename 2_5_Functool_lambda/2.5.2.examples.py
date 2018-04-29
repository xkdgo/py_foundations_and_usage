
n, k = map(int, input().split())
print(n + k)


x = input().split()
print(x)
map_obj = map(int, x) # f [a, b, c, d] -> f(a), f(b), f(c), f(d)
print(map_obj)
n = next(map_obj)
print(n)
k = next(map_obj)
print(k)
print(n + k)


# Рассмотрим класс filter который возвращает итератор значений в которых функция вовращает true
x = input().split()
xs = (int(i) for i in x)

def even(x):
    return x % 2 == 0

evens = filter(even, xs) # класс filter является итератором


print(next(evens))
print(next(evens))
print(next(evens))
print(next(evens))



