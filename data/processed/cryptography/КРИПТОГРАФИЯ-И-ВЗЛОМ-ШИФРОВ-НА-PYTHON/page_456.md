---
source_image: page_456.png
page_number: 456
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.18
tokens: 7407
characters: 1811
timestamp: 2025-12-24T08:57:36.480014
finish_reason: stop
---

Исходный код программы Public Key Cipher

Откройте в редакторе файлов новое окно, выбрав пункты меню File→New File. Введите в этом окне приведенный ниже код и сохраните его в файле publicKeyCipher.py.

publicKeyCipher.py

1. # Шифрование с открытым ключом
2. # https://www.nostarch.com/crackingcodes/ (BSD Licensed)
3.
4. import sys, math
5.
6. # Открытый и закрытый ключи для этой программы создаются
7. # программой makePublicPrivateKeys.py. Программа должна
8. # выполняться в той же папке, в которой находятся файлы ключей.
9.
10. SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
11.
12. def main():
13.     # Проверяем, что необходимо сделать: записать зашифрованное
14.     # сообщение в файл или дешифровать сообщение, прочитанное из файла
15.     filename = 'encrypted_file.txt' # файл для чтения/записи
16.     mode = 'encrypt' # задать 'encrypt' или 'decrypt'
17.
18.     if mode == 'encrypt':
19.         message = 'Journalists belong in the gutter because that is where the ruling classes throw their guilty secrets. Gerald Priestland. The Founding Fathers gave the free press the protection it must have to bare the secrets of government and inform the people. Hugo Black.'
20.         pubKeyFilename = 'al_sweigart_pubkey.txt'
21.         print('Encrypting and writing to %s...' % (filename))
22.         encryptedText = encryptAndWriteToFile(filename, pubKeyFilename, message)
23.
24.         print('Encrypted text:')
25.         print(encryptedText)
26.
27.     elif mode == 'decrypt':
28.         privKeyFilename = 'al_sweigart_privkey.txt'
29.         print('Reading from %s and decrypting...' % (filename))
30.         decryptedText = readFromFileAndDecrypt(filename, privKeyFilename)
31.
32.         print('Decrypted text:')
33.         print(decryptedText)
34.