import os
import aes_cipher
from zipfile import ZipFile
from getpass import getpass
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data_encrypter = aes_cipher.DataEncrypter()
data_decrypter = aes_cipher.DataDecrypter()

# Метод шифрования файлов
def encrypt_file(file, key):
    with open(file, 'rb') as f:
        data = f.read()
        data_encrypter.Encrypt(data, key.decode())
        with open(file, 'wb') as f:
            f.write(data_encrypter.encrypted_data)

# Метод дешифрования файлов
def decrypt_file(file, key):
    with open(file, 'rb') as f:
        data = f.read()
        data_decrypter.Decrypt(data, key.decode())
        with open(file, 'wb') as f:
            f.write(data_decrypter.decrypted_data)

# Метод генерации и шифрования ключа
def pass_generation():
    key = get_random_bytes(16) # Генерируем ключ шифрования

    # Шифрование
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext = cipher.encrypt_and_digest(key)# Зашифрованный текст
    ciphertext = str(ciphertext[1])

    # Запись ключа в файл
    new_file = open('password.txt', 'w+')
    new_file.write(ciphertext)
    new_file.close()

    print('Файл с ключем сформирован.')

# Метод выбора варианта работы с файлом
def check_value(file, key):
    try:
        choice = input('1. Шифровка\n2. Расшифровка\nСделайте выбор: ')

        if choice == '1':
            encrypt_file(file, key)
            print(f'Файл {file} зашифрован.')
        elif choice == '2':
            decrypt_file(file, key)
            print(f'Файл {file} расшифрован.')
        else:
            print('Вы ввели что-то не то, теперь заново запускайте программу.')

    except:
        print('Введено не корректное значение!!!')

def main():
    choice = input('1. Сформировать ключ\n2. Работа с файлом\nСделайте выбор: ')

    if choice == '1':
        pass_generation()

    elif choice == '2':
        try:
            with ZipFile('password.zip', 'r') as zip_file:
                password = getpass('Введите пароль для доступа к файлу: ')
                file_key = input('Введите название файла с ключем: ')
                file = input('Введите путь к файлу: ')
        
                with zip_file.open(file_key, mode='r', pwd=password.encode()) as pas_file:
                    key_zip_file = pas_file.read()

                    check_value(file, key_zip_file)

        except:
            print('Что-то пошло не так!!!')
    else:
        print('Вы ввели что-то не то, теперь заново запускайте программу.') 

if __name__ == "__main__":
    main()