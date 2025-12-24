---
source_image: page_150.png
page_number: 150
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.39
tokens: 7324
characters: 1487
timestamp: 2025-12-24T08:49:35.148995
finish_reason: stop
---

Пример выполнения программы Transposition Decrypt

Выполнив программу расшифровки перестановочного шифра, вы должны получить следующий результат:

Common sense is not so common.

Если хотите дешифровать другое сообщение или использовать другой ключ, измените значения, присваиваемые переменным myMessage и myKey в строках 7 и 8.

Импорт модулей и функция main()

Первая часть программы transpositionDecrypt.py аналогична первой части программы transpositionEncrypt.py.

1. # Программа дешифрования перестановочного шифра
2. # https://www.nostarch.com/crackingcodes/ (BSD Licensed)
3.
4. import math, pyperclip
5.
6. def main():
7.     myMessage = 'Cenoonommstmme oo snnio. s s c'
8.     myKey = 8
9.
10.    plaintext = decryptMessage(myKey, myMessage)
11.
12.    # Вывести текст с завершающим символом '|' на случай,
13.    # если в конце дешифрованного сообщения имеются пробелы
14.    print(plaintext + '|')
15.
16.    pyperclip.copy(plaintext)

В строке 4 импортируются модули pyperclip и math. С помощью одной инструкции import можно импортировать сразу несколько модулей, разделив их имена запятыми.

В функции main(), определение которой начинается в строке 6, создаются переменные myMessage и myKey, а затем вызывается функция decryptMessage(). Возвращаемым значением функции decryptMessage() будет дешифрованный простой текст, восстановленный из шифротекста с помощью ключа. Этот текст сохраняется в переменной plaintext, которая выводится на экран (с завершающим символом верти-