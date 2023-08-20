import pyAesCrypt

password = input('Введите пароль для шифрованного файла: ')

#encrypt
pyAesCrypt.encryptFile('data.txt', 'data.txt.aes', password)

#decrypt
pyAesCrypt.decryptFile('data.txt.aes', 'data-2.txt', password)