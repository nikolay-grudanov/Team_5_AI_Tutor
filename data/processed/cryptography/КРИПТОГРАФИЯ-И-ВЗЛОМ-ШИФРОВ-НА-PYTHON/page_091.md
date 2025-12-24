---
source_image: page_091.png
page_number: 91
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.04
tokens: 7459
characters: 1760
timestamp: 2025-12-24T08:48:11.589097
finish_reason: stop
---

Исходный код программы Caesar Cipher

Ведите приведенный ниже код в редакторе файлов и сохраните его в файле caesarCipher.py. Затем загрузите модуль pyperclip.py, доступный по адресу https://inventwithpython.com/pyperclip.py, и поместите его в тот же каталог, в котором находится файл caesarCipher.py. Данный модуль будет импортироваться программой caesarCipher.py; подробнее об этом мы поговорим в разделе “Импорт модулей и установка переменных”.

Когда файлы будут готовы, нажмите клавишу <F5>, чтобы запустить программу. Если столкнетесь с ошибками или другими проблемами, сравните свой код с кодом, приведенным в книге, воспользовавшись онлайн-утилитой Diff по адресу https://inventwithpython.com/cracking/diff/.

caesarCipher.py

1. # Шифр Цезаря
2. # https://www.nostarch.com/crackingcodes/ (BSD Licensed)
3.
4. import pyperclip
5.
6. # Строка, подлежащая шифрованию/дешифрованию
7. message = 'This is my secret message.'
8.
9. # Ключ шифрования/дешифрования
10. key = 13
11.
12. # Установка режима работы: шифрование или дешифрование
13. mode = 'encrypt' # задать 'encrypt' или 'decrypt'
14.
15. # Все символы, которые могут быть зашифрованы
16. SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
17.
18. # Переменная, хранящая зашифрованную/дешифрованную форму сообщения
19. translated = ''
20.
21. for symbol in message:
22.     # Примечание: шифровать/дешифровать можно только символы,
23.     # включенные в строку SYMBOLS
24.     if symbol in SYMBOLS:
25.         symbolIndex = SYMBOLS.find(symbol)
26.         # Выполнить шифрование/дешифрование
27.         if mode == 'encrypt':
28.             translatedIndex = symbolIndex + key
29.         elif mode == 'decrypt':
30.             translatedIndex = symbolIndex - key