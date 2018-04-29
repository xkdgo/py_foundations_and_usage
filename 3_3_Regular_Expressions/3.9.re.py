'''
Вам дана последовательность строк.
Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.

Sample Input:

zabcz
zzz
zzxzz
zz
zxz
zzxzxxz

Sample Output:

zabcz
zzxzz
'''
import sys
import re

regex = re.compile(r'z...z')

for line in sys.stdin:
    line = line.rstrip()
    # process line
    match = regex.findall(line)
    if match:
        print(line)
