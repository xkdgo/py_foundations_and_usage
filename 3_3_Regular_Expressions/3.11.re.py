'''
Вам дана последовательность строк.
Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).

Sample Input:

blabla is a tandem repetition
123123 is good too
go go
aaa

Sample Output:

blabla is a tandem repetition
123123 is good too
'''
import sys
import re

regex = re.compile(r'\b(\w+)\1\b')

for line in sys.stdin:
    line = line.rstrip()
    # process line
    match = regex.findall(line)
    if match:
        print(line)
