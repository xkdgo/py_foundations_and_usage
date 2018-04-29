#!/usr/bin/python3.6

'''
Алиса владеет интересной информацией, которую хочет заполучить Боб.
Алиса умна, поэтому она хранит свою информацию в зашифрованном файле.
У Алисы плохая память, поэтому она хранит все свои пароли в открытом виде в текстовом файле.

Бобу удалось завладеть зашифрованным файлом с интересной информацией и файлом с паролями, но он не смог понять какой из паролей ему нужен. Помогите ему решить эту проблему.

Алиса зашифровала свою информацию с помощью библиотеки simple-crypt.
Она представила информацию в виде строки, и затем записала в бинарный файл результат работы метода simplecrypt.encrypt.

Вам необходимо установить библиотеку simple-crypt, и с помощью метода simplecrypt.decrypt узнать, какой из паролей служит ключом для расшифровки файла с интересной информацией.

Ответом для данной задачи служит расшифрованная интересная информация Алисы.

'''



def open_file_and_decrypt(encryptedfile, passwordsfile):
    ''' This function get .bin file with password compare it with passwords file
    and return password
    '''

    import simplecrypt
    with open(encryptedfile, 'rb') as enc_file:
        encrypted = enc_file.read()
        print(encrypted)
        with open(passwordsfile) as passwd:
            passwds = passwd.read().split('\n')
            print(passwds)
            for key in passwds:
                try:
                    decrypted = simplecrypt.decrypt(key, encrypted)
                except:
                    print(f'{key} not valid')
                else:
                    print(f'{key} valid')
                    return decrypted.decode('utf-8')

print(open_file_and_decrypt('encrypted.bin', 'passwords.txt'))
