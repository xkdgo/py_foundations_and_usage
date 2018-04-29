'''
Вам дана последовательность строк.
В каждой строке поменяйте местами
две первых буквы в каждом слове, состоящем хотя бы из двух букв.
Буквой считается символ из группы \w.

Sample Input:

this is a text
"this' !is. ?n1ce,

Sample Output:

htis si a etxt
"htis' !si. ?1nce,
'''
import sys
import re

regex = re.compile(r"\b(.*?)(\w)(\w)(.*?)\b", re.IGNORECASE)

for line in sys.stdin:
    line = line.rstrip()
    # process line
    line = regex.sub(r"\1\3\2\4", line)
    print(line)
