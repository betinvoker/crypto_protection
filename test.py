import os
from zipfile import ZipFile

password = '123'

with ZipFile("password.zip", "r") as zip_file:
    zip_file.setpassword(password.encode())
    try:
        t = zip_file.read('password.txt')
        print(t)
    except RuntimeError as e:
        print("Bad password")
