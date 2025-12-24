---
source_image: page_327.png
page_number: 327
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.19
tokens: 7389
characters: 1713
timestamp: 2025-12-24T08:54:11.109847
finish_reason: stop
---

6. LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
7.
8. def main():
9.     # Этот текст можно скопировать из файла примера (см. введение)
10.    myMessage = """Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist.""""
11.    myKey = 'ASIMOV'
12.    myMode = 'encrypt'  # задать 'encrypt' или 'decrypt'
13.
14.    if myMode == 'encrypt':
15.        translated = encryptMessage(myKey, myMessage)
16.    elif myMode == 'decrypt':
17.        translated = decryptMessage(myKey, myMessage)
18.
19.    print('%sed message:' % (myMode.title()))
20.    print(translated)
21.    pyperclip.copy(translated)
22.    print()
23.    print('The message has been copied to the clipboard.')

Зашифрованное или дешифрованное сообщение (в зависимости от того, какое значение присвоено переменной myMode) сохраняется в переменной translated, которая выводится на экран (строка 20) и копируется в буфер обмена (строка 21).

Создание строк с помощью списковых методов append() и join()

Почти во всех программах, рассмотренных в книге, нам приходилось создавать строки программным путем. Сначала объявлялась переменная, содержащая пустую строку, а затем в нее добавлялись символы путем конкатенации. Введите в интерактивной оболочке следующий код.

>>> building = ''
>>> for c in 'Hello world!':
...     building += c
...
>>> print(building)

В данном случае в цикле перебираются все символы строки 'Hello world!', которые конкатенируются со строкой, хранящейся в переменной building. По завершении цикла переменная building будет содержать всю исходную строку.

Несмотря на кажущуюся простоту, данная методика реализуется в Python слишком неэффективно. Намного быстрее начать с пустого списка и при-