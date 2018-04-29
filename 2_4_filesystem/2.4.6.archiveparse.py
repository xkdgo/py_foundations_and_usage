#!/usr/bin/python3
'''
Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.

Вам необходимо распаковать этот архив,
и затем найти в данной в файловой структуре все директории,
в которых есть хотя бы один файл с расширением ".py".

'''
import os
import zipfile


def archive_parse(archive):
    '''Unzip archive and parse it to find directories with *.py files
    then sort list of directories in lexicographic manner
    '''
    result = []
    with zipfile.ZipFile(archive, 'r') as zip_ref:
        zip_ref.extractall('.')
    for item in os.walk('.'):
       main_dir, sub_dir, files = item
       for fi in files:
            if '.py' in fi:
                result.append(main_dir[2:])
                break
    result.sort()
    return result


if __name__ == "__main__":
    for item in archive_parse('main.zip'):
        print(item)
