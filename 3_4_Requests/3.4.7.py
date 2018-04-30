'''


Вашей программе на вход подается ссылка на HTML файл.
Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > и вывести список сайтов,
на которые есть ссылка.

Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. То есть, это последовательность символов,
которая следует сразу после символов протокола, если он есть, до символов порта или пути, если они есть,
за исключением случаев с относительными ссылками вида
<a href="../some_path/index.html">.

Сайты следует выводить в алфавитном порядке.

Пример HTML файла:

<a href="http://stepic.org/courses">
<a href='https://stepic.org'>
<a href='http://neerc.ifmo.ru:1345'>
<a href="ftp://mail.ru/distib" >
<a href="ya.ru">
<a href="www.ya.ru">
<a href="../skip_relative_links">

Пример ответа:

mail.ru
neerc.ifmo.ru
stepic.org
www.ya.ru
ya.ru


'''
import requests
import re


def find_and_sort_domains_from_href(url):
    """

    :param url: url of some page
    :return: sorted list of host.domain contained in hrefs of some page with url
    """
    string = r'<a.*?href(?:\s+)?=(?:\s+)?[\"\'](?:http://|https://|ftp://)?(?P<url>\w\S+?)[\/\:\'\"\?]'
    regex = re.compile(string, re.DOTALL)
    res = requests.get(url)
    page = res.text
    lst = list(set(regex.findall(page)))
    lst.sort()
    return lst


if __name__ == '__main__':
    for item in find_and_sort_domains_from_href(input().rstrip()):
        print(item)
