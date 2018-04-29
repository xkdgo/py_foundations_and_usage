'''
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве слова.
'''
import sys
import re

regex = re.compile(r'\bcat\b')

for line in sys.stdin:
    line = line.rstrip()
    # process line
    match = regex.findall(line)
    if match:
        print(line)
