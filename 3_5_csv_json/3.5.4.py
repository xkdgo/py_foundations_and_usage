'''

Вам дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов, которые соответствуют классам.

У каждого JSON-объекта есть поле name, которое содержит имя класса, и поле parents,
которое содержит список имен прямых предков.

Пример:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

﻿Эквивалент на Python:

class A:
    pass

class B(A, C):
    pass

class C(A):
    pass


Гарантируется, что никакой класс не наследуется от себя явно или косвенно,
и что никакой класс не наследуется явно от одного класса более одного раза.

Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.

<имя класса> : <количество потомков>

Выводить классы следует в лексикографическом порядке.

Sample Input:

[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

Sample Output:

A : 3
B : 1
C : 2

'''

import json

string = input()

list_from_json = json.loads(string)

list_of_keys = []

# составляем ключи в лексикографическом порядке
for dict_item in list_from_json:
    list_of_keys.append(dict_item['name'])
list_of_keys.sort()


result_dict = {}

for key in list_of_keys:
    result_dict[key] = []
    for dict_item in list_from_json:
        # находим и записываем в список непосредственных детей данного ключа
        if key in dict_item['parents']:
            result_dict[key].append(dict_item['name'])

copy_dict = result_dict.copy()

for key in copy_dict:
    for item in copy_dict[key]:
        # находим и добавляем внуков каждого ключа к уже записанным детям
        if item in copy_dict.keys():
            result_dict[key] += result_dict[item]

for key in list_of_keys:
    # делаем требуемый в задаче подсчет
    childs = 1
    childs += len(set(result_dict[key]))
    print('{} : {}'.format(key, childs))