---
source_image: page_278.png
page_number: 278
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.92
tokens: 7400
characters: 1782
timestamp: 2025-12-24T08:52:48.916891
finish_reason: stop
---

В ключах для простого подстановочного шифра можно легко допустить ошибку, поскольку они довольно длинные и должны содержать каждую букву алфавита. Например, можно ввести ключ, в котором какая-то буква отсутствует или встречается дважды. Функция keyIsValid() в строке 14 проверяет допустимость ключа, и в случае обнаружения проблемы программа завершает работу, выводя сообщение об ошибке.

14. if not keyIsValid(myKey):
15.     sys.exit('There is an error in the key or symbol set.')

В строках 16–19 проверяется, чему равна переменная myMode — 'encrypt' или 'decrypt', и соответственно вызывается либо функция encryptMessage(), либо функция decryptMessage().

16. if myMode == 'encrypt':
17.     translated = encryptMessage(myKey, myMessage)
18. elif myMode == 'decrypt':
19.     translated = decryptMessage(myKey, myMessage)

Функции encryptMessage() и decryptMessage() возвращают строку зашифрованного или дешифрованного текста, которая сохраняется в переменной translated.

В строке 20 используемый ключ отображается на экране. Далее на экран выводится зашифрованное или дешифрованное сообщение, которое также копируется в буфер обмена.

20. print('Using key %s' % (myKey))
21. print('The %sed message is:' % (myMode))
22. print(translated)
23. pyperclip.copy(translated)
24. print()
25. print('This message has been copied to the clipboard.')

Строка 25 — последняя в функции main(). На этом программа завершает свою работу.
Далее мы рассмотрим, как в функции keyIsValid() применяется метод sort() для проверки допустимости ключа.

Списковый метод sort()

У списков есть метод sort(), располагающий элементы списка в определенном порядке. Возможность сортировки очень удобна, когда необходимо проверить, содержат ли два списка одни и те же элементы, пусть и расположенные иначе.