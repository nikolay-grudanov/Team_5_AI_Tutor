---
source_image: page_223.png
page_number: 223
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.89
tokens: 7432
characters: 1853
timestamp: 2025-12-24T08:51:33.362923
finish_reason: stop
---

Отображение результатов взлома сообщения

Код взлома шифротекста помещен в функцию hackTransposition(), которая вызывается в строке 11 и будет определена в строке 21. Эта функция имеет один аргумент: зашифрованное сообщение, которое мы пытаемся взломать. Если функции удалось взломать шифротекст, она возвращает строку дешифрованного текста, в противном случае возвращается значение None.

11. hackedMessage = hackTransposition(myMessage)
12.
13. if hackedMessage == None:
14.     print('Failed to hack encryption.')
15. else:
16.     print('Copying hacked message to clipboard:')
17.     print(hackedMessage)
18.     pyperclip.copy(hackedMessage)

В строке 11 вызывается функция hackTransposition(), которая возвращает взломанное сообщение, если попытка оказалась удачной, или значение None. Результат сохраняется в переменной hackedMessage.

В строках 13 и 14 программа проверяет значение переменной hackedMessage и, если она равна None, сообщает пользователю о том, что взломать шифротекст не удалось.

Следующие четыре строки определяют, что будет делать программа, если функции удалось взломать шифротекст. В строке 17 выводится дешифрованное сообщение, а в строке 18 оно копируется в буфер обмена. Но для того, чтобы этот код заработал, мы должны определить функцию hackTransposition(), которая рассматривается ниже.

Получение взломанного сообщения

Функция hackTransposition() начинается парой инструкций print().

21. def hackTransposition(message):
22.     print('Hacking...')
23.
24.     # Выполнение программы на Python можно в любой момент прервать,
25.     # нажав <Ctrl+C> (Windows) или <Ctrl+D> (macOS и Linux):
26.     print('(Press Ctrl-C (on Windows) or Ctrl-D (on macOS and Linux) to quit at any time.)')

Поскольку программа проверяет множество ключей, она выводит сообщение о том, что предпринимается попытка дешифровать сообщение.