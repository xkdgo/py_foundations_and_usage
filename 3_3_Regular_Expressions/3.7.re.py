'''
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.
'''
import sys
import re

regex = re.compile(r'cat.*cat')

for line in sys.stdin:
    line = line.rstrip()
    # process line
    match = regex.findall(line)
    if match:
        print(line)
