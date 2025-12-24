---
source_image: page_111.png
page_number: 111
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.99
tokens: 7371
characters: 1435
timestamp: 2025-12-24T08:48:40.645272
finish_reason: stop
---

щего постулата (максима Шеннона): "Враг знает систему". Частью шифра, сохраняющей секретность сообщения, является ключ, а в случае шифра Цезаря эту информацию можно легко раскрыть.

В этой главе...
• Принцип Керкгоффса и максима Шеннона
• Метод грубой силы
• Функция range()
• Форматирование строк

Исходный код программы Caesar Hacker

Откройте в файловом редакторе новое окно, выбрав пункты меню File→New File. Введите в этом окне приведенный ниже код и сохраните его в файле caesarHacker.py.

Когда файл будет готов, нажмите клавишу <F5>, чтобы запустить программу. Если столкнетесь с ошибками или другими проблемами, сравните свой код с кодом, приведенным в книге, воспользовавшись онлайн-утилитой Diff по адресу https://inventwithpython.com/cracking/diff/.

caesarHacker.py

1. # Программа взлома шифра Цезаря
2. # https://www.nostarch.com/crackingcodes/ (BSD Licensed)
3.
4. message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'
5. SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
6.
7. # Цикл по всем возможным значениям ключа
8. for key in range(len(SYMBOLS)):
9.     # Важно присвоить пустую строку переменной translated,
10.    # чтобы очистить ее от значения из предыдущей итерации
11.   translated = ''
12.
13.   # Остальная часть программы почти не изменилась
14.
15.   # Цикл по всем символам сообщения
16.   for symbol in message:
17.     if symbol in SYMBOLS:
18.       symbolIndex = SYMBOLS.find(symbol)