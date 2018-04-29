'''
Вашей программе на вход подаются три строки s, a, b, состоящие из строчных латинских букв.
За одну операцию вы можете заменить все вхождения строки a в строку s на строку b.

Например, s = "abab", a = "ab", b = "ba", тогда после выполнения одной операции
строка s перейдет в строку "baba", после выполнения двух и операций – в строку "bbaa",
и дальнейшие операции не будут изменять строку s﻿.

Необходимо узнать, после какого минимального количества операций
в строке s не останется вхождений строки a, либо же определить, что это невозможно.

Выведите одно число – минимальное число операций,
после применения которых в строке s не останется вхождений строки a.
Если после применения любого числа операций в строке s
останутся вхождения строки a, выведите Impossible.
'''

def input_graber(num):
    """
    :return: function return tuple of num strings from std input
    """
    lst = []
    for i in range(num):
        lst.append(input())
    return tuple(lst)

def min_oper_count(s, a, b):
    """
    :param s: main string that may consists string a
    :param a: string to check if it in s
    :param b: string to change from a in s
    :return: min count of operation to change all a in s by changing a by b, else Impossible
    """
    if a in s and a in b:
        return 'Impossible'
    count = 0
    while a in s:
        s = s.replace(a, b)
        count += 1
    return count

s, a, b = input_graber(3)
print(min_oper_count(s, a, b))
