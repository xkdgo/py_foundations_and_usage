'''
Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.

Выведите одно число – количество вхождений строки t в строку s.

Пример:
s = "abababa"
t = "aba"

Вхождения строки t в строку s:
abababa
abababa
abababa
'''

def input_graber(num):
    """
    :return: function return tuple of num strings from std input
    """
    lst = []
    for i in range(num):
        lst.append(input())
    return tuple(lst)

def count_of_find_string(s, t):
    """
    :param s: string to test
    :param t: string to check appear in s
    :return: count of t appears in s
    """
    pos = 0
    cnt = 0
    while s.find(t, pos) != -1:
        pos = s.find(t, pos) + 1
        cnt += 1
    return cnt

s, t = input_graber(2)
print(count_of_find_string(s, t))

