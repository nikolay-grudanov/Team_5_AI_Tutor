---
source_image: page_125.png
page_number: 125
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.85
tokens: 7389
characters: 1590
timestamp: 2025-12-24T08:49:01.153993
finish_reason: stop
---

transpositionEncrypt.py

1. # Программа шифрования на основе перестановочного шифра
2. # https://www.nostarch.com/crackingcodes/ (BSD Licensed)
3.
4. import pyperclip
5.
6. def main():
7.     myMessage = 'Common sense is not so common.'
8.     myKey = 8
9.
10.    ciphertext = encryptMessage(myKey, myMessage)
11.
12.    # Отобразить зашифрованную строку, хранящуюся в переменной
13.    # ciphertext, вставив после нее символ '|' на случай, если
14.    # в конце зашифрованного сообщения имеются пробелы
15.    print(ciphertext + '|')
16.
17.    # Скопировать зашифрованную строку в буфер обмена
18.    pyperclip.copy(ciphertext)
19.
20.
21. def encryptMessage(key, message):
22.     # Каждая строка в списке ciphertext представляет столбец таблицы
23.     ciphertext = [''] * key
24.
25.     # Цикл по всем столбцам в списке ciphertext
26.     for column in range(key):
27.         currentIndex = column
28.
29.         # Цикл, пока значение currentIndex не превысит длину сообщения
30.         while currentIndex < len(message):
31.             # Поместить в конец текущего столбца в списке ciphertext
32.             # символ сообщения с индексом currentIndex
33.             ciphertext[column] += message[currentIndex]
34.
35.             # Увеличить значение currentIndex
36.             currentIndex += key
37.
38.     # Возврат списка ciphertext в виде единой строки
39.     return ''.join(ciphertext)
40.
41.
42. # Если файл transpositionEncrypt.py выполняется как программа
43. # (а не импортируется как модуль), вызвать функцию main()
44. if __name__ == '__main__':
45.     main()