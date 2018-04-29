'''
Вам дана последовательность строк.
Выведите строки, содержащие обратный слеш "\﻿".

Sample Input:

\w denotes word character
No slashes here

Sample Output:

\w denotes word character
'''
import sys
import re

regex = re.compile(r'\\')

for line in sys.stdin:
    line = line.rstrip()
    # process line
    match = regex.findall(line)
    if match:
        print(line)
