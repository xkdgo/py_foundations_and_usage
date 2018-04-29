'''
В этой задаче вам необходимо воспользоваться API сайта numbersapi.com

Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт об этом числе.

Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.

Пример запроса к интересному числу:
http://numbersapi.com/31/math?json=true

Пример запроса к скучному числу:
http://numbersapi.com/999/math?json=true
'''

import requests


def numbers_api(number):
    """
    Function get number and check information about number
    at numbersapi.com
    returns 'Interesting' if this number have some interesting facts about
    else returns 'Boring'
    """

    api_url = 'http://numbersapi.com/{}/math'.format(number)
    params = {
        'json': 'true'
    }

    res = requests.get(api_url, params=params)
    #print(res.status_code)
    #print(res.headers['Content-Type'].split())
    data = res.json()
    db_exists = data['found']
    print(db_exists)
    return 'Interesting' if db_exists else 'Boring'

path = 'dataset_24476_3.txt'
with open(path) as read_numbers, open('facts.txt', 'w') as write_facts:
    inc = read_numbers.read()
    number_lst = inc.split()
    print(number_lst)
    for number in number_lst:
        print(number)
        write_facts.write('{}\n'.format(numbers_api(number)))



