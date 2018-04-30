'''

Рассмотрим два HTML-документа A и B.
Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">,
возможно с дополнительными параметрами внутри тега.
Из A можно перейти в B за два перехода если существует такой документ C,
что из A в C можно перейти за один переход и из C в B можно перейти за один переход.

Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.

Sample Input 1:

https://stepic.org/media/attachments/lesson/24472/sample0.html
https://stepic.org/media/attachments/lesson/24472/sample2.html

Sample Output 1:

Yes

Sample Input 2:

https://stepic.org/media/attachments/lesson/24472/sample0.html
https://stepic.org/media/attachments/lesson/24472/sample1.html

Sample Output 2:

No

Sample Input 3:

https://stepic.org/media/attachments/lesson/24472/sample1.html
https://stepic.org/media/attachments/lesson/24472/sample2.html

Sample Output 3:

Yes

'''

import requests
import re


def input_graber(num):
    """
    :return: function return tuple of num strings from std input
    """
    lst = []
    for i in range(num):
        lst.append(input())
    return tuple(lst)

def all_url_from_html_page(url):
    """

    :param url: url of some page
    :return: list of href urls that contains page with parameter url
    """
    string = r'<a\shref=\"(?P<url>htt\S+)\"'
    res = requests.get(url)
    page = res.text
    regex = re.compile(string)
    lst = regex.findall(page)
    return(lst)


# catching urls from stdin
#url_a, url_b = input_graber(2)

if __name__ == '__main__':
    url_a, url_b = input_graber(2)
    hrefs = all_url_from_html_page(url_a)
    result_lst = []
    for urls in hrefs:
        if all_url_from_html_page(urls):
            result_lst.extend(all_url_from_html_page(urls))
    print('Yes') if url_b in result_lst else print('No')
