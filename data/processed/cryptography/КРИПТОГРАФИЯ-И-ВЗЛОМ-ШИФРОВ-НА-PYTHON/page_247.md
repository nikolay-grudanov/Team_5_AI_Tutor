---
source_image: page_247.png
page_number: 247
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.59
tokens: 7330
characters: 1405
timestamp: 2025-12-24T08:51:58.605628
finish_reason: stop
---

В этой главе...

• Кортежи
• Сколько различных ключей может иметь аффинный ключ
• Генерирование случайных ключей

Исходный код программы Affine Cipher

Откройте в редакторе файлов новое окно, выбрав пункты меню File⇒New File. Введите в этом окне приведенный ниже код и сохраните его в файле affineCipher.py. Убедитесь в том, что модуль pyperclip.py и модуль cryptomath.py, который мы создали в главе 13, находятся в той же папке, что и файл affineCipher.py.

affineCipher.py

1. # Программа аффинного шифрования
2. # https://www.nostarch.com/crackingcodes/ (BSD Licensed)
3.
4. import sys, pyperclip, cryptomath, random
5. SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
6.
7.
8. def main():
9.     myMessage = """A computer would deserve to be called intelligent if it could deceive a human into believing that it was human."
-Alan Turing"""
10.    myKey = 2894
11.    myMode = 'encrypt'  # задать 'encrypt' или 'decrypt'
12.
13.    if myMode == 'encrypt':
14.        translated = encryptMessage(myKey, myMessage)
15.    elif myMode == 'decrypt':
16.        translated = decryptMessage(myKey, myMessage)
17.    print('Key: %s' % (myKey))
18.    print('%sed text:' % (myMode.title()))
19.    print(translated)
20.    pyperclip.copy(translated)
21.    print('Full %sed text copied to clipboard.' % (myMode))
22.
23.
24. def getKeyParts(key):
25.    keyA = key // len(SYMBOLS)