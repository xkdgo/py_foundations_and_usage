"""
Вам дана частичная выборка из датасета зафиксированных преступлений,
совершенных в городе Чикаго с 2001 года по настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

Файл с данными:
Crimes.csv
"""
import csv

with open('Crimes.csv') as f:
    reader = csv.reader(f)
    headers = next(reader)
    print(headers)
    result_dict = {}
    for row in reader:
        if '2015' in row[2]:
            if row[5] in result_dict:
                result_dict[row[5]] += 1
            else:
                result_dict[row[5]] = 1
    maxi = 1
    for key in result_dict:
        if result_dict[key] >= maxi:
            maxi = result_dict[key]
            crime = key
        else:
            pass

    print(crime)



