'''
Вам дана последовательность строк.
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
Буквой считается символ из группы \w.

Sample Input:

attraction
buzzzz

Sample Output:

atraction
buz
'''
import sys
import re

regex = re.compile(r"(\w)(\1){1,}")

for line in sys.stdin:
    line = line.rstrip()
    # process line
    line = regex.sub(r"\1", line)
    print(line)
