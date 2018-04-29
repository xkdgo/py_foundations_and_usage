# coding=utf-8
import os
import os.path
import shutil
import zlib


# печать текущей папки
print(os.getcwd())

# Вывод содержимого папки main в виде list
print(os.listdir('main'))

# Вывод содержимого текущей папки в виде list
print(os.listdir(os.getcwd()))

# проверка наличия файла или директории
print(os.path.exists('main.zip'))
print(os.path.exists('main'))
print(os.path.exists('notexisted'))

# проверка файл или директория
print(os.path.isfile('main.zip'))
print(os.path.isfile('main'))

print(os.path.isdir('main.zip'))
print(os.path.isdir('main'))

# узнаем абсолютный путь по относительному
print(os.path.abspath('main.zip'))

# смена текущей директории
os.chdir('..')
print(os.getcwd())

os.chdir('2_4_filesystem')
# копирование файлов
shutil.copy('testfile.txt', 'testfile.txt.bak')

#копирование каталогов
#shutil.copytree('main', 'test/test/main')

#архивирование каталогов
print(shutil.get_archive_formats())
shutil.make_archive('myarchive', 'gztar', 'test','test')
shutil.make_archive('myarchive', 'zip', 'test', 'test')
