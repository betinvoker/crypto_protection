import os
from zipfile import ZipFile
from getpass import getpass
import aes_cipher

data_encrypter = aes_cipher.DataEncrypter()
data_decrypter = aes_cipher.DataDecrypter()

def encryptfile(file, password):
    with open(file, 'rb') as f:
        data = f.read()
        data_encrypter.Encrypt(data, password)
        with open(file, 'wb') as f:
            f.write(data_encrypter.encrypted_data)

def decryptfile(file, password):
    with open(file, 'rb') as f:
        data = f.read()
        data_decrypter.Decrypt(data, password)
        with open(file, 'wb') as f:
            f.write(data_decrypter.decrypted_data)

def main():
    with ZipFile("password.zip", "r") as zip_file:
        password = getpass('Введите пароль: ')
        zip_file.setpassword(password.encode())

        try:
            file = input('Введите путь к файлу для работы: ')
            choice = input('1. Шифровка\n2. Расшифровка\nСделайте выбор: ')

            if choice == '1':
                encryptfile(file, password)
            elif choice == '2':
                decryptfile(file, password)
        except RuntimeError as e:
            print('Не правильный пароль!!!')
    
if __name__ == "__main__":
    main()