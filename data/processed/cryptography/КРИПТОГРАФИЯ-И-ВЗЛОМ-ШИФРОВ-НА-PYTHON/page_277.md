---
source_image: page_277.png
page_number: 277
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.24
tokens: 7351
characters: 1736
timestamp: 2025-12-24T08:52:47.016921
finish_reason: stop
---

Using key LFWOAYUISVKMNXPBDCRJTQEGHZ
The decrypted message is:
If a man is offered a fact which goes against his instincts, he will scrutinize it closely, and unless the evidence is overwhelming, he will refuse to believe it. If, on the other hand, he is offered something which affords a reason for acting in accordance to his instincts, he will accept it even on the slightest evidence. The origin of myths is explained in this way.
-Bertrand Russell

This message has been copied to the clipboard.

Импорт модулей, настройка констант и функция main()

Рассмотрим начальный фрагмент программы.

1. # Простой подстановочный шифр
2. # https://www.nostarch.com/crackingcodes/ (BSD Licensed)
3.
4. import pyperclip, sys, random
5.
6.
7. LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

В строке 4 импортируются модули pyperclip, sys и random. Значением константы LETTERS становится строка, содержащая все буквы алфавита в верхнем регистре. Это символьный набор для простого подстановочного шифра.

Функция main() напоминает аналогичные функции программ шифрования, рассмотренных в предыдущих главах. В переменных myMessage, myKey и myMode задаются используемые в программе сообщение, ключ и режим соответственно.

9. def main():
10.    myMessage = 'If a man is offered a fact which goes against his instincts, he will scrutinize it closely, and unless the evidence is overwhelming, he will refuse to believe it. If, on the other hand, he is offered something which affords a reason for acting in accordance to his instincts, he will accept it even on the slightest evidence. The origin of myths is explained in this way.
    -Bertrand Russell'
11.    myKey = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
12.    myMode = 'encrypt'  # задать 'encrypt' или 'decrypt'